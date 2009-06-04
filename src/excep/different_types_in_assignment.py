class DifferentTypesInAssignment(Exception):
	def __init__(self, a,b,f):
		self.content = "DIFFERENT_TYPES_IN_ASSIGNMENT: %s and %s [%s]" %(a,b,f)

	def __str__(self):
		return self.content		

