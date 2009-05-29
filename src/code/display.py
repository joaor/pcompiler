from module import *

def go_children(children,f, *args):
	for child in children:
		r = f(child, *args)
	return r



def run_tree( node, in_function=False):
	if node == None:	return None
	if type(node) == type(""):	
		return find_var(node.upper(), stack)

	if node.type in ['procedure_declaration', 'function_declaration']:
		global table
		table = add_to_stack(Table(), stack)
		in_function = True

	elif node.type == 'block' and not in_function:
		global nm, table
		table = add_to_stack(Table(nm), stack)


	if node.type in ['variable_declaration_part','formal_parameter_section_list']:
		go_children(node.children, var_subtree)
		if in_function and node.type == 'formal_parameter_section_list':
			stack.proc_func[-1].copy_params(table.hash)
			
	elif node.type == 'block_name':
		nm = node.children[0].upper()
		if in_function:
			table.name = nm
			stack.proc_func.append( ProcAndFunc(nm) )
			
	elif node.type == 'function_returning':
		stack.get_pf().set_returning(node.children[0].upper())
			
	elif node.type in ['procedure_statement', 'function_designator']:
		function_designator(node, stack)
			
	elif node.type == 'assignment_statement':
		try:
			assignment_validation(node, find_var(node.children[0], stack))		
		except DifferentTypesInAssignment, e:
			print e
	
	else:
		go_children(node.children, run_tree, in_function)
		if node.type == 'block':	
			stack.pop_frame()
			#table = stack.stack[-1]




def type_denoter_subtree( node):
	if node == None:		return
	if type(node) == type(""):										
		table.add_type(node.upper())
		return node

	go_children(node.children, type_denoter_subtree)
	#table.check_queue( go_children(node.children, type_denoter_subtree).upper())



def var_subtree(node):
	if node == None:		return
	if type(node) == type(""):
		try:
			table.add_var(node.upper())
		except VariableAlreadyDefined, e:
			print e
		return

	if node.type == 'type_denoter':
		go_children(node.children, type_denoter_subtree)
		try:
			table.check_queue()
		except VariableDeclarationError, e:
			print e
		table.clean()
	else:
		go_children(node.children, var_subtree)


def params_subtree(node):
	list=[]
	if node == None: return
	if type(node) == type(""):
		f= find_var(node, stack)
		if f: return [f]
			
	else:		
		for child in node.children:
			p = params_subtree(child)
			if p: list.extend(p)
			
	return list
	


def function_designator(node, stack):
	try:
		return function_calling(node, stack)
	except WrongNumberOfArguments, e:	print e
	except FunctionOrProcedureNotDefined, e: print e


def function_calling(node, stack):
	name = node.children[0].upper()
	pf = find_pf(name, stack)
	
	if not pf:	return
	if len(node.children)>1:
	
		types = params_subtree(node.children[1])
		if len(types) != len(pf.params):
			raise WrongNumberOfArguments(name, len(pf.params), len(types))
			
		try:	
			pf.check_params(types)
		except ArgumentTypeIncompatibility, e:
			print e

		return pf.r_type
	else:
		raise WrongNumberOfArguments(name, len(pf.params), 0)



def assignment_validation(node, assignment_type=None, t=None):
	if node==None or assignment_type==None: return
	if type(node) == type(''):
		t=find_var(node.upper(), stack)
		if t==None: return
	
	elif node.type == 'function_designator':
		t = function_designator(node, stack)
		
	if t:
		if t != assignment_type:
			raise DifferentTypesInAssignment(t,assignment_type)
	else:
		go_children(node.children, assignment_validation, assignment_type)
			
			
			

table = None
nm = ''
stack = Stack()

