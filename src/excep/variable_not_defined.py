class VariableNotDefined(Exception):
	def __init__(self, var):
		self.content = "Variable %s is not yet defined" %var

	def __str__(self):
		return self.content		

