class Table():
	def __init__(self):
		self.hash = {}
		self.list = []

	def queue_identifier(self,id):
		self.list.append(id)


	def add_type_to_ids(self,type):
		for i in self.list:
			self.hash[i] = type
		self.list = []


	def add_type(self, type):
		self.hash[self.list.pop(0)] = type


	def find(self, identifier):
		if identifier in self.hash:
			return type
		else:
			return None





class Stack():
	def __init__(self):
		self.n = 0
		self.stack = []


	def add_frame(self, frame):
		self.stack.push([self.n, frame])
		self.n += 1


	def search(identifier):
		for i in range(len(self.stack)-1,-1,-1):
			t = self.stack[i].find(identifier)
			if t:	return t
		return None


