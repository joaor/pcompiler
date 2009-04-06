from ply import lex

reserved = { 'and' 			:	'AND',
							'or'			:	'OR',
							'not'			:	'NOT',
							'if'			:	'IF',
							'for'			:	'FOR',
							'while'		:	'WHILE',
							'repeat'	:	'REPEAT',
							'mod'			:	'MOD',
							'div'			:	'DIV',
							'true'		:	'TRUE',
							'false'		:	'FALSE',
							'program'	:	'PROGRAM',
							'begin'		:	'BEGIN',
							'end'			:	'END',
							'writeln'	:	'WRITELN',
							'write'		:	'WRITE',
							'readln'	:	'READLN',
							'read'		:	'READ',
							'then'	:	'THEN'}

# List of token names
tokens = ('INTEGER','VAR','REAL','BOOLEAN','CHAR',
					'ADD_OP','SUB_OP','MUL_OP','DIV_OP','MOD','DIV',
					'LEFT_PAREN','RIGHT_PAREN',
					'AND','OR','NOT',
					'TRUE','FALSE',
					'IF','FOR','WHILE','REPEAT',
					'EQUALS','LESS','GREATER','GREATER_OR_EQUAL','LESS_OR_EQUAL','NOT_EQUAL',
					'DECLARATOR', 'BEGIN', 'END', 'PROGRAM',
					'WRITE', 'WRITELN', 'READLN', 'READ', 'SEMICOLON', 'COMMA', 'COLON',
					'COMMENT', 'STRING','DOT','THEN')

# Regular statement rules for tokens.
t_EQUALS = r'='
t_ADD_OP = r'\+'
t_SUB_OP = r'-'
t_MUL_OP = r'\*'
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

def t_VAR(t):
	r'[a-zA-Z_][\w_]*'
	if t.value.lower() in reserved:
		t.type = reserved.get(t.value.lower())    # Check for reserved words
	return t

def t_CHAR(t):
	r'[a-zA-Z]'
	return t

def t_REAL(t):
	r'[0-9]+\.[0-9]+'
	return t

# A regular statement rule with some action code.
def t_INTEGER(t):
    r'[0-9]+'
    try:
         t.value = int(t.value)
    except ValueError:
         print "Line %d: Number %s is too large!" % (t.lineno, t.value)
    t.value = 0
    return t


# Define a rule so that we can track line numbers.
def t_newline(t):
    r'\n+'
    t.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs).
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.skip(1)

# Build the lexer
lex.lex()

# Get the input
data = raw_input()

lex.input(data)

# Tokenize
while 1 :
        tok = lex.token()
        if not tok :
                break
        print tok


