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
#Correspondencia entre argumentos
#Erro float

return_counter = 0
var_counter = 0
block_flag = False
main_flag = False
MAIN_BLOCK = ""
ACT_BLOCK = ""

def generate(node):
	global block_flag,main_flag,MAIN_BLOCK,ACT_BLOCK
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

	elif node.type in ["procedure_and_function_declaration_part"] and not main_flag:
		for child in node.children:
			generate(child)
		main = True
		ACT_BLOCK = MAIN_BLOCK
		print ACT_BLOCK

	elif node.type in ["procedure_and_function_declaration_part"] and main_flag:
		for child in node.children:
			generate(child)
	
	elif node.type in ["procedure_declaration"]:
		if len(node.children[0].children)==1:
			name = generate(node.children[0])
			frames[name] = Frame()
		else:
			name = generate(node.children[0].children[0])
			frames[name] = Frame()
			generate(node.children[0].children[1]) #gerar parametros
				
		translate_proc_1st(name)
		generate(node.children[1])
		translate_proc_2nd(name)

	elif node.type in  ["block","variable_declaration_part","variable_declation_list","compound_statement",
					"statement_sequence","statement","open_statement","closed_statement",
					"program_heading","proc_or_func_declaration_list","proc_or_func_declaration",
					"formal_parameter_list","formal_parameter_section_list"]:
		for child in node.children:
			generate(child)

	elif node.type in [ "unsigned_constant","relop","addop","expression","actual_parameter",
					"params","boolean","procedure_heading"]:
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
				if ACT_BLOCK == MAIN_BLOCK:
					return global_vars[child]
				else:
					if child in frames[ACT_BLOCK].global_vars:
						return frames[ACT_BLOCK].global_vars[child]
					else:
						return global_vars[child]
			else:
				return generate(child)

	elif node.type in [ "identifier_list","type_denoter","actual_parameter_list"]:
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

		if ACT_BLOCK == MAIN_BLOCK:
			f.write("%s = %s;\n" % (global_vars[var],st) )
		else:
			if var in frames[ACT_BLOCK].global_vars:
				f.write("%s = %s;\n" % (frames[ACT_BLOCK].global_vars[var],st) )
			else:
				f.write("%s = %s;\n" % (global_vars[var],st) )

	elif node.type in ["procedure_statement"]: #LAVAGEM AKI
		name = generate(node.children[0])
		
		if len(node.children)!=1:
			params = generate(node.children[1])
		else:
			params = None
	
		if name == "writeln" or name == "write":
			par = params[0][0]
			if par in var_type:
				translate_printf_var(name,dic_type_c[dic_typ[var_type[par]]],par)

			elif ACT_BLOCK != MAIN_BLOCK and par in frames[ACT_BLOCK].var_type:
				translate_printf_var(name,dic_type_c[dic_typ[frames[ACT_BLOCK].var_type[par]]],par)
			
			else:
				translate_printf(name,par)

		else:
			translate_call_stat(name)

	elif node.type in ["simple_expression","term"]:
		if len(node.children) == 1:
			return [generate(node.children[0])]
		else:
			return [generate(node.children[0]), generate(node.children[1]), generate(node.children[2])]

	elif node.type in ["variable_declaration","formal_parameter_section"]:
		var = generate(node.children[0])
		typ = generate(node.children[1])
		if len(var) == len(typ):
			for i in range(len(var)):
				if ACT_BLOCK == MAIN_BLOCK:
					do_main_set_var(var[i],typ[i])
				else:
					do_frame_set_var(var[i],typ[i],dic_typ[typ[i]])			
		else:
			t = typ[0]
			for v in var:
				if ACT_BLOCK == MAIN_BLOCK:
					do_main_set_var(v,t)
				else:
					do_frame_set_var(v,t,dic_typ[t])

def do_main_set_var(v,t):
	w = set_var(v,t)
	f.write("%s %s;\n" % (w[0],w[1]))

def do_frame_set_var(v,t,dt):
	w = frames[ACT_BLOCK].set_var(v,t,dt)
	nt = dic_typ[w[0]]
	f.write( "sp->locals[%s]=(%s*)malloc(sizeof(%s));\n" % (w[1],nt,nt) )

def translate_printf_var(name,typ_par,par):
	if name == "writeln":
		typ_par = "\"" + typ_par + "\\n\""
	else:
		typ_par = "\"" + typ_par + "\""
	f.write("printf(%s, %s);\n" % (typ_par,par) )

def translate_printf(name,par):
	par = par.replace("\'","\"")
	if name == "writeln":
		par = par[:-1]
		par = par + "\\n\""
	f.write("printf(%s);\n" % (par))

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
	translate_redirector()
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
	global return_counter
	f.write(  "goto exit;\n"
			"redirector:\n"
		)

	for i in range(return_counter):
		f.write("if(_ra==%d) goto return%d;\n" % (i,i))
		
	f.write("exit:\n")

def translate_call_stat(name):
	global return_counter
	f.write(  "_ra=%d;\n" % (return_counter) )
	f.write(  "goto %s;\n" % (name) )
	f.write(  "return%d:\n" % (return_counter) )
	return_counter += 1	

