class NameRepeatedInParams(Exception):
	def __init__(self, n,f):
		self.content = "NAME_REPEATED_IN_PARAMS: %s [%s]" %(n,f)

	def __str__(self):
		return self.content		

