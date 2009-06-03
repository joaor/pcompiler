class VariableNotAssigned(Exception):
	def __init__(self, v,t):
		self.var = v
		self.content = "VARIABLE_NOT_ASSIGNED: %s (%s) has no value" %(v,t)

	def __str__(self):
		return self.content		

