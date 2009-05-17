class AST:
	def __init__(self,t,c=None):
		self.type = t
		if c:
			self.children = c
		else:
			self.children = [ ]

