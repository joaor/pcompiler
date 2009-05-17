class VariableAlreadyDefined(Exception):
	def __init__(self, var):
		self.content = "variable %s already defined in frame" %var

	def __str__(self):
		return self.content		

