import ply.yacc as yacc
import apps.Usuario.lexer as lexer

precedence = (
	('nonassoc', 'LESSTHAN', 'GREATERTHAN'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    )

tokens = lexer.tokens

names = { }
printed_info = []

def p_statement_assign(t):
    '''statement : NAME EQUALS expression END_OF_SENTENCE'''
    try:
    	names[t[1]] = t[3]
    except:
        #print("Nombre indefinido '%s'" % t[1])
        names[t[0]] = 0
        printed_info.append("Nombre indefinido")

def p_statement_print(p):
    '''statement : PRINT LPAREN expression RPAREN END_OF_SENTENCE'''
    print(p[3])
    printed_info.append(p[3])

def p_statement_expr(t):
    'statement : expression END_OF_SENTENCE'

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression LESSTHAN expression
                  | expression GREATERTHAN expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]
    elif t[2] == '<': t[0] = bool(t[1] < t[3])
    elif t[2] == '>': t[0] = bool(t[1] > t[3])

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    '''expression : NUMBER
    			  | TRUE
    			  | FALSE
    			  | STRING'''
    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
    try:
        t[0] = names[t[1]]
    except LookupError:
        #print("Nombre indefinido '%s'" % t[1])
        printed_info.append("Identificador indefinido")
        t[0] = 0

def p_error(t):
    #print("Error de sintaxis en '%s'" % t.value)
    var = "Error de sintaxis"
    printed_info.append(var)

p = yacc.yacc()

"""
contenido = ""

with open('codigo.txt', 'r') as file:
    contenido = file.readlines()

for i in contenido:
    t = parser.parse(i)

print("RESULTADOS")

for i in names:
    print(names[i])


while True:
    try:
        s = input('calc > ') 
    except EOFError:
        break

    try:
    	t = parser.parse(s)
    except:
    	print("Expresion no valida")
"""

