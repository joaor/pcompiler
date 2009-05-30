from ply import lex

#dicionario de palavras reservadas
reserved = {
	'and' 		:	'AND',
	'or'			:	'OR',
	'not'		:	'NOT',
	'if'			:	'IF',
	'for'		:	'FOR',
	'while'		:	'WHILE',
	'repeat'		:	'REPEAT',
	'mod'		:	'MOD',
	'div'		:	'DIV',
	'true'		:	'TRUE',
	'false'		:	'FALSE',
	'program'		:	'PROGRAM',
	'begin'		:	'BEGIN',
	'end'		:	'END',
	'then'		:	'THEN',
	'type'		:	'TYPE',
	'const'		:	'CONST',
	'else'		:	'ELSE',
	'procedure'	:	'PROCEDURE',
	'function'	:	'FUNCTION',
	'in'			:	'IN',
	'nil'		:	'NIL',
	'var'		:	'VAR',
	'do'			:	'DO',
	'to'			:	'TO',
	'downto'		:	'DOWNTO',
	'until'		:	'UNTIL'
}

#Lista de tokens
tokens = ('INTEGER','VAR','REAL','BOOLEAN','CHAR',
					'ADD_OP','SUB_OP','MUL_OP','DIV_OP','MOD','DIV',
					'LEFT_PAREN','RIGHT_PAREN',
					'AND','OR','NOT',
					'TRUE','FALSE',
					'IF','FOR','WHILE','REPEAT','ELSE',
					'EQUALS','LESS','GREATER','GREATER_OR_EQUAL','LESS_OR_EQUAL','NOT_EQUAL',
					'DECLARATOR','BEGIN','END','PROGRAM','TYPE','CONST','PROCEDURE','FUNCTION',
				 	'SEMICOLON', 'COMMA', 'COLON',
					'COMMENT', 'STRING','DOT','THEN','EXP','NIL','IN','IDENTIFIER','DO','TO','DOWNTO','UNTIL')

#Expressoes regulares para cada token
t_EQUALS = r'='
t_ADD_OP = r'\+'
t_SUB_OP = r'-'
t_MUL_OP = r'\*'
t_EXP = r'\*\*'
t_DIV_OP = r'/'
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'
t_GREATER	=	r'>'
t_LESS	=	r'<'
t_GREATER_OR_EQUAL	=	r'>='
t_LESS_OR_EQUAL	=	r'<='
t_NOT_EQUAL	=	r'<>'
t_DECLARATOR	=	r':='
t_SEMICOLON = r';'
t_COMMA = r','
t_COLON = r':'
t_COMMENT = r' (\{ [^\}]* \}) | (\(\* [^(\*\))]* \*\))'
t_STRING = r" (\' [^\']* \') | (\" [^\"]* \") "
t_DOT = r'\.'

def t_IDENTIFIER(t):
	r'[a-zA-Z_][\w_]*'
	if t.value.lower() in reserved:
		t.type = reserved.get(t.value.lower())
	return t

def t_BOOLEAN(t):
	r'"true"|"false"'
	try:
		t.value = bool(t.value)
	except ValueError:
		print "Line %d: Number %s is too large!" % (t.lineno, t.value)
		t.value = False
	return t

def t_CHAR(t):
	r'(\'[\w]\') | (\"[\w]\")'
	return t

def t_REAL(t):
	r'[0-9]+\.[0-9]+'
	try:
		t.value = float(t.value)
	except ValueError:
		print "Line %d: Number %s is too large!" % (t.lineno, t.value)
		t.value = 0.0
	return t

def t_INTEGER(t):
    r'[0-9]+'
    try:
    	t.value = int(t.value)
    except ValueError:
    	print "Line %d: Number %s is too large!" % (t.lineno, t.value)
    	t.value = 0
    return t

def t_newline(t):
    r'\n+'
    t.lineno += len(t.value)

#Caracteres igorados
t_ignore  = ' \t'

#Caso haja erro
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.skip(1)

lex.lex()


if __name__=="__main__":
	data = raw_input()
	lex.input(data)
	while 1 :
		   tok = lex.token()
		   if not tok :
		           break
		   print tok


