# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer. This is required.
from entrega1 import tokens

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
    print(f"Parsed declaration: {p[2]} of type {p[4]}")
    p[0] = ('declaration', p[2], p[4])   

def p_functions(p):
    '''functions : functions function
                 | empty'''
    print("Parsed functions")
    p[0] = p[1] + [p[2]] if len(p) == 3 else []


def p_function(p):
    'function : VOID ID LPAREN parameters RPAREN COLON type block'
    p[0] = ('function', p[2], p[4], p[7], p[8])

def p_factor_funccall(p):
    'factor : ID LPAREN args RPAREN'
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
    p[0] = ('assignment', p[1], p[3])


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
    p[0] = ('id', p[1])

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

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

# Test the parser with the contents of plyex.cpp
file = 'plyex.cpp'
with open(file, 'r') as f:
    data = f.read()
    result = parser.parse(data)
    print(result)




