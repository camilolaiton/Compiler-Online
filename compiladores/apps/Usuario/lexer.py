import ply.lex as lex

tokens = [
    'NAME','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN','GREATERTHAN','LESSTHAN','TRUE',
    'FALSE', 'STRING', 'END_OF_SENTENCE', 'PRINT'
    ]

t_END_OF_SENTENCE = r';'
t_LESSTHAN= r'<'
t_GREATERTHAN = r'>'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("El entero es muy largo %d", t.value)
        t.value = 0
    return t

def t_PRINT(t):
    'escriba'
    return t

def t_TRUE(t):
    'true'
    t.value = True
    return t

def t_FALSE(t):
    'false'
    t.value = False
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_STRING(t):
    r'"(?:\\"|.)*?"'

    t.value = bytes(t.value.lstrip('"').rstrip('"'), "utf-8").decode("unicode_escape")

    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

"""
lexer.input('x = 5 + 4 - 5 "hola" false true () hola >')

while True:
    tok = lexer.token()

    if not tok: 
        break      # No more input
    #print(tok)
"""