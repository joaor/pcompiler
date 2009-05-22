class WrongNumberOfArguments(Exception):
	def __init__(self, f, a, b):
		self.content = "WRONG_NUMBER_OF_ARGUMENTS: %s takes exactly %d arguments (%d given) " %(f,a,b)

	def __str__(self):
		return self.content		

