# Yacc example

from ply import yacc

# Get the token map from the lexer that we defined
# earlier.  This is required.

from lexFile import tokens

#def p_program(t):
#	'program : program_heading SEMICOLON block DOT'

def p_program_heading(t):
	'''program_heading : PROGRAM VAR
				    | PROGRAM VAR LEFT_PAREN identifier_list RIGHT_PAREN'''

def p_identifier_list(t):
	'''identifier_list : identifier_list COMMA VAR
				    | VAR'''

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




