class VariableDeclarationError(Exception):
	def __init__(self, a):
		self.content = "VARIABLE_DECLARATION_ERROR: Type %s doesn't have a match" %a

	def __str__(self):
		return self.content		

