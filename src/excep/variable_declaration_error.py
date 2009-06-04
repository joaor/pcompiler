class VariableDeclarationError(Exception):
	def __init__(self, v,t,f):
		self.content = "VARIABLE_DECLARATION_ERROR: given %d types to %d variables [%s]" %(t,v,f)

	def __str__(self):
		return self.content		

