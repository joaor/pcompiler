from excep.variable_already_defined import *
from excep.variable_declaration_error import *
from excep.variable_not_defined import *

class Stack():
	def __init__(self):
		self.stack = []


	def add_frame(self, frame):
		self.stack.append(frame)

	
	#find local
	def find(self, identifier, d):
		for i in range(len(self.stack)-1,-1,-1):
			if self.stack[i].depth == d:

				if self.stack[i].find(identifier):
					return True
			break
		raise VariableNotDefined(identifier)
		
	
	def length(self):
		return len(self.stack)
		
	def __getitem__(self, p):
		return self.stack[p]

	def display(self):
		for frame in self.stack:
			print frame.name, frame.hash, frame.depth
				


