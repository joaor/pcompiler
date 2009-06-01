class FunctionOrProcedureAlreadyDefined(Exception):
	def __init__(self, id):
		self.content = "FUNCTION_OR_PROCEDURE_ALREADY_DEFINED: %s" %id

	def __str__(self):
		return self.content		

