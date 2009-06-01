from generate import *

class Frame(object):
	def __init__(self,r=None):
		self.global_vars = {}
		self.var_type = {}
		self.var_counter = 0
		self.return_typ = r

	def set_var(self,v,t,tc):
		next = str(self.var_counter)
		var = "*((%s*)sp->locals[%s])" % (tc,next)
		self.global_vars[v] = var
		self.var_type[var] = t
		self.var_counter += 1	
		return (self.var_type[var],next)

