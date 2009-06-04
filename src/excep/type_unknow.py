class TypeUnknow(Exception):
	def __init__(self, t,f):
		self.content = "TYPE_UNKNOW: %s [%s]" %(t,f)

	def __str__(self):
		return self.content		

