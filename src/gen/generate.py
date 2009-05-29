f = open("gen/c_code/output.c",'w')

def generate(node):
	if node == None:
		return None

	elif type(node) == type(""):
		return node

	elif node.type == "program":
		translate_header()
		for child in node.children:
			generate(child)
		translate_footer()
		f.close()

	elif node.type in ["block","variable_declaration_part","variable_declation_list"]:
		for child in node.children:
			generate(child)
	
	#elif node.type in ["type_denoter"]:
		#print "OOOOOOOOOOOOOOOOOOOO"

	elif node.type in ["identifier_list","type_denoter"]:
		l = []
		for child in node.children:
			r = generate(child)
			if type(r) == type(""):
				l.append(r)
			else:
				l = l + r
		return l

	elif node.type in ["variable_declaration"]:
		var = generate(node.children[0])
		typ = generate(node.children[1])
		print var
		print typ
		if len(var) == len(typ):
			for i in range(len(var)):
				f.write("%s %s;\n" % (typ[i],var[i]))
		else:
			for v in var:
				f.write("%s %s;\n" % (typ[0],v))

def translate_header():
	f.write(  "#include \"frame.h\"\n"
			"#include <stdlib.h>\n"
			"#include <stdio.h>\n\n"
			"int main()\n{\n"
			"int _ra;\n"
			"frame* fp=NULL;\n"
			"frame* sp=NULL;\n"
		)

def translate_footer():
	f.write("\n}\n\n")
