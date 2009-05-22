class ArgumentTypeIncompatibility(Exception):
	def __init__(self, arg, type):
		self.content = "ARGUMENT_TYPE_INCOMPATIBILITY: Type of argument #%d must be %s" %(arg,type)

	def __str__(self):
		return self.content		

