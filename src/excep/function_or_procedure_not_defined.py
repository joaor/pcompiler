class FunctionOrProcedureNotDefined(Exception):
	def __init__(self, id):
		self.content = "FUNCTION_OR_PROCEDURE_NOT_DEFINED: %s" %id

	def __str__(self):
		return self.content		

