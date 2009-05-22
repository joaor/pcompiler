class DifferentTypesInAssignment(Exception):
	def __init__(self, a,b):
		self.content = "DifferenTypesInAssignment: %s and %s" %(a,b)

	def __str__(self):
		return self.content		

