from ply import yacc
from lexFile import tokens

#Estrutura do programa e o seu bloco de codigo---------------------------------
def p_program(t):
	'program : program_heading SEMICOLON block DOT'

def p_block(t):
	'block : constant_list'


#Definicao do heading do programa------------------------------------------------
def p_program_heading(t):
	'''program_heading : PROGRAM VAR
				    | PROGRAM VAR LEFT_PAREN identifier_list RIGHT_PAREN'''

def p_identifier_list(t):
	'''identifier_list : identifier_list COMMA VAR
				    | VAR'''


#Definicao de constantes----------------------------------------------------------
def p_constant_list(t):
	'''constant_list 	: constant_list constant_definition
 					| constant_definition'''

def p_constant_definition(t):
	'constant_definition : VAR EQUALS cexpression SEMICOLON'

def p_cexpression(t):
	'''cexpression : csimple_expression
 				| csimple_expression relop csimple_expression'''

def p_csimple_expression(t):
	'''csimple_expression : cterm
 					  | csimple_expression addop cterm'''

def p_cterm(t):
	'''cterm  : cfactor
 			| cterm mulop cfactor'''

def p_cfactor(t):
	'''cfactor : sign cfactor
 			 | cexponentiation'''

def p_cexponentiation(t):
	'''cexponentiation  : cprimary
 					| cprimary EXP cexponentiation'''

def p_cprimary(t):
	'''cprimary 	: VAR
 				| LEFT_PAREN cexpression RIGHT_PAREN
 				| unsigned_constant
 				| NOT cprimary'''


#Alguns conjuntos de operacoes--------------------------------------
def p_unsigned_constant(t):
	'''unsigned_constant : INTEGER
					 | REAL
 					 | CHAR
 					 | NIL'''

def p_sign(t):
	'''sign   : ADD_OP
 			| SUB_OP'''

def p_relop(t):
	'''relop : EQUALS
 		    | NOT_EQUAL
 		    | LESS
 		    | GREATER
 		    | LESS_OR_EQUAL
 		    | GREATER_OR_EQUAL
 		    | IN'''

def p_addop(t):
	'''addop  : ADD_OP
 			| SUB_OP
 			| OR'''

def p_mulop(t):
	'''mulop  : MUL_OP
 			| DIV_OP
 			| DIV
			| MOD
 			| AND'''

#Caso haja erro
def p_error(t):
	print "Syntax error in input!"

yacc.yacc()

while 1:

	try:
		s = raw_input('enter > ')
	except EOFError:
		break
	if not s:
		continue
	yacc.parse(s)



