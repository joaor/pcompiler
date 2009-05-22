from excep.variable_already_defined import *
from excep.variable_declaration_error import *
from excep.variable_not_defined import *
from excep.function_or_procedure_not_defined import *

class Stack():
	def __init__(self):
		self.stack = []
		self.proc_func = []

	def add_frame(self, frame):
		self.stack.append(frame)

	def find_var(self, identifier):
		for i in range(len(self.stack)-1,-1,-1):
			type = self.stack[i].find(identifier)
			if type: 
				return type
				
		if self.proc_func[-1].name == identifier:
			return self.proc_func[-1].r_type
			
		raise VariableNotDefined(identifier)
		
	def find_pf(self, name):
		for i in self.proc_func:
			if i.name == name:
				return i
		raise FunctionOrProcedureNotDefined(name)
		
	
	def length(self):
		return len(self.stack)
		
	def __getitem__(self, p):
		return self.stack[p]

	def display(self):
		for frame in self.stack:
			print frame.name, frame.hash
			
	def pop_frame(self):
		self.stack.pop()
		
	def get_pf(self):
		return self.proc_func[-1]


