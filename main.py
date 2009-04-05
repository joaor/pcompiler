from ply import lex

reserved = { 'and' : 'AND'}

# List of token names
tokens = ('AND','NUM','VAR','EQUALS','ADDOP','SUBOP','MULOP','DIVOP','LPAREN','RPAREN')

# Regular statement rules for tokens.
t_EQUALS = r'='
t_ADDOP = r'\+'
t_SUBOP = r'-'
t_MULOP = r'\*'
t_DIVOP = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_VAR(t):
	r'[a-zA-Z_][\w_]*'
	if t.value in reserved:
		t.type = reserved.get(t.value)    # Check for reserved words
	return t

# A regular statement rule with some action code.
def t_NUM(t):
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


