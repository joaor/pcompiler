class ProcAndFunc():
	def __init__(self, nm):
		self.name = nm
		self.params = []
		
	def add_param(self,name,type):
		if name not in self.params:
			self.params.append( (name,type))
		else:
			print "parametro repetido"
			#to do raise exception
			
	def copy_params(self, hash):
		for i in hash:
			self.add_param(i, hash[i])
		
		
		
	def check_params(self, types):
		if len(types) != len(self.params):
			return False
			#to do raise exception 'numero de parametros errados'
		
		else:
			for i in range(len(types)):
				if types[i] != self.params[i][1]:
					return False
					#to do raise exception 'tipos incorrectos'
			return True
			
			
	def __str__(self):
		stri = ''
		for i in self.params:
			stri += str(i)
			
		return stri