class Exceptions():
	def __init__(self, l=[]):
		self.list = l
		
	def add(self, e):
		self.list.append(e)
	
	def find(self, e):
		for i in range(len(self.list)):
			if type(i)==e:
				return i
				
	def remove(self,e):
		self.list.remove(e)
		
	def pop(self):
		if self.list:
			self.list.pop()
	
	
	def __str__(self):
		stri=''
		for e in self.list:
			stri += str(e)+'\n'
		return stri
		
