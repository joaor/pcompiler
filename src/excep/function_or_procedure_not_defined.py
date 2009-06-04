class FunctionOrProcedureNotDefined(Exception):
	def __init__(self, id, f):
		self.content = "FUNCTION_OR_PROCEDURE_NOT_DEFINED: %s [%s]" %(id,f)

	def __str__(self):
		return self.content		

