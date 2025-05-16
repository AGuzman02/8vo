
current_function = 'global'
function_directory = {}

variable_table = {
    'global': {}
}

semantic_cube = {
    'int': {
        'int': {
            '=': 'int', '+': 'int', '-': 'int', '*': 'int', '/': 'int',
            '<': 'int', '>': 'int', '<=': 'int', '>=': 'int', '==': 'int', '!=': 'int'
        },
        'float': {},
        'string': {}
    },
    'float': {
        'float': {
            '=': 'float', '+': 'float', '-': 'float', '*': 'float', '/': 'float',
            '<': 'int', '>': 'int', '<=': 'int', '>=': 'int', '==': 'int', '!=': 'int'
        },
        'int': {
            '=': 'float', '+': 'float', '-': 'float', '*': 'float', '/': 'float',
            '<': 'int', '>': 'int', '<=': 'int', '>=': 'int', '==': 'int', '!=': 'int'
        },
        'string': {}
    },
    'string': {
        'string': {
            '=': 'string', '+': 'string', '==': 'int', '!=': 'int'
        },
        'int': {},
        'float': {}
    }
}