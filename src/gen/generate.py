f = open("gen/c_code/output.c",'w')
dic_typ = {"integer":"int","real":"float","string":"char*"}
dic_trans = {"mod":"%","div":"//"}

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
		assg = generate(node.children[1])

		st = " ".join( get_list(assg) )
		for i in dic_trans:
			st = st.replace(i,dic_trans[i])
		f.write("%s = %s;\n" % (var,st) )	

	elif node.type in ["procedure_statement"]:
		name = generate(node.children[0])
		params = generate(node.children[1])
		#TODO chamada de funcoes
		print name + "OLA"	
	

	elif node.type in ["simple_expression","term"]:
		if len(node.children) == 1:
			assg = [generate(node.children[0])]
		else:
			assg = [generate(node.children[0]), generate(node.children[1]), generate(node.children[2])]
		return assg

	elif node.type in ["variable_declaration"]:
		var = generate(node.children[0])
		typ = generate(node.children[1])
		if len(var) == len(typ):
			for i in range(len(var)):
				f.write("%s %s;\n" % (dic_typ[typ[i]],var[i]))
		else:
			t = dic_typ[typ[0]]
			for v in var:
				f.write("%s %s;\n" % (t,v))

def get_list(lis):
	a = []
	for i in lis:
		if type(i) == type([]):
			a = a + get_list(i)
		else:
			a.append(str(i))
	return a




def translate_header():
	f.write(  "#include \"frame.h\"\n"
			"#include <stdlib.h>\n"
			"#include <stdio.h>\n\n"
			"int main()\n{\n"
			"frame* fp=NULL;\n"
			"frame* sp=NULL;\n"
		)

def translate_footer():
	f.write(  "return 0\n"
			"}\n\n"
		)






