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
			EXCEPTIONS.add(e)
		
		return

	elif node.type == 'block':
		global nm, table
		table = add_to_stack(Table(nm), stack)

	if node.type == 'variable_declaration_part':
		go_children(node.children, var_subtree)
			
	elif node.type == 'block_name':
		nm = node.children[0].upper()
			
	elif node.type in ['procedure_statement', 'function_designator']:
		function_designator(node)
			
	elif node.type == 'assignment_statement':
		try:
			assignment_validator(node, find_var(node.children[0], stack))		
		except DifferentTypesInAssignment, e:
			EXCEPTIONS.add(e)
	
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
			EXCEPTIONS.add(e)
		return node

	go_children(node.children, type_denoter_subtree)
	#table.check_queue( go_children(node.children, type_denoter_subtree).upper())



def var_subtree(node):
	if node == None:		return
	if type(node) == type(""):
		try:
			table.add_var(node.upper()) #procura local (permite same name que um var global)
		except VariableAlreadyDefined, e:
			EXCEPTIONS.add(e)
		return

	if node.type == 'type_denoter':
		go_children(node.children, type_denoter_subtree)
		try:
			table.check_queue()
		except VariableDeclarationError, e:
			EXCEPTIONS.add(e)
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
			EXCEPTIONS.add(e)
			return False
	
	elif node.type == 'block':
		go_children(node.children, run_tree)
	
	elif node.type == 'function_returning':
		#stack.get_pf().set_returning(node.children[0].upper())
		type = node.children[0].upper()
		stack.get_pf().r_type = type
		table.set_var(table.name, type) 
	
	elif node.type == 'variable_declaration_part':	
		go_children(node.children, var_subtree)
		
	elif node.type == 'formal_parameter_section_list':
		go_children(node.children, var_subtree)
		stack.proc_func[-1].copy_params(table.list)
	
	else:
		r = go_children(node.children, pf_subtree)
		return r



def params_subtree(node):
	list=[]
	if node == None: return
	if type(node) == type(""):
		arr = ["'",'"']
		if node[0] in arr and node[-1] in arr:
			return ['STRING']
			
		var= find_var(node, stack)
		if var: 
			return [var.type]
	
	elif type(node) == type(1):
		return ['INTEGER']

	elif type(node) == type(1.1):
		return ['REAL']
	
	elif node.type == 'boolean':
		return ['BOOLEAN'] 
	
	else:		
		for child in node.children:
			p = params_subtree(child)
			if p: list.extend(p)
			
	return list
	


def function_designator(node, f=True):
	try:
		return function_calling(node, f)
	except WrongNumberOfArguments, e:	EXCEPTIONS.add(e)
	except FunctionOrProcedureNotDefined, e: EXCEPTIONS.add(e)


def function_calling(node, flag):
	if flag:
		name = node.children[0]
		l = len(node.children)
	else:
		name = node
		l = 0
		
	pf = find_pf(name, stack)
	if pf == None:	return
	
	###########################
	for i in pf.not_init:
		var = find_var(i.var, stack)
		if var and var.value:
			EXCEPTIONS.remove(i)
			pf.not_init.remove(i)
	
	if l>1:
	
		types = params_subtree(node.children[1])
		if len(types) != len(pf.params):
			raise WrongNumberOfArguments(name, len(pf.params), len(types))
			
		try:	
			pf.check_params(types)
		except ArgumentTypeIncompatibility, e:
			EXCEPTIONS.add(e)

	else:
		if len(pf.params)!=0:
			raise WrongNumberOfArguments(name, len(pf.params), 0)
			
	return pf.r_type


def assignment_validator(node, var):
	if not var:	return
	try:
		go_children(node.children[1:], assignment_validation, var.type)
		stack.set_value_on_var(var.name,True)
	except VariableNotAssigned, e:
		EXCEPTIONS.add(e)
		if stack.proc_func and table.name==stack.proc_func[-1].name:
			stack.proc_func[-1].add_ex(e)


def assignment_validation(node, assignment_type=None, v=None):
	if node==None or assignment_type==None: return
	
	if type(node) == type(''):
		if len(node)==3 and node[0]==node[2]=="'":
			v = Var(node,'CHAR',True)
		
		else:
			v = find_var(node, stack)
			if v==None:
				t = function_designator(node, False)
				if t: 
					v = Var(node, t, True)
					EXCEPTIONS.pop()
				else: return
			
	
	elif type(node) == type(1):
		v = Var(str(node),'INTEGER',True)

	elif type(node) == type(1.1):
		v = Var(str(node),'REAL',True)
	
	elif node.type == 'boolean':
		v = Var(str(node),'BOOLEAN',True)
	
	elif node.type == 'function_designator':
		v = Var(str(node),function_designator(node),True)

	if v:
		if v.type != assignment_type:
			raise DifferentTypesInAssignment(v.type,assignment_type)
		if not v.value:			
			raise VariableNotAssigned(node.upper(), v.type, table.name)
	else:
		go_children(node.children, assignment_validation, assignment_type)
			
			
			

table = None
nm = ''
stack = Stack()

