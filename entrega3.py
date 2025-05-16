import os
import ply.yacc as yacc
from entrega1 import tokens
from structures import *
from semantic import *

# Program structure
def p_program(p):
    'program : PROGRAM ID SEMI declarations functions MAIN block END'
    print("Parsed program")
    p[0] = ('program', p[2], p[4], p[5], p[7])

# Declarations
def p_declarations(p):
    '''declarations : declarations declaration
                    | empty'''
    print("Parsed declarations")
    p[0] = p[1] + [p[2]] if len(p) == 3 else []

def p_declaration(p):
    'declaration : VAR ID COLON type SEMI'
    var_name = p[2]
    var_type = p[4]
    
    if declarar_variable(var_name, var_type, current_function):
        p[0] = ('declaration', var_name, var_type)
    else:
        p[0] = None  

def p_functions(p):
    '''functions : functions function
                 | empty'''
    print("Parsed functions")
    p[0] = p[1] + [p[2]] if len(p) == 3 else []


def p_function(p):
    'function : VOID ID LPAREN parameters RPAREN COLON type block'
    global current_function
    func_name = p[2]
    param_list = p[4]
    return_type = p[7]
    block = p[8]
    
    previous_function = current_function
    current_function = func_name

    if func_name in function_directory:
        print(f"[Error] La función '{func_name}' ya está declarada")
        p[0] = None
        return
    
    if func_name in variable_table['global']:
        print(f"[Error] El nombre '{func_name}' ya está usado como variable global, no puede ser usado como función")
        p[0] = None
        return
    
    function_directory[func_name] = {
        'return_type': return_type,
        'params': param_list
    }

    variable_table[func_name] = {}

    if not validar_parametros_unicos(param_list, func_name):
        p[0] = None
        return
    
    for param in param_list:
        variable_table[func_name][param[2]] = param[1]

    if not validar_return_en_funcion(func_name, block[1]):
        p[0] = None
        return

    current_function = previous_function
    p[0] = ('function', p[2], p[4], p[7], p[8])

def p_factor_funccall(p):
    'factor : ID LPAREN args RPAREN'
    nombre_funcion = p[1]
    argumentos = p[3]

    if not validar_que_no_sea_variable(nombre_funcion, current_function):
        p[0] = None
        return
    
    if not validar_funcion_existe(nombre_funcion):
        p[0] = None
        return
    
    if not validar_numero_argumentos(nombre_funcion, argumentos):
        p[0] = None
        return
    
    if not validar_tipos_argumentos(nombre_funcion, argumentos):
        p[0] = None
        return
    
    p[0] = ('funccall', p[1], p[3])

def p_args(p):
    '''args : args COMMA expression
            | expression
            | empty'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2 and p[1] != None:
        p[0] = [p[1]]
    else:
        p[0] = []

# Parameters
def p_parameters(p):
    '''parameters : parameters COMMA parameter
                  | parameter
                  | empty'''
    p[0] = p[1] + [p[3]] if len(p) == 4 else [p[1]] if len(p) == 2 else []

def p_parameter(p):
    'parameter : type ID'
    p[0] = ('parameter', p[1], p[2])

# Type
def p_type(p):
    '''type : INT_TYPE
            | FLOAT_TYPE
            | VOID
            | STRING'''
    p[0] = p[1]

# Block
def p_block(p):
    'block : LBRACE statements RBRACE'
    p[0] = ('block', p[2])

# Statements
def p_statements(p):
    '''statements : statements statement
                  | empty'''
    p[0] = p[1] + [p[2]] if len(p) == 3 else []

def p_statement(p):
    '''statement : declaration
                 | assignment
                 | if_statement
                 | while_statement
                 | print_statement
                 | return_statement'''
    p[0] = p[1]

# Assignment
def p_assignment(p):
    'assignment : ID EQUAL expression SEMI'
    var_name = p[1]
    var_type = obtener_tipo_variable(var_name, current_function)

    if var_type is None:
        p[0] = None
        return

    expr_type = obtener_tipo_expresion(p[3])

    if expr_type is None:
        p[0] = None
        return

    if '=' in semantic_cube.get(var_type, {}).get(expr_type, {}):
        p[0] = ('assignment', var_name, p[3])
    else:
        print(f"[Error] Asignación inválida: no se puede asignar tipo '{expr_type}' a variable '{var_name}' de tipo '{var_type}'")
        p[0] = None

# If statement
def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN block ELSE block
                    | IF LPAREN expression RPAREN block'''
    p[0] = ('if', p[3], p[5], p[7] if len(p) == 8 else None)

# While statement
def p_while_statement(p):
    'while_statement : WHILE LPAREN expression RPAREN block'
    p[0] = ('while', p[3], p[5])

# Print statement
def p_print_statement(p):
    '''print_statement : PRINT LPAREN STRING RPAREN SEMI
                        | PRINT LPAREN expression RPAREN SEMI'''
    p[0] = ('print', p[3])

# Return statement
def p_return_statement(p):
    'return_statement : RETURN expression SEMI'
    p[0] = ('return', p[2])

# Expressions
def p_expression_binop(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | expression GT term
                  | expression LT term
                  | expression GTE term
                  | expression LTE term
                  | expression EQ term
                  | expression NEQ term'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

# Term
def p_term_binop(p):
    '''term : term MULT factor
            | term DIV factor'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

# Factor
def p_factor_num(p):
    'factor : INT'
    p[0] = p[1]
 
def p_factor_id(p):
    'factor : ID'
    var_name = p[1]
    var_type = obtener_tipo_variable(var_name, current_function)

    p[0] = ('id', var_name, var_type) if var_type else None

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_factor_string(p):
    'factor : STRING'
    p[0] = p[1]

def p_factor_float(p):
    'factor : FLOAT'
    p[0] = p[1]

# Empty rule
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at token {p.type}, value {p.value}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

test_dir = 'tests'
for filename in os.listdir(test_dir):
    if filename.endswith('.cpp'):
        file_path = os.path.join(test_dir, filename)
        print(f"\n--- Prueba: {filename} ---")
        
        variable_table.clear()
        variable_table['global'] = {}
        function_directory.clear()
        current_function = 'global'

        parser = yacc.yacc(debug=False, write_tables=False)

        with open(file_path, 'r') as f:
            data = f.read()
            result = parser.parse(data)