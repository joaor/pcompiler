from excep.variable_already_defined import *
from excep.variable_declaration_error import *
from excep.variable_not_defined import *

class Table():
	def __init__(self, d, nm=None):
		self.hash = {}
		self.list = []
		self.depth = d
		self.name = nm

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
		
