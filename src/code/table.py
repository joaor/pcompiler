from excep.variable_already_defined import *
from excep.variable_declaration_error import *
from excep.variable_not_defined import *
from excep.type_unknow import *
from code.var import *

class Table():
	def __init__(self, nm=None):
		self.list = []
		self.name = nm
		self.listv = []
		self.listt = []


	def set_var(self, n, t):
		self.list.append(Var(n, t))


	def add_var(self,id):
		if id not in self.listv and not self.find(id):
			self.listv.append(id)
		else:
			raise VariableAlreadyDefined(id)


	def add_type(self, type):
		if type in ['REAL', 'INTEGER', 'CHAR', 'BOOLEAN']:
			self.listt.append(type)
		else:
			raise TypeUnknow(type)
		

	def find(self, identifier):
		for var in self.list:
			if var.name == identifier:
				return var

			
	def clean(self):
		self.listv = []
		self.listt = []
		
			
	def check_queue(self):
		lt = len(self.listt)
		lv = len(self.listv)
		if lv == lt:
			for i in range(lt):
				self.list.append( Var(self.listv[i],self.listt[i]))
			
		elif lt==1:
			for i in self.listv:
				self.list.append( Var(i,self.listt[0]))
				
		else:
			raise VariableDeclarationError(lv, lt)
				
		

