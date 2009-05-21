class FunctionOrProcedureNotDefined(Exception):
	def __init__(self, id):
		self.content = "Function or Procedure %s is not yet defined" %id

	def __str__(self):
		return self.content		

