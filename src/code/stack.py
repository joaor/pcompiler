from excep.variable_already_defined import *
from excep.variable_declaration_error import *

class Table():
	def __init__(self):
		self.hash = {}
		self.list = []

	def queue_identifier(self,id):
		if id not in self.list and id not in self.hash:
			self.list.append(id)
		else:
			raise VariableAlreadyDefined(id)

	def add_type_to_ids(self,type):
		for i in self.list:
			self.hash[i] = type
		self.list = []


	def add_type(self, type):
		if self.list != []:
			self.hash[self.list.pop(0)] = type
		else:
			raise VariableDeclarationError(type)


	def find(self, identifier):
		if identifier in self.hash:
			return type
		else:
			return None
			
	def check_queue(self, type):
		self.add_type_to_ids(type)





class Stack():
	def __init__(self):
		self.n = 0
		self.stack = []


	def add_frame(self, frame):
		self.stack.append([self.n, frame])
		self.n += 1
		#print 'foi.m adicionado nova frame'


	def search(self,identifier):
		for i in range(len(self.stack)-1,-1,-1):
			t = self.stack[i].find(identifier)
			if t:	return t
		return None
		
	
	def length(self):
		return len(self.stack)
		
	def __getitem__(self, p):
		return self.stack[p]

	def display(self):
		for frame in self.stack:
			print frame[0], frame[1].hash
				


