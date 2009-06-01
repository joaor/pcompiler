from module import *
from excep.function_or_procedure_already_defined import *

def go_children(children,f, *args):
	for child in children:
		r = f(child, *args)
		if r==False:	break
	return r


def run_tree( node):
	if node == None or type(node) == type(1):	return None
	if type(node) == type(""):	
		return find_var(node.upper(), stack)

	if node.type in ['procedure_declaration', 'function_declaration']:
		global table
		table = add_to_stack(Table(), stack)
		
		try:
			proc_or_func_creation(node)
		except FunctionOrProcedureAlreadyDefined, e:
			print e
		
		return

	elif node.type == 'block':
		global nm, table
		table = add_to_stack(Table(nm), stack)

	if node.type == 'variable_declaration_part':
		go_children(node.children, var_subtree)
			
	elif node.type == 'block_name':
		nm = node.children[0].upper()
			
	elif node.type == 'function_returning':
		stack.get_pf().set_returning(node.children[0].upper())
			
	elif node.type in ['procedure_statement', 'function_designator']:
		function_designator(node, stack)
			
	elif node.type == 'assignment_statement':
		try:
			assignment_validator(node, node.children[0], find_var(node.children[0], stack))		
		except DifferentTypesInAssignment, e:
			print e
	
	else:
		go_children(node.children, run_tree)
		if node.type == 'block':	
			stack.pop_frame()
			#table = stack.stack[-1]




def type_denoter_subtree( node):
	if node == None:		return
	if type(node) == type(""):
		try:										
			table.add_type(node.upper())
		except TypeUnknow, e:
			print e
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



def proc_or_func_creation(node):
	go_children(node.children, pf_subtree)
	stack.pop_frame()

def pf_subtree(node):
	if node.type == 'block_name':
		try:
			nm = node.children[0].upper()
			stack.add_proc_or_func(nm)
			table.name = nm
		except FunctionOrProcedureAlreadyDefined, e:
			print e
			return False
	
	elif node.type == 'block':
		go_children(node.children, run_tree)
	
	elif node.type == 'function_returning':
		stack.get_pf().set_returning(node.children[0].upper())
	
	elif node.type == 'variable_declaration_part':	
		go_children(node.children, var_subtree)
		
	elif node.type == 'formal_parameter_section_list':
		go_children(node.children, var_subtree)
		stack.proc_func[-1].copy_params(table.hash)
	
	else:
		r = go_children(node.children, pf_subtree)
		return r



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
		if len(pf.params)!=0:
			raise WrongNumberOfArguments(name, len(pf.params), 0)
		return pf.r_type


def assignment_validator(node, var, info):
	if not info:	return
		
	#print var, info
	try:
		go_children(node.children[1:], assignment_validation, info[0])
		#assignment_validation(node, info[0])
	except VariableNotAssigned, e:
		print e
		return
	info[1]=True 


def assignment_validation(node, assignment_type=None, t=None):
	if node==None or assignment_type==None: return
	if type(node) == type(''):
		if len(node)==3 and node[0]==node[2]=="'":
			t = ['CHAR',node]
		else:
			t=find_var(node.upper(), stack)
			if t==None: return
	
	elif type(node) == type(1):
		t = ['INTEGER',node]

	elif type(node) == type(1.1):
		t = ['REAL',node]
	
	elif node.type == 'boolean':
		t = ['BOOLEAN',node]	
	
	elif node.type == 'function_designator':
		t = function_designator(node, stack)
		
		
	if t:
		if t[0] != assignment_type:
			raise DifferentTypesInAssignment(t[0],assignment_type)
		if not t[1]:
			raise VariableNotAssigned(node.upper(), t[0])
	else:
		go_children(node.children, assignment_validation, assignment_type)
			
			
			

table = None
nm = ''
stack = Stack()

