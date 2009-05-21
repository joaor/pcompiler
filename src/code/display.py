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

def find_var(node):
	if node not in key_words: 	
		try:
			stack.find_var(node)
		except VariableNotDefined, e:
			print e
	return None
	
def find_pf(node):
	if node not in key_words:
		try:
			return stack.find_pf(node)
		except FunctionOrProcedureNotDefined, e:
			print e
	return None
	

def go_children(c,f):
	for i in c:
		r = f(i)
	return r
	
	

def run_tree( node, in_function=False):
	if node == None:	return None
	if type(node) == type(""):	return find_var(node.upper())

	if node.type in ['procedure_declaration', 'function_declaration']:
		add_to_stack(Table())
		in_function = True

	elif node.type == 'block' and not in_function:
		global nm
		add_to_stack(Table(nm))


	if node.type in ['variable_declaration_part','formal_parameter_section_list']:
		go_children(node.children, var_subtree)
		
		if in_function and node.type == 'formal_parameter_section_list':	
			stack.proc_func[-1].copy_params(table.hash)
			
	elif node.type == 'block_name':
		nm = node.children[0].upper()
		
		if in_function:
			table.name = nm
			stack.proc_func.append( ProcAndFunc(nm) )
			
	elif node.type in ['procedure_statement', 'function_designator']:
		function_calling(node)
			
	else:
		for child in node.children:	
			block = run_tree(child, in_function)
		if node.type == 'block':	
			stack.pop_frame()



def type_denoter_subtree( node):
	if node == None:		return
	if type(node) == type(""):										
		try:
			table.add_type(node.upper())
		except VariableDeclarationError, e:
			print "Type %s doesn't have a match" %e
		return node

	table.check_queue( go_children(node.children, type_denoter_subtree).upper())



def var_subtree(node):
	if node == None:		return
	if type(node) == type(""):
		try:
			table.queue_identifier(node.upper())
		except VariableAlreadyDefined, e:
			print e
		return

	if node.type == 'type_denoter':
		go_children(node.children, type_denoter_subtree)
	else:
		go_children(node.children, var_subtree)



def function_calling(node):
	n_args = find_pf(node.children[0].upper())
	
	if n_args:
		print 'lalalalallala',n_args, node.children[0]




table = None
key_words = ['WRITELN', 'WRITE', 'READLN', 'READ']
nm = ''

stack = Stack()


