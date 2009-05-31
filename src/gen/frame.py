from generate import *

class Frame(object):
	def __init__(self):
		self.global_vars = {}
		self.var_type = {}
		self.var_counter = 0

	def set_var(self,v,t):
		next = str(self.var_counter)
		self.global_vars[v] = next
		self.var_type[next] = t
		self.var_counter += 1	
		return (self.var_type[next],next)

