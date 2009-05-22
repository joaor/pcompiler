class ArgumentTypeIncompatibility(Exception):
	def __init__(self, arg, type, f):
		self.content = "ARGUMENT_TYPE_INCOMPATIBILITY: Type of argument #%d in %s must be %s" %(arg,f,type)

	def __str__(self):
		return self.content		

