from excep.variable_already_defined import *
from excep.variable_declaration_error import *
from excep.variable_not_defined import *
from excep.type_unknow import *

class Table():
	def __init__(self, nm=None):
		self.hash = {}
		self.name = nm
		self.listv = []
		self.listt = []

	def add_var(self,id):
		if id not in self.listv and id not in self.hash:
			self.listv.append(id)
		else:
			raise VariableAlreadyDefined(id)


	def add_type(self, type):
		if type in ['REAL', 'INTEGER', 'STRING']:
			self.listt.append(type)
		else:
			raise TypeUnknow(type)
		

	def find(self, identifier):
		if identifier in self.hash:
			return self.hash[identifier]
			
	def clean(self):
		self.listv = []
		self.listt = []
		
			
	def check_queue(self):
		lt = len(self.listt)
		lv = len(self.listv)
		if lv == lt:
			for i in range(lt):
				self.hash[self.listv[i]] = self.listt[i]
			
		elif lt==1:
			for i in self.listv:
				self.hash[i] = self.listt[0]
				
		else:
			raise VariableDeclarationError(lv, lt)
				
		

