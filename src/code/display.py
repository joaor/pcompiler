from stack import *
	
def add_to_stack( t):
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




def run_tree( node, depth=-1, flag=False):
	if node == None:	return None
	
	if type(node) == type(""):
		if node.upper() not in key_words: 	
			try:
				stack.find(node.upper(), depth)
			except VariableNotDefined, e:
				print e	
		return None


	if node.type in ['procedure_declaration', 'function_declaration']:
		global nm
		depth += 1
		add_to_stack(Table(depth))
		flag = True

	elif node.type == 'block' and not flag:
		global nm
		depth += 1
		add_to_stack(Table(depth, nm))

	if node.type in ['variable_declaration_part','formal_parameter_section_list']:
		for	child in node.children:
			var_subtree(child)
			
	elif node.type == 'block_name':
		nm = node.children[0]
		if flag:
			table.name = nm

	else:
		for child in node.children:
			block = run_tree(child, depth,flag)



def type_denoter_subtree( node):
	if node == None:		return

	if type(node) == type(""):										
		try:
			table.add_type(node.upper())
		except VariableDeclarationError, e:
			print "Type %s doesn't have a match" %e
		return node

	for child in node.children:
		t = type_denoter_subtree(child)
	table.check_queue(t.upper())



def var_subtree( node):
	if node == None:		return

	if type(node) == type(""):
		try:
			table.queue_identifier(node.upper())
		except VariableAlreadyDefined, e:
			print e
		return

	if node.type == 'type_denoter':
		for child in node.children:
			type_denoter_subtree(child)
		return

	for child in node.children:
		var_subtree(child)



pf_flag = False
stack = Stack()
table = None
key_words = ['WRITELN', 'WRITE', 'READLN', 'READ']
nm = ''

