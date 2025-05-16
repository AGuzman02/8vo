import ply.lex as lex

#reserved words
reserved = {
    'def': 'DEF',
    'true': 'TRUE',
    'false': 'FALSE',
    'none': 'NONE',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'is': 'IS',
    'if': 'IF',
    'elif': 'ELIF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'pass': 'PASS',
    'try': 'TRY',
    'except': 'EXCEPT',
    'return': 'RETURN',
    'import': 'IMPORT',
    'from': 'FROM',
    'as': 'AS',
    'print': 'PRINT',
    'int': 'INT_TYPE',
    'program': 'PROGRAM',
    'float': 'FLOAT_TYPE',
    'string': 'STRING',
    'var': 'VAR',
    'main': 'MAIN',
    'void': 'VOID',
    'end': 'END',
    }



# List of token names
tokens = [
    "ID",
    "EQUAL",
    "EQ",
    "NEQ",
    "GT",
    "LT",
    "GTE",
    "LTE",
    "PLUS",
    "MINUS",
    "MULT",
    "DIV",
    "LPAREN",
    "RPAREN",
    "LBRACE",
    "RBRACE",
    "LBRACKET",
    "RBRACKET",
    "SEMI",
    "COLON",
    "COMMA",
    "COMMENT",
    "INT",
    "FLOAT",
] + list(reserved.values())

# Regular expression rules for simple tokens
t_EQUAL=r'='
t_EQ=r'=='
t_NEQ=r'!='
t_GT=r'>'
t_LT=r'<'
t_GTE=r'>='
t_LTE=r'<='
t_PLUS=r'\+'
t_MINUS=r'-'
t_MULT=r'\*'
t_DIV=r'/'
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_LBRACE=r'\{'
t_RBRACE=r'\}'
t_LBRACKET=r'\['
t_RBRACKET=r'\]'
t_SEMI=r';'
t_COLON=r':'
t_COMMA=r','

# A regular expression rule with some action code
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*\b'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t

def t_FLOAT(t):
    r'[0-9]+\.[0-9]+\b'
    t.value=float(t.value)
    return t

def t_INT(t):
    r'[0-9]+\b'
    t.value=int(t.value)
    return t

def t_STRING(t):
    r'"[^"\n]*"'
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


#file = 'test.cpp'

#with open(file) as f:
    # Give the lexer some input
    #for x in f:
        #lexer.input(x)

        # Tokenize
        #while True:
            #tok = lexer.token()
            #if not tok: 
                #break   
            #print(tok)   # No more input



# When executed, the example will produce the following output:

# $ python example.py
# LexToken(NUMBER,3,2,1)
# LexToken(PLUS,'+',2,3)
# LexToken(NUMBER,4,2,5)
# LexToken(TIMES,'*',2,7)
# LexToken(NUMBER,10,2,10)
# LexToken(PLUS,'+',3,14)
# LexToken(MINUS,'-',3,16)
# LexToken(NUMBER,20,3,18)
# LexToken(TIMES,'*',3,20)
# LexToken(NUMBER,2,3,21)

