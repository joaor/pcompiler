from excep.variable_already_defined import *
from excep.variable_declaration_error import *
from excep.variable_not_defined import *

class Stack():
	def __init__(self):
		self.stack = []
		#list of ProcAndFunction()
		self.proc_func = []


	def add_frame(self, frame):
		self.stack.append(frame)

	
	#find local
	def find(self, identifier):
		for i in range(len(self.stack)-1,-1,-1):
			if self.stack[i].find(identifier):
				return True
			
		#ver se e func/proc e se o numero e tipos params coincide
		
		raise VariableNotDefined(identifier)
		
	
	def length(self):
		return len(self.stack)
		
	def __getitem__(self, p):
		return self.stack[p]

	def display(self):
		for frame in self.stack:
			print frame.name, frame.hash
			
	def pop_frame(self):
		self.stack.pop()
				


