from structures import variable_table, semantic_cube, function_directory

def declarar_variable(var_name, var_type, scope):
    if scope not in variable_table:
        variable_table[scope] = {}

    if var_name in variable_table[scope]:
        print(f"[Error] Variable '{var_name}' ya fue declarada")
        return False
    
    variable_table[scope][var_name] = var_type
    return True


def obtener_tipo_variable(var_name, scope):
    if var_name in variable_table.get(scope, {}):
        return variable_table[scope][var_name]
    elif var_name in variable_table['global']:
        return variable_table['global'][var_name]
    else:
        print(f"[Error] Variable '{var_name}' no declarada")
        return None
    
def obtener_tipo_expresion(expr):
    if isinstance(expr, int):
        return 'int'
    elif isinstance(expr, float):
        return 'float'
    elif isinstance(expr, str):
        return 'string'
    elif isinstance(expr, tuple) and expr[0] == 'id':
        return expr[2]
    elif isinstance(expr, tuple) and expr[0] == 'binop':
        _, op, left, right = expr
        tipo_izq = obtener_tipo_expresion(left)
        tipo_der = obtener_tipo_expresion(right)

        if tipo_izq and tipo_der and op in semantic_cube.get(tipo_izq, {}).get(tipo_der, {}):
            return semantic_cube[tipo_izq][tipo_der][op]
        else:
            print(f"[Error] Operación inválida: {tipo_izq} {op} {tipo_der}")
            return None
    return None 

def validar_parametros_unicos(param_list, func_name):
    nombres = [param[2] for param in param_list]
    if len(nombres) != len(set(nombres)):
        print(f"[Error] Parámetros duplicados en la función '{func_name}'")
        return False
    return True

def validar_funcion_existe(nombre_funcion):
    if nombre_funcion not in function_directory:
        print(f"[Error] Función '{nombre_funcion}' no ha sido declarada")
        return False
    return True

def validar_numero_argumentos(nombre_funcion, argumentos):
    num_esperado = len(function_directory[nombre_funcion]['params'])
    num_recibido = len(argumentos)

    if num_esperado != num_recibido:
        print(f"[Error] Número de argumentos incorrecto en llamada a '{nombre_funcion}': se esperaban {num_esperado}, se recibieron {num_recibido}")
        return False
    return True

def validar_tipos_argumentos(nombre_funcion, argumentos):
    parametros = function_directory[nombre_funcion]['params']

    for i, (arg, param) in enumerate(zip(argumentos, parametros), 1):
        tipo_argumento = obtener_tipo_expresion(arg)
        tipo_esperado = param[1]

        if tipo_argumento != tipo_esperado:
            print(f"[Error] Tipo incorrecto en argumento {i} de llamada a '{nombre_funcion}': se esperaba {tipo_esperado}, se recibio {tipo_argumento}")
            return False

    return True

def validar_return_en_funcion(func_name, block_statements):
    return_type = function_directory[func_name]['return_type']
    tiene_return = False

    for stmt in block_statements:
        if isinstance(stmt, tuple) and stmt[0] == 'return':
            tiene_return = True

            if return_type == 'void':
                print(f"[Error] La función '{func_name}' es void y no debe retornar un valor.")
                return False
            tipo_return = obtener_tipo_expresion(stmt[1])

            if tipo_return != return_type:
                print(f"[Error] La función '{func_name}' debe retornar '{return_type}', pero se encontró '{tipo_return}'")
                return False

    if return_type != 'void' and not tiene_return:
        print(f"[Error] La función '{func_name}' debe contener al menos un return de tipo '{return_type}'")
        return False

    return True

def validar_que_no_sea_variable(nombre, scope):
    if nombre in variable_table.get(scope, {}) or nombre in variable_table['global']:
        print(f"[Error] '{nombre}' es una variable, no puede ser usada como función")
        return False
    return True