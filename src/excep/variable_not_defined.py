class VariableNotDefined(Exception):
	def __init__(self, var,f):
		self.content = "VARIABLE_NOT_DEFINED: %s [%s]" %(var,f)

	def __str__(self):
		return self.content		

