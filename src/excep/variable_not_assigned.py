class VariableNotAssigned(Exception):
	def __init__(self, v,t,f):
		self.var = v
		self.content = "VARIABLE_NOT_ASSIGNED: %s (%s) has no value [%s]" %(v,t,f)

	def __str__(self):
		return self.content		

