import ply.lex as lex

# List of token names
tokens = (
   'DEF',
   'ID',
   'INT',
   'FLOAT',
   'STRING',
   'TRUE',
   'FALSE',
   'NONE',
   'AND',
   'OR',
   'NOT',
   'IS',
   'IF',
   'ELIF',
   'ELSE',
   'FOR',
   'WHILE',
   'BREAK',
   'CONTINUE',
   'PASS',
   'TRY',
   'EXCEPT',
   'RETURN',
   'IMPORT',
   'FROM',
   'AS',
   'PRINT',
   'EQUAL',
   'EQ',
   'NEQ',
   'GT',
   'LT',
   'GTE',
   'LTE',
   'PLUS',
   'MINUS',
   'MULT',
   'DIV',
   'LPAREN',
   'RPAREN',
   'LBRACE',
   'RBRACE',
   'LBRACKET',
   'RBRACKET',
   'SEMI',
   'COLON',
   'COMMA',
   'COMMENT',
   'IN',
   'PROGRAM',
   'VAR',
   'MAIN',
   'VOID',
   'END',
   'INT_TYPE',
   'FLOAT_TYPE'
)

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

#Keywords
def t_DEF(t):
    r'\bdef\b'
    return t

def t_TRUE(t):
    r'\btrue\b'
    return t

def t_FALSE(t):
    r'\bfalse\b'
    return t

def t_NONE(t):
    r'\bnone\b'
    return t

def t_AND(t):
    r'\band\b'
    return t

def t_OR(t):
    r'\bor\b'
    return t

def t_NOT(t):
    r'\bnot\b'
    return t

def t_IS(t):
    r'\bis\b'
    return t

def t_IF(t):
    r'\bif\b'
    return t

def t_ELIF(t):
    r'\belif\b'
    return t

def t_ELSE(t):
    r'\belse\b'
    return t

def t_FOR(t):
    r'\bfor\b'
    return t

def t_WHILE(t):
    r'\bwhile\b'
    return t

def t_BREAK(t):
    r'\bbreak\b'
    return t

def t_CONTINUE(t):
    r'\bcontinue\b'
    return t

def t_PASS(t):
    r'\bpass\b'
    return t

def t_TRY(t):
    r'\btry\b'
    return t

def t_EXCEPT(t):
    r'\bexcept\b'
    return t

def t_RETURN(t):
    r'\breturn\b'
    return t

def t_IMPORT(t):
    r'\bimport\b'
    return t

def t_FROM(t):
    r'\bfrom\b'
    return t

def t_AS(t):
    r'\bas\b'
    return t

def t_PRINT(t):
    r'\bprint\b'
    return t

def t_IN(t):
    r'\bin\b'
    return t

def t_PROGRAM(t):
    r'\bprogram\b'
    return t

def t_VAR(t):
    r'\bvar\b'
    return t

def t_MAIN(t):
    r'\bmain\b'
    return t

def t_VOID(t):
    r'\bvoid\b'
    return t

def t_END(t):
    r'\bend\b'
    return t

def t_INT_TYPE(t):
    r'\bint\b'
    return t

def t_FLOAT_TYPE(t):
    r'\bfloat\b'
    return t

# A regular expression rule with some action code
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*\b'
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
    return t

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

file = 'plyex.txt'

with open(file) as f:
    # Give the lexer some input
    for x in f:
        lexer.input(x)

        # Tokenize
        while True:
            tok = lexer.token()
            if not tok: 
                break      # No more input
            print(tok)



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