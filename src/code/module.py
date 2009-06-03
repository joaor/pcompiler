from stack import *
from table import *
from code.proc_and_func import *
from excep.wrong_number_of_arguments import *
from excep.different_types_in_assignment import *
from excep.variable_not_assigned import *
from excep.exceptions import *

key_words = ['WRITELN', 'WRITE', 'READLN', 'READ', 
						'+', '-', '*', '/', '=','<','>','<>','<=', '>=', 
						'MOD', 'DIV', 'AND', 'OR', 'NOT', 'TO', 'DOWNTO']
						
EXCEPTIONS = Exceptions()


def display(node,i=0):
	if type(node) == type("") or node == None or type(node) == type(1) or type(node) == type(1.4):
		print node,i
		return
	print node.type,i
	for child in node.children:
		display(child,i+1)


def add_to_stack(t, stack):
	stack.add_frame(t)
	return stack[-1]
	
	
def find_var(node, stack):
	if node not in key_words: 	
		try:
			return stack.find_var(node.upper())
		except VariableNotDefined, e:
			print e
	
	
def find_pf(node, stack):
	if node not in key_words:
		try:
			return stack.find_pf(node)
		except FunctionOrProcedureNotDefined, e:
			EXCEPTIONS.add(e)
	 


