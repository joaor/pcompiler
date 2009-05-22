class VariableNotDefined(Exception):
	def __init__(self, var):
		self.content = "VARIABLE_NOT_DEFINED: %s" %var

	def __str__(self):
		return self.content		

