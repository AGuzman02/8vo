'''
FuncTable = 
{ 
Function Name : 
  {
    FunctionName: name,
    VarTable: {
                Variable Name : var_type, 
                Variable Name : var_type, 
                Variable Name : var_type, 
              } 
  },


  }

'''



# variable types
VarType = ["int", "float", "string"]
OperatorType = ["+", "-", "*", "/", "<", ">", "!=", "=", "PRINT"]

# possible values for constants
ValueType = str | int | float


class Var:
  def __init__(self, var_type):
    self.var_type = var_type
VarTableType = dict[str, Var] #{Variable Name: Variable Object}

class VarTable:
  def __init__(self):
    self.vars: VarTableType = {}

  def add_var(self, name, var_type):
    if name in self.vars:
      raise Exception(f"Variable {name} already declared")
    self.vars[name] = Var(var_type)

  def get_var(self, name): 
    return self.vars[name] if name in self.vars else None

  def get_type(self, name):
    return self.vars[name].var_type if name in self.vars else None
  
class Function:
  def __init__(self, name, args):
    self.name = name
    self.vars = VarTable()
    for arg in args:
      type = arg.split(' ')[0]
      var_name = arg.split(' ')[1]
      self.vars.add_var(var_name, type)

FunctionTableType = dict[str, Function] #{Function Name: Function Object}

class FunctionTable:
  def __init__(self):
    self.funcs = FunctionTableType

  def add_function(self, name, args):
    if name in self.funcs:
      print('Error Doble dclaracion de funcion')
    else:
      self.funcs[name] = Function(name, [])

  def get_function(self, name):
    func = self.funcs[name]
    if func is None:
      print('Error de funcion no declarada')
    return func

  def add_var(self, name, var, var_type):
    func = self.get_function(name)
    func.vars.add_var(var, var_type)
  
  def get_var(self, func_name, var_name):
    func = self.get_function(func_name)
    return func.var_table.get_var(var_name)