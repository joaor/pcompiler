class ArgumentTypeIncompatibility(Exception):
	def __init__(self, arg, type):
		self.content = "Type of argument #%d must be %s" %(arg,type)

	def __str__(self):
		return self.content		

