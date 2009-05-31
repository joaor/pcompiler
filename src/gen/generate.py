from frame import *

f = open("gen/c_code/output.c",'w')
dic_typ = {"integer":"int","real":"float","char":"char","boolean":"int"}
dic_type_c = {"int":"%d","float":"%f","char":"%c"}
dic_trans = {"mod":"%","div":"/"}
global_vars = {} #{'y': 'g0', 'a': 'g2', 'c': 'g4', 'z': 'g1', 'b': 'g3'}
var_type = {} #{'g4': 'integer', 'g3': 'boolean', 'g2': 'char', 'g1': 'real', 'g0': 'real'}
frames = {}
#WRONG_NUMBER_OF_ARGUMENTS: SCOPEINNER takes exactly 0 arguments (0 given) 
#VARIABLE_NOT_ASSIGNED: C (INTEGER) has no value
#Funcoes com o mesmo nome nao da erro

var_counter = 0
block_flag = False
MAIN_BLOCK = ""
ACT_BLOCK = ""

def generate(node):
	global block_flag,MAIN_BLOCK,ACT_BLOCK
	if node == None:
		return None	

	elif type(node) == type(""):
		if node.upper() in ["FALSE","TRUE"]:
			return node.upper()
		else:
			return node

	elif type(node) == type(1) or type(node) == type(1.4): 
		return node

	elif node.type in ["program"]:
		translate_header()
		for child in node.children:
			generate(child)
		translate_footer()
		f.close()
	
	elif node.type in ["block_name"]:
		b = node.children[0]
		if not block_flag:
			MAIN_BLOCK = b
			block_flag = True
		ACT_BLOCK = b
		print ACT_BLOCK
		return ACT_BLOCK

	elif node.type in ["procedure_and_function_declaration_part"]:
		for child in node.children:
			generate(child)

	elif node.type in ["procedure_declaration"]:
		name = generate(node.children[0])
		frames[name] = Frame()
		translate_proc_1st(name)
		generate(node.children[1])
		translate_proc_2nd(name)

	elif node.type in  ["block","variable_declaration_part","variable_declation_list","compound_statement",
					"statement_sequence","statement","open_statement","closed_statement",
					"program_heading","proc_or_func_declaration_list","proc_or_func_declaration"]:
		for child in node.children:
			generate(child)

	elif node.type in [ "unsigned_constant","relop","addop","expression","actual_parameter",
					"params","boolean"]:
		for child in node.children:
			return generate(child)

	elif node.type in ["mulop"]:
		st = generate(node.children[0])
		for i in dic_trans:
			st = st.replace(i,dic_trans[i])
		return st

	elif node.type in ["primary"]:
		for child in node.children:
			if type(child) == type(""):
				for i in global_vars:
					child = child.replace(i,global_vars[i])
				return child
			else:
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
		st = get_list(assg)
		f.write("%s = %s;\n" % (global_vars[var],st) )	

	elif node.type in ["procedure_statement"]:
		name = generate(node.children[0])
		
		if len(node.children)!=1:
			params = generate(node.children[1])
		else:
			params = None
	
		if name == "writeln" or name == "write":
			par = params[0][0]
			if par in var_type:
				par1 = dic_type_c[dic_typ[var_type[par]]]
				if name == "writeln":
					par1 = "\"" + par1 + "\\n\""
				else:
					par1 = "\"" + par1 + "\""
				f.write("printf(%s, %s);\n" % (par1,par) )
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
				if ACT_BLOCK == MAIN_BLOCK:
					w = set_var(var[i],typ[i])
					f.write( "%s %s;\n" % (w[0],w[1]) )
				else:
					w = frames[ACT_BLOCK].set_var(var[i],typ[i])
					nt = dic_typ[w[0]]
					f.write( "sp->locals[%s]=(%s*)malloc(sizeof(%s));\n" % (w[1],nt,nt) )
				
		else:
			t = typ[0]
			for v in var:
				if ACT_BLOCK == MAIN_BLOCK:
					w = set_var(v,t)
					f.write("%s %s;\n" % (w[0],w[1]))
				else:
					w = frames[ACT_BLOCK].set_var(v,t)
					nt = dic_typ[w[0]]
					f.write( "sp->locals[%s]=(%s*)malloc(sizeof(%s));\n" % (w[1],nt,nt) )

def set_var(v,t):
	global var_counter
	next = "g"+str(var_counter)
	global_vars[v] = next
	var_type[next] = t
	var_counter += 1	
	return (dic_typ[var_type[next]],next)

def get_list(lis):
	if type(lis) == type([]):
		return "(%s)" % " ".join([ get_list(i) for i in lis ]) 	
	else:
		return str(lis)




def translate_header():
	f.write(  "#include \"frame.h\"\n"
			"#include <stdlib.h>\n"
			"#include <stdio.h>\n"
			"#define FALSE 0\n"
			"#define TRUE 1\n\n"
			"int main()\n{\n"
			"int _ra;\n"
			"frame* fp=NULL;\n"
			"frame* sp=NULL;\n"
			"sp=(frame*)malloc(sizeof(frame));\n"
		)

def translate_footer():
	f.write(  "return 0;\n"
			"}\n\n"
		)

def translate_proc_1st(name):
	f.write(  "goto %sskip;\n" % (name) )
	f.write(  "%s:\n" % (name) )
	f.write(  "fp=sp;\n"
			"sp=(frame*)malloc(sizeof(frame));\n"
			"sp->parent=fp;\n"
			"sp->return_address=_ra;\n"
		)

def translate_proc_2nd(name):	
	f.write(  "_ra=sp->return_address;\n"
			"sp=sp->parent;\n"
			"fp=sp->parent;\n"
			"goto redirector;\n"
		)
	f.write(  "%sskip:\n" % (name) )

def translate_redirector():
	f.write("/*Redirector*/\n")
	f.write("goto exit;\n")
	f.write("redirector:\n")

	for i in range(returncounter):
		f.write("if(_ra==%d) goto return%d;\n" % (i,i))   #Para cada endereco de retorno, sua label associada
		
	f.write("exit:\n;\n")


