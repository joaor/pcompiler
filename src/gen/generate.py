f = open("gen/c_code/output.c",'w')
dic_typ = {"integer":"int","real":"float","string":"char*"}
dic_type_c = {"int":"%d","float":"%f","char*":"%c"}
dic_trans = {"mod":"%","div":"//"}
global_vars = {}

var_counter = 0

#TODO: palavras reservadas, a:=false, linha da sempre 1
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

	elif node.type in [ "primary","unsigned_constant","relop","addop","mulop","expression","actual_parameter",
					"params"]:
		for child in node.children:
			return generate(child)


	elif node.type in ["identifier_list","type_denoter","actual_parameter_list"]:
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

		for i in global_vars:
			st = st.replace(i,global_vars[i][1])

		f.write("%s = %s;\n" % (global_vars[var][1],st) )	

	elif node.type in ["procedure_statement"]:
		name = generate(node.children[0])
		params = generate(node.children[1])
	
		if name == "writeln" or name == "write":
			par = params[0][0]
			if par in global_vars:
				par1 = dic_type_c[global_vars[str(par)][0]]
				if name == "writeln":
					par1 = "\"" + par1 + "\\n\""
				else:
					par1 = "\"" + par1 + "\""
				f.write("printf(%s, %s);\n" % (par1 ,global_vars[str(par)][1]))
			else:
				par = par.replace("\'","\"")
				if name == "writeln":
					par = par[:-1]
					par = par + "\\n\""
				f.write("printf(%s);\n" % (par))
		else:
			#TODO Outras funcoes; podem nao ter parametros!
			pass

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
				t = dic_typ[typ[i]]
				v = set_var(var[i],t)
				f.write( "%s %s;\n" % (t,v) )
				
		else:
			t = dic_typ[typ[0]]
			for v in var:
				v1 = set_var(v,t)
				f.write("%s %s;\n" % (t,v1))

def set_var(v,t):
	global var_counter
	global_vars[v] = (t,"g"+str(var_counter))
	var_counter += 1
	return global_vars[v][1]

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
	f.write(  "return 0;\n"
			"}\n\n"
		)






