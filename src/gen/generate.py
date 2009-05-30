f = open("gen/c_code/output.c",'w')
dic_typ = {"integer":"int","real":"float","string":"char*"}

def generate(node):
	if node == None:
		return None

	elif type(node) == type("") or type(node) == type(1):
		#print "retornei "+ str(node) 
		return node

	elif node.type in ["program"]:
		translate_header()
		for child in node.children:
			generate(child)
		translate_footer()
		f.close()
#"block","variable_declaration_part","variable_declation_list","compound_statement",
#					"statement_sequence","statement","open_statement","closed_statement","expression",
#					"unsigned_constant","relop","addop","mulop","sign"
#"identifier_list","type_denoter","simple_expression","term","factor","exponentiation",
#					"primary"

	elif node.type in  ["block","variable_declaration_part","variable_declation_list","compound_statement",
					"statement_sequence","statement","open_statement","closed_statement"]:
		for child in node.children:
			generate(child)

	elif node.type in ["primary","unsigned_constant","relop","addop","mulop","expression"]:
		for child in node.children:
			return generate(child)


	elif node.type in ["identifier_list","type_denoter"]:
		l = []
		for child in node.children:
			r = generate(child)
			if type(r) == type(""):
				l.append(r)
			else:
				l = l + r
		return l

	elif node.type in ["assignment_statement"]:
		var = generate(node.children[0])
		print var +"olaaaaaaaaaaa"
		assg = generate(node.children[1])
		print "Assgmt:"
		print assg

	elif node.type in ["simple_expression","term"]:
		if len(node.children) == 1:
			#print "AKIII"
			assg = generate(node.children[0])
			#print "ola "+str(assg)
			return assg
		else:
			assg = [generate(node.children[0]), generate(node.children[1]), generate(node.children[2])]
			return assg

	elif node.type in ["variable_declaration"]:
		var = generate(node.children[0])
		typ = generate(node.children[1])
		#print var
		#print typ
		if len(var) == len(typ):
			for i in range(len(var)):
				f.write("%s %s;\n" % (dic_typ[typ[i]],var[i]))
		else:
			t = dic_typ[typ[0]]
			for v in var:
				f.write("%s %s;\n" % (t,v))

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
