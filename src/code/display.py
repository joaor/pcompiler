from stack import *

class Display():
	def __init__(self):
		self.stack = Stack()
		
	def add_to_stack(self):
		self.stack.add_frame(Table())
		self.table = self.stack[-1][1]


	def display(self, node):
		if type(node) == type("") or node == None:
			#print node
			return

		#print node.type
		if node.type == 'block':
			self.add_to_stack()
			
		if node.type == 'formal_parameter_section_list':
			for	child in node.children:
				self.var_subtree(child)
			
		elif node.type in 'variable_declaration_part':
			for	child in node.children:
				self.var_subtree(child)

		else:
			for child in node.children:
				self.display(child)


	def type_denoter_subtree(self, node, n=0):
		if node == None:		return

		if type(node) == type(""):
			if n:								self.table.add_type(node.upper())
			else:								self.table.add_type_to_ids(node.upper())
			return

		for child in node.children:
			self.type_denoter_subtree(child,1)



	def var_subtree(self, node):
		if node == None:		return

		if type(node) == type(""):
			try:
				self.table.queue_identifier(node.lower())
			except VariableAlreadyDefined, e:
				print e
			return

		if node.type == 'type_denoter':
			for child in node.children:
				self.type_denoter_subtree(child)
			return

		for child in node.children:
			self.var_subtree(child)


