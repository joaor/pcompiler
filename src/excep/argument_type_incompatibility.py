class ArgumentTypeIncompatibility(Exception):
	def __init__(self, arg, type, f):
		self.content = "ARGUMENT_TYPE_INCOMPATIBILITY: Type of argument #%d must be %s [%s]" %(arg,type,f)

	def __str__(self):
		return self.content		

