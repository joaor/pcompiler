class VariableDeclarationError(Exception):
	def __init__(self, v,t):
		self.content = "VARIABLE_DECLARATION_ERROR: given %d types to %d variables" %(t,v)

	def __str__(self):
		return self.content		

