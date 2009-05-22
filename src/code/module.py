from stack import *
from table import *
from code.proc_and_func import *
from excep.wrong_number_of_arguments import *
from excep.different_types_in_assignment import *

key_words = ['WRITELN', 'WRITE', 'READLN', 'READ']


def display(node):
	if type(node) == type("") or node == None:
		print node
		return
	print node.type
	for child in node.children:
			display(child)


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
			print e
	 


