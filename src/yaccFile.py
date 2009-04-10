from ply import yacc
from lexFile import tokens

#Estrutura do programa e o seu bloco de codigo---------------------------------
def p_program(t):
	#program a;  .
	'program : program_heading SEMICOLON block DOT'

def p_block(t):
	'block : constant_definition_part variable_declaration_part procedure_and_function_declaration_part compound_statement'


#Declaracao do heading do programa------------------------------------------------
def p_program_heading(t):
	'''program_heading : PROGRAM IDENTIFIER
				    | PROGRAM IDENTIFIER LEFT_PAREN identifier_list RIGHT_PAREN'''

def p_identifier_list(t):
	'''identifier_list : identifier_list COMMA IDENTIFIER
				    | IDENTIFIER'''

#Declaracao de constantes----------------------------------------------------------
def p_constant_definition_part(t):
	'''constant_definition_part : CONST constant_list
							| '''

def p_constant_list(t):
	'''constant_list 	: constant_list constant_definition
 					| constant_definition'''

def p_constant_definition(t):
	'constant_definition : IDENTIFIER EQUALS cexpression SEMICOLON'

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
	'''cprimary 	: IDENTIFIER
 				| LEFT_PAREN cexpression RIGHT_PAREN
 				| unsigned_constant
 				| NOT cprimary'''

#Declaracao de variaveis----------------------------------------------------
def p_variable_declaration_part(t):
	'''variable_declaration_part 	: VAR variable_declaration_list SEMICOLON
							|'''

def p_variable_declaration_list(t):
	'''variable_declaration_list 	: variable_declaration_list SEMICOLON variable_declaration
 							| variable_declaration'''

def p_variable_declaration(t):
	'variable_declaration : identifier_list COLON type_denoter'

def p_type_denoter(t):
	'''type_denoter 	: IDENTIFIER
 					| LEFT_PAREN identifier_list RIGHT_PAREN'''

#Declaracao de procedimentos e funcoes--------------------------------------
def p_procedure_and_function_declaration_part(t):
	'''procedure_and_function_declaration_part : proc_or_func_declaration_list SEMICOLON
									   |'''

def p_proc_or_func_declaration_list(t):
	'''proc_or_func_declaration_list 	: proc_or_func_declaration_list SEMICOLON proc_or_func_declaration
 								| proc_or_func_declaration'''

def p_proc_or_func_declaration(t):
	'''proc_or_func_declaration 	: procedure_declaration
 							| function_declaration'''


#Declaracao de procedimentos-------------------------------------------
def p_procedure_declaration(t):
	#procedure a; ;
	'''procedure_declaration : PROCEDURE IDENTIFIER SEMICOLON block
						| procedure_heading SEMICOLON block'''

def p_procedure_heading(t):
	#procedure a(c,v : real); ;
	'''procedure_heading 	: PROCEDURE IDENTIFIER formal_parameter_list'''


#Declaracao de funcoes---------------------------------------------------------
def p_function_declaration(t):
	#funcao a;  ;-> nao devolve nada
	'''function_declaration 	: FUNCTION IDENTIFIER SEMICOLON block
 						| function_heading SEMICOLON block'''

def p_function_heading(t):
	#funcao a: real;  ; -> devolve real
	#funcao b(a,b : real ; VAR g:integer ) : real;  ;  -> devolve real, mas tem argumentos
	'''function_heading 	: FUNCTION IDENTIFIER COLON IDENTIFIER 
	 					| FUNCTION IDENTIFIER formal_parameter_list COLON IDENTIFIER'''


#Corpo das funcoes e procedimentos------------------------------------------------------
def p_formal_parameter_list(t):
	'formal_parameter_list : LEFT_PAREN formal_parameter_section_list RIGHT_PAREN'

def p_formal_parameter_section_list(t):
	'''formal_parameter_section_list 	: formal_parameter_section_list SEMICOLON formal_parameter_section
 								| formal_parameter_section'''

def p_formal_parameter_section(t):
	'''formal_parameter_section 	: identifier_list COLON IDENTIFIER
 							| VAR identifier_list COLON IDENTIFIER
 							| procedure_heading
 							| function_heading'''

#Statements----------------------------------------------------------------------------------
def p_compound_statement(t):
	'compound_statement : BEGIN statement_sequence END'

def p_statement_sequence(t):
	'''statement_sequence 	: statement_sequence SEMICOLON statement
 						| statement'''

def p_statement(t):
	'''statement 	: open_statement
 				| closed_statement'''

def p_closed_statement(t):
	'''closed_statement : assignment_statement
 					| procedure_statement
 					| compound_statement
 					| repeat_statement
 					| closed_if_statement
 					| closed_while_statement
 					| closed_for_statement
 					| '''

def p_open_statement(t):
	'''open_statement 	: open_if_statement
 					| open_while_statement
 					| open_for_statement'''

#While dentro do for -> program a; begin for count:=1 downto 100 do begin while a<6 do count:=count+1; end; end.

#REPEAT e WHILE---------------------------------------------------------------------------------- 
#program a(d,c); var a:integer; begin a:=1; repeat a:=a+1; until a=6; end.
def p_repeat_statement(t):
	'repeat_statement : REPEAT statement_sequence UNTIL expression'

#program a; begin a:=5; while a<6 do a:=a+1; end.
#program a; begin a:=5; while a<6 do begin a:=a+1; end; end.
def p_open_while_statement(t):
	'open_while_statement : WHILE expression DO open_statement'

def p_closed_while_statement(t):
	'closed_while_statement : WHILE expression DO closed_statement'

#FOR----------------------------------------------------------------------------------------------------
#program a; var sum:integer; begin sum:=0; for count:=1 to 100 do sum:=sum + count; end.
def p_open_for_statement(t):
	'open_for_statement : FOR IDENTIFIER DECLARATOR expression direction expression DO open_statement'

def p_closed_for_statement(t):
	'closed_for_statement : FOR IDENTIFIER DECLARATOR expression direction expression DO closed_statement'

def p_direction(t):
	'''direction 	: TO
 				| DOWNTO'''

#IF e atribuicao de valores a variaveis-----------------------------------------------------------------------
# program a; begin a:=0; b:=1; if a=b then begin a:=1 end; end.
def p_open_if_statement(t):
	'''open_if_statement 	: IF expression THEN statement
 						| IF expression THEN closed_statement ELSE open_statement'''

def p_closed_if_statement(t):
	'closed_if_statement : IF expression THEN closed_statement ELSE closed_statement'

def p_assignment_statement(t):
	'assignment_statement : IDENTIFIER DECLARATOR expression'

#chamada de procedimentos----------------------------------------------------------------------------
#program a; begin a(d); end.
def p_procedure_statement(t):
	'''procedure_statement 	: IDENTIFIER params
 						| IDENTIFIER'''

def p_params(t):
	'params : LEFT_PAREN actual_parameter_list RIGHT_PAREN'

def p_actual_parameter_list(t):
	'''actual_parameter_list : actual_parameter_list COMMA actual_parameter
 						| actual_parameter'''

def p_actual_parameter(t):
	'''actual_parameter : expression
 					| expression COLON expression
 					| expression COLON expression COLON expression'''

#expressoes legais nos statements--------------------------------------------------------------------
def p_expression(t):
	'''expression 	: simple_expression
 				| simple_expression relop simple_expression'''

def p_simple_expression(t):
	'''simple_expression 	: term
 						| simple_expression addop term'''

def p_term(t):
	'''term 	: factor
 			| term mulop factor'''

def p_factor(t):
	'''factor 	: sign factor
 				| exponentiation'''

def p_exponentiation(t):
	'''exponentiation 	: primary
 					| primary EXP exponentiation'''

def p_primary(t):
	'''primary 	: IDENTIFIER
 				| unsigned_constant
 				| function_designator
 				| LEFT_PAREN expression RIGHT_PAREN
 				| NOT primary'''

def p_function_designator(t):   #functions with no params will be handled by plain identifier
	'function_designator : IDENTIFIER params'



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



