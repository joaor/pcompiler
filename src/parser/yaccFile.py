from ply import yacc
from lexFile import tokens
from lib.ast import *

#Estrutura do programa e o seu bloco de codigo---------------------------------
def p_program(t):
	#program a;  .
	'program : program_heading SEMICOLON block DOT'
	t[0] = AST("program", [t[1],t[3]] )


def p_block(t):
	'block : variable_declaration_part procedure_and_function_declaration_part compound_statement'
	t[0] = AST("block", [t[1],t[2],t[3]] )
	
#auxiliar para conseguir distinguir nomes de programa, funcao e procedimentos
def p_block_name(t):
	'block_name : IDENTIFIER'
	
	t[0] = AST("block_name", [t[1]])


#Declaracao do heading do programa------------------------------------------------
def p_program_heading(t):
	'''program_heading : PROGRAM block_name
				    | PROGRAM block_name LEFT_PAREN identifier_list RIGHT_PAREN'''
	if len(t)==3:	
		t[0] = AST("program_heading", [t[2]] )
	else:
		t[0] = AST("program_heading", [t[2],t[4]] )


def p_identifier_list(t):
	'''identifier_list : identifier_list COMMA IDENTIFIER
				    | IDENTIFIER'''
	if len(t)==2:
		t[0] = AST("identifier_list", [t[1]] )
	else:
		t[0] = AST("identifier_list", [t[1],t[3]] )

#Declaracao de variaveis----------------------------------------------------
def p_variable_declaration_part(t):
	'''variable_declaration_part 	: VAR variable_declaration_list SEMICOLON
							|'''
	if len(t)==4:
		t[0] = AST("variable_declaration_part", [t[2]] )

def p_variable_declaration_list(t):
	'''variable_declaration_list 	: variable_declaration_list SEMICOLON variable_declaration
 							| variable_declaration'''
	if len(t)==2:
		t[0] = AST("variable_declation_list", [t[1]] )
	else:
		t[0] = AST("variable_declation_list", [t[1],t[3]] )

def p_variable_declaration(t):
	'variable_declaration : identifier_list COLON type_denoter'
	t[0] = AST("variable_declaration", [t[1],t[3]] )

def p_type_denoter(t):
	'''type_denoter 	: IDENTIFIER
 					| LEFT_PAREN identifier_list RIGHT_PAREN'''
	if len(t)==2:
		t[0] = AST("type_denoter", [t[1]] )
	else:
		t[0] = AST("type_denoter", [t[2]] )

#Declaracao de procedimentos e funcoes--------------------------------------
def p_procedure_and_function_declaration_part(t):
	'''procedure_and_function_declaration_part : proc_or_func_declaration_list SEMICOLON
									   |'''
	if len(t)==3:
		t[0] = AST("procedure_and_function_declaration_part", [t[1]] )

def p_proc_or_func_declaration_list(t):
	'''proc_or_func_declaration_list 	: proc_or_func_declaration_list SEMICOLON proc_or_func_declaration
 								| proc_or_func_declaration'''
	if len(t)==2:
		t[0] = AST("proc_or_func_declaration_list", [t[1]] )
	else:
		t[0] = AST("proc_or_func_declaration_list", [t[1],t[3]] )
	

def p_proc_or_func_declaration(t):
	'''proc_or_func_declaration 	: procedure_declaration
 							| function_declaration'''
	t[0] = AST("proc_or_func_declaration", [t[1]] )


#Declaracao de procedimentos-------------------------------------------
def p_procedure_declaration(t):
	#procedure a; ;
	'''procedure_declaration : PROCEDURE block_name SEMICOLON block
						| procedure_heading SEMICOLON block'''
	if len(t)==5:
		t[0] = AST("procedure_declaration", [t[2],t[4]] )
	else:
		t[0] = AST("procedure_declaration", [t[1],t[3]] )

def p_procedure_heading(t):
	#procedure a(c,v : real); ;
	'''procedure_heading 	: PROCEDURE block_name formal_parameter_list'''
	t[0] = AST("procedure_heading", [t[2],t[3]] )


#Declaracao de funcoes---------------------------------------------------------
def p_function_declaration(t):
	#funcao a;  ;-> nao devolve nada -> foi apagada
	'''function_declaration 	: function_heading SEMICOLON block'''
	if len(t)==5:
		t[0] = AST("function_declaration", [t[2],t[4]] )
	else:
		t[0] = AST("function_declaration", [t[1],t[3]] )

def p_function_heading(t):
	#funcao a: real;  ; -> devolve real 
	#funcao b(a,b : real ; VAR g:integer ) : real;  ;  -> devolve real, mas tem argumentos
	'''function_heading 	: FUNCTION block_name COLON function_returning 
	 					| FUNCTION block_name formal_parameter_list COLON function_returning'''
	if len(t)==5:
		t[0] = AST("function_heading", [t[2],t[4]] )
	else:
		t[0] = AST("function_heading", [t[2],t[3],t[5]] )
		
def p_function_returning(t):
	'function_returning : IDENTIFIER'
	t[0] = AST("function_returning", [t[1]])

#Corpo das funcoes e procedimentos------------------------------------------------------
def p_formal_parameter_list(t):
	'formal_parameter_list : LEFT_PAREN formal_parameter_section_list RIGHT_PAREN'
	t[0] = AST("formal_parameter_list", [t[2]] )

def p_formal_parameter_section_list(t):
	'''formal_parameter_section_list 	: formal_parameter_section_list SEMICOLON formal_parameter_section
 								| formal_parameter_section'''
	if len(t)==2:
		t[0] = AST("formal_parameter_section_list", [t[1]] )
	else:
		t[0] = AST("formal_parameter_section_list", [t[1],t[3]] )

def p_formal_parameter_section(t):
	'''formal_parameter_section 	: identifier_list COLON type_denoter
 							| VAR identifier_list COLON type_denoter
 							| procedure_heading
 							| function_heading'''
	if len(t)==2:
		t[0] = AST("formal_parameter_section", [t[1]] )
	elif len(t)==4:
		t[0] = AST("formal_parameter_section", [t[1],t[3]] )
	else:
		t[0] = AST("formal_parameter_section", [t[1],t[2],t[4]] )

#Statements----------------------------------------------------------------------------------
def p_compound_statement(t):
	'compound_statement : BEGIN statement_sequence END'
	t[0] = AST("compound_statement", [t[2]] )

def p_statement_sequence(t):
	'''statement_sequence 	: statement_sequence SEMICOLON statement
 						| statement'''
	if len(t)==2:
		t[0] = AST("statement_sequence", [t[1]] )
	else:
		t[0] = AST("statement_sequence", [t[1],t[3]] )

def p_statement(t):
	'''statement 	: open_statement
 				| closed_statement'''
	t[0] = AST("statement", [t[1]] )

def p_closed_statement(t):
	'''closed_statement : assignment_statement
 					| procedure_statement
 					| compound_statement
 					| repeat_statement
 					| closed_if_statement
 					| closed_while_statement
 					| closed_for_statement
 					| '''
	if len(t)==2:	
		t[0] = AST("closed_statement", [t[1]] )

def p_open_statement(t):
	'''open_statement 	: open_if_statement
 					| open_while_statement
 					| open_for_statement'''
	t[0] = AST("open_statement", [t[1]] )

#While dentro do for -> program a; begin for count:=1 downto 100 do begin while a<6 do count:=count+1; end; end.

#REPEAT e WHILE---------------------------------------------------------------------------------- 
#program a(d,c); var a:integer; begin a:=1; repeat a:=a+1; until a=6; end.
def p_repeat_statement(t):
	'repeat_statement : REPEAT statement_sequence UNTIL expression'
	t[0] = AST("repeat_statement", [t[2],t[4]] )

#program a; begin a:=5; while a<6 do a:=a+1; end.
#program a; begin a:=5; while a<6 do begin a:=a+1; end; end.
def p_open_while_statement(t):
	'open_while_statement : WHILE expression DO open_statement'
	t[0] = AST("open_while_statement", [t[2],t[4]] )

def p_closed_while_statement(t):
	'closed_while_statement : WHILE expression DO closed_statement'
	t[0] = AST("closed_while_statement", [t[2],t[4]] )

#FOR----------------------------------------------------------------------------------------------------
#program a; var sum:integer; begin sum:=0; for count:=1 to 100 do sum:=sum + count; end.
def p_open_for_statement(t):
	'open_for_statement : FOR IDENTIFIER DECLARATOR expression direction expression DO open_statement'
	t[0] = AST("open_for_statement", [t[2],t[4],t[5],t[6],t[8]] )

def p_closed_for_statement(t):
	'closed_for_statement : FOR IDENTIFIER DECLARATOR expression direction expression DO closed_statement'
	t[0] = AST("closed_for_statement", [t[2],t[4],t[5],t[6],t[8]] )

def p_direction(t):
	'''direction 	: TO
 				| DOWNTO'''

#IF e atribuicao de valores a variaveis-----------------------------------------------------------------------
# program a; begin a:=0; b:=1; if a=b then begin a:=1 end; end.
def p_open_if_statement(t):
	'''open_if_statement 	: IF expression THEN statement
 						| IF expression THEN closed_statement ELSE open_statement'''
	if len(t)==5:
		t[0] = AST("open_if_statement", [t[2],t[4]] )
	else:
		t[0] = AST("open_if_statement", [t[2],t[4],t[6]] )

def p_closed_if_statement(t):
	'closed_if_statement : IF expression THEN closed_statement ELSE closed_statement'
	t[0] = AST("closed_if_statement", [t[2],t[4],t[6]] )

def p_assignment_statement(t):
	'assignment_statement : IDENTIFIER DECLARATOR expression'
	t[0] = AST("assignment_statement", [t[1],t[3]] )

#chamada de procedimentos----------------------------------------------------------------------------
#program a; begin a(d); end.
def p_procedure_statement(t):
	'''procedure_statement 	: IDENTIFIER params
 						| IDENTIFIER'''
	if len(t)==2:
		t[0] = AST("procedure_statement", [t[1]] )
	else:
		t[0] = AST("procedure_statement", [t[1],t[2]] )

def p_params(t):
	'params : LEFT_PAREN actual_parameter_list RIGHT_PAREN'
	t[0] = AST("params", [t[2]] )

def p_actual_parameter_list(t):
	'''actual_parameter_list : actual_parameter_list COMMA actual_parameter
 						| actual_parameter'''
	if len(t)==2:
		t[0] = AST("actual_parameter_list", [t[1]] )
	else:
		t[0] = AST("actual_parameter_list", [t[1],t[3]] )

def p_actual_parameter(t):
	'''actual_parameter : expression
 					| expression COLON expression
 					| expression COLON expression COLON expression'''
	if len(t)==2:
		t[0] = AST("actual_parameter", [t[1]] )
	elif len(t)==4:
		t[0] = AST("actual_parameter", [t[1],t[3]] )
	else:
		t[0] = AST("actual_parameter", [t[1],t[3],t[5]] )

#expressoes legais nos statements--------------------------------------------------------------------
def p_expression(t):
	'''expression 	: simple_expression
 				| simple_expression relop simple_expression'''
	if len(t)==2:
		t[0] = AST("expression", [t[1]] )
	else:
		t[0] = AST("expression", [t[1],t[2],t[3]] )

def p_simple_expression(t):
	'''simple_expression 	: term
 						| simple_expression addop term'''
	if len(t)==2:
		t[0] = AST("simple_expression", [t[1]] )
	else:
		t[0] = AST("simple_expression", [t[1],t[2],t[3]] )

def p_term(t):
	'''term 	: primary
 			| term mulop primary'''
	if len(t)==2:
		t[0] = AST("term", [t[1]] )
	else:
		t[0] = AST("term", [t[1],t[2],t[3]] )

def p_primary(t):
	'''primary 	: IDENTIFIER
 				| unsigned_constant
 				| function_designator
 				| LEFT_PAREN expression RIGHT_PAREN
 				| NOT primary'''
	if len(t)==2:
		t[0] = AST("primary", [t[1]] )
	else:
		t[0] = AST("primary", [t[2]] )

def p_function_designator(t):   #functions with no params will be handled by plain identifier
	'function_designator : IDENTIFIER params'
	t[0] = AST("function_designator", [t[1],t[2]] )



#Alguns conjuntos de operacoes--------------------------------------
def p_unsigned_constant(t):
	'''unsigned_constant : INTEGER
					 | REAL
 					 | CHAR
 					 | boolean
					 | STRING'''
	t[0] = AST("unsigned_constant", [t[1]] )

def p_boolean(t):
	'''boolean :   FALSE
				| TRUE'''
	t[0] = AST("boolean", [t[1]] )

def p_relop(t):
	'''relop : EQUALS
 		    | NOT_EQUAL
 		    | LESS
 		    | GREATER
 		    | LESS_OR_EQUAL
 		    | GREATER_OR_EQUAL'''
	t[0] = AST("relop", [t[1]] )

def p_addop(t):
	'''addop  : ADD_OP
 			| SUB_OP
 			| OR'''
	t[0] = AST("addop", [t[1]] )

def p_mulop(t):
	'''mulop  : MUL_OP
 			| DIV_OP
 			| DIV
			| MOD
 			| AND'''
	t[0] = AST("mulop", [t[1]] )

#Caso haja erro
def p_error(t):
	import sys
	print "Syntax error in input, in line %d!" % t.lineno
	sys.exit()
#yacc.parse(s)



