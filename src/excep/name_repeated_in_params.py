class NameRepeatedInParams(Exception):
	def __init__(self, n):
		self.content = "NAME_REPEATED_IN_PARAMS: %s" %n

	def __str__(self):
		return self.content		

