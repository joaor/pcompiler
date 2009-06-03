from excep.argument_type_incompatibility import *
from excep.name_repeated_in_params import *


class ProcAndFunc():
	def __init__(self, nm):
		self.name = nm
		self.params = []
		self.r_type =None
		self.not_init=[]
		
	def add_param(self,i):
		for p in self.params:
			if p.name == i.name:
				raise NameRepeatedInParams(i.name)
		self.params.append(i)

			
	def copy_params(self, l):
		for i in l:
			i.value = True
			self.add_param(i)
		
	def check_params(self, types):
		#print types
		#for i in self.params:
		#	print i.name, i.type, i.value
		#print '--------------'
			
		for i in range(len(types)):
			if types[i] != self.params[i].type:
				raise ArgumentTypeIncompatibility(i+1,self.params[i].type,self.name)
		return True
			
			
	def __str__(self, stri = ''):
		for i in self.params: 
			stri += str((i.name,i.type,i.value))
		return stri

	def set_returning(self, t):
		self.t_type = t
		
	def add_ex(self, e):
		self.not_init.append(e)

