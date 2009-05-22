class VariableAlreadyDefined(Exception):
	def __init__(self, var):
		self.content = "VARIABLE_ALREADY_DEFINED: %s" %var

	def __str__(self):
		return self.content		

