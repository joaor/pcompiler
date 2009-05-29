class TypeUnknow(Exception):
	def __init__(self, t):
		self.content = "TYPE_UNKNOW: %s" %t

	def __str__(self):
		return self.content		

