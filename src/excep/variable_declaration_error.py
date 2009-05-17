class VariableDeclarationError(Exception):
	def __init__(self, var):
		self.content = var

	def __str__(self):
		return self.content		

