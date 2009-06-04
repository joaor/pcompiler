class FunctionOrProcedureAlreadyDefined(Exception):
	def __init__(self, id,f):
		self.content = "FUNCTION_OR_PROCEDURE_ALREADY_DEFINED: %s [%s]" %(id,f)

	def __str__(self):
		return self.content		

