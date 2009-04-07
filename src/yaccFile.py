# Yacc example

from ply import yacc

# Get the token map from the lexer that we defined
# earlier.  This is required.

from lexFile import tokens

__var_names = {}

def p_assign_statement(t):
	'assign_statement : VAR EQUALS statement'
	__var_names[t[1]] = t[3]

def p_statement_plus(t):
	'statement : statement ADD_OP term'
	t[0] = t[1] + t[3]

def p_statement_minus(t):
	'statement : statement SUB_OP term'
	t[0] = t[1] - t[3]

def p_statement_term(t):
	'statement : term'
	t[0] = t[1]

def p_term_times(t):
	'term : term MUL_OP factor'
	t[0] = t[1] * t[3]

def p_term_div(t):
	'term : term DIV_OP factor'
	t[0] = t[1] / t[3]

def p_term_factor(t):
	'term : factor'
	t[0] = t[1]

def p_factor_num(t):
	'factor : INTEGER'
	t[0] = t[1]

def p_factor_var(t):
	'factor : VAR'
	if __var_names.has_key(t[1]):
		t[0] = __var_names[t[1]]
	else:
		print "Undefined Variable", t[1], "in line no.", t.lineno(1)

def p_factor_expr(t):
	'factor : LEFT_PAREN statement RIGHT_PAREN'
	t[0] = t[2]

# Error rule for syntax errors
def p_error(t):
	print "Syntax error in input!"

# Build the parser
yacc.yacc()

while 1:

	try:
		s = raw_input('enter > ')
	except EOFError:
		break
	if not s:
		continue
	yacc.parse(s)




