from stack import *
from table import *
from code.proc_and_func import *
	
def add_to_stack(t):
	global table
	stack.add_frame(t)
	table = stack[-1]
	
def display(node):
	if type(node) == type("") or node == None:
		print node
		return
	print node.type
	for child in node.children:
			display(child)

def find(node):
	if node not in key_words: 	
		try:
			stack.find(node)
		except VariableNotDefined, e:
			print e
	return None


def run_tree( node, pf_flag=False):
	if node == None:	return None
	
	if type(node) == type(""):	return find(node.upper())

	if node.type in ['procedure_declaration', 'function_declaration']:
		add_to_stack(Table())
		pf_flag = True

	elif node.type == 'block' and not pf_flag:
		global nm
		add_to_stack(Table(nm))


	if node.type in ['variable_declaration_part','formal_parameter_section_list']:
		for	child in node.children:	
			var_subtree(child)
		if pf_flag and node.type == 'formal_parameter_section_list':	stack.proc_func[-1].copy_params(table.hash)
			
	elif node.type == 'block_name':
		nm = node.children[0]
		
		if pf_flag:
			table.name = nm
			stack.proc_func.append( ProcAndFunc(nm) )
			
	else:
		for child in node.children:	
			block = run_tree(child, pf_flag)
		if node.type == 'block':	stack.pop_frame()



def type_denoter_subtree( node):
	if node == None:		return

	if type(node) == type(""):										
		try:
			table.add_type(node.upper())
		except VariableDeclarationError, e:
			print "Type %s doesn't have a match" %e
		return node

	for child in node.children:		t = type_denoter_subtree(child)
	table.check_queue(t.upper())



def var_subtree(node):
	if node == None:		return

	if type(node) == type(""):
		try:
			table.queue_identifier(node.upper())
		except VariableAlreadyDefined, e:
			print e
		return

	if node.type == 'type_denoter':
		for child in node.children:		type_denoter_subtree(child)
		return

	for child in node.children:		var_subtree(child)




table = None
key_words = ['WRITELN', 'WRITE', 'READLN', 'READ']
nm = ''

stack = Stack()


