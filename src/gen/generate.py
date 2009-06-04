from frame import *

f = open("gen/c_code/output.c",'w')
dic_typ = {"integer":"int","real":"float","char":"char","boolean":"int"}
dic_type_c = {"int":"%d","float":"%f","char":"%c"}
dic_trans = {"mod":"%","div":"/","=":"==","and":"&&","<>":"!=","or":"||","not":"!"}
global_vars = {} #{'y': 'g0', 'a': 'g2', 'c': 'g4', 'z': 'g1', 'b': 'g3'}
var_type = {} #{'g4': 'integer', 'g3': 'boolean', 'g2': 'char', 'g1': 'real', 'g0': 'real'}
frames = {}

#VARIABLE_NOT_ASSIGNED: C (INTEGER) has no value
#Estamos a ignorar funcoes k nao devolvem nada
#falha kando se chma funcao/proc do estilo ola(2+3,9)
#falha kando se chma funcao/proc do estilo ola(ola(4),9)
#Se der erro de sintax nao fazer geracao de codigo
#yacc: Warning. Token 'CONST' defined, but not used.
#yacc: Warning. Token 'EXP' defined, but not used.
#yacc: Warning. Token 'COMMENT' defined, but not used.
#yacc: Warning. Token 'IN' defined, but not used.
#yacc: Warning. Token 'NIL' defined, but not used.
#yacc: Warning. Token 'BOOLEAN' defined, but not used.
#yacc: Warning. Token 'TYPE' defined, but not used.

return_counter = 0
var_counter = 0
stat_counter = 0
block_flag = False
main_flag = False
MAIN_BLOCK = ""
ACT_BLOCK = ""

def generate(node):
	global block_flag,main_flag,MAIN_BLOCK,ACT_BLOCK,stat_counter
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
			MAIN_BLOCK = b.lower()
			block_flag = True
		ACT_BLOCK = b.lower()
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
	
	elif node.type in ["function_declaration"]:
		name = generate(node.children[0].children[0])
		
		if len(node.children[0].children) ==3:
			retur = generate(node.children[0].children[2]) # return value
		else:
			retur = generate(node.children[0].children[1]) # return value

		frames[name] = Frame(retur.lower())
		translate_proc_1st(name)		
		
		if len(node.children[0].children) ==3:
			par = generate(node.children[0].children[1]) #gerar parametros

		generate(node.children[1]) # corpo da func
		translate_proc_2nd(name)

	elif node.type in ["procedure_declaration"]:
		if len(node.children[0].children)==1:
			name = generate(node.children[0])
		else:
			name = generate(node.children[0].children[0])

		frames[name] = Frame()
		translate_proc_1st(name)

		if len(node.children[0].children)!=1:
			generate(node.children[0].children[1]) #gerar parametros	
		
		generate(node.children[1]) #corpo do proc
		translate_proc_2nd(name)

	elif node.type in  ["block","variable_declaration_part","variable_declation_list","compound_statement",
					"statement_sequence","statement","open_statement","closed_statement",
					"program_heading","proc_or_func_declaration_list","proc_or_func_declaration",
					"formal_parameter_list","formal_parameter_section_list"]:
		for child in node.children:
			generate(child)

	elif node.type in [ "unsigned_constant","actual_parameter","direction",
					"params","boolean","procedure_heading","function_returning"]:
		for child in node.children:
			return generate(child)

	elif node.type in ["closed_if_statement","open_if_statement"]:
		stat_counter += 1
		a = stat_counter
		l = get_list(generate(node.children[0]))
		f.write("if %s goto then%d;\n" % (l,a) )
		if len(node.children) == 3:
			generate(node.children[2])		
		f.write("goto endif%d;\n" % (a) )
		f.write("then%d:\n" % (a) )
		generate(node.children[1])		
		f.write("endif%d:\n" % (a) )

	elif node.type in ["closed_while_statement","open_while_statement"]:
		stat_counter += 1
		a = stat_counter
		l = get_list(generate(node.children[0]))
		f.write("while%d:\n" % (a) )
		f.write("if (!(%s)) goto endwhile%d;\n" % (l,a) )
		generate(node.children[1])
		f.write("goto while%d;\n" % (a) )
		f.write("endwhile%d:\n" % (a) )		

	elif node.type in ["closed_for_statement","open_for_statement"]:
		stat_counter += 1
		a = stat_counter
		v = generate(node.children[0]) #gera assigment
		direction = generate(node.children[1]).lower()
		if direction == 'to':
			signal = '<'
			op = '+'
		else:
			signal = '>'
			op = '-'
		limit = generate(node.children[2])
		f.write("for%d:\n" % (a) )
		f.write("if (!(%s %s= %s)) goto endfor%d;\n" % (v,signal,str(limit[0][0]),a) )
		generate(node.children[3])
		f.write("%s = %s %s 1;\n" % (v,v,op) )
		f.write("goto for%d;\n" % (a) )
		f.write("endfor%d:\n" % (a) )

	elif node.type in ["repeat_statement"]:
		stat_counter += 1
		a = stat_counter
		exp = get_list(generate(node.children[1]))
		f.write("repeat%d:\n" % (a) )
		generate(node.children[0])
		f.write("if %s goto endrepeat%d;\n" % (exp,a) )
		generate(node.children[1])
		f.write("goto repeat%d;\n" % (a) )
		f.write("endrepeat%d:\n" % (a) )

	elif node.type in ["mulop","relop","addop"]:
		st = generate(node.children[0])
		if st in dic_trans:
			st = dic_trans[st]
		return st

	elif node.type in ["primary"]:
		if len(node.children) == 2:
			return [dic_trans[generate(node.children[0])],generate(node.children[1])]
		for child in node.children:
			if type(child) == type(""):
				if child.lower() in frames:
					return (child.lower(),[])
				if ACT_BLOCK == MAIN_BLOCK:
					return global_vars[child]
				else:
					if child in frames[ACT_BLOCK].global_vars:
						return frames[ACT_BLOCK].global_vars[child]
					else:
						return global_vars[child]
			else:
				return generate(child)

	elif node.type in [ "identifier_list","type_denoter","actual_parameter_list","expression"]:
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
		
		if type(assg[0][0]) == type(()):
			translate_call_stat(assg[0][0][0].lower(),assg[0][0][1],var)
		
		else:
			st = get_list(assg)
		
			if var.lower() == ACT_BLOCK:
				rt = dic_typ[frames[ACT_BLOCK].return_typ]
				f.write("sp->parent->return_val[0] = (%s*)malloc(sizeof(%s));\n" % (rt,rt) )
				f.write("*((%s*)sp->parent->return_val[0]) = %s;\n" % (rt,st) )
			elif ACT_BLOCK == MAIN_BLOCK:
				f.write("%s = %s;\n" % (global_vars[var],st) )
				return global_vars[var]
			else:
				if var in frames[ACT_BLOCK].global_vars:
					f.write("%s = %s;\n" % (frames[ACT_BLOCK].global_vars[var],st) )
					return frames[ACT_BLOCK].global_vars[var]
				else:
					f.write("%s = %s;\n" % (global_vars[var],st) )
					return global_vars[var]

	elif node.type in ["procedure_statement","function_designator"]:
		name = generate(node.children[0]).lower()
		
		if len(node.children)!=1:
			params = generate(node.children[1])
		else:
			params = None
	
		if node.type == "function_designator":
			return (name,params)
		if name == "writeln" or name == "write":
			par = params[0][0]
			if par in var_type:
				translate_printf_var(name,dic_type_c[dic_typ[var_type[par]]],par)

			elif ACT_BLOCK != MAIN_BLOCK and par in frames[ACT_BLOCK].var_type:
				translate_printf_var(name,dic_type_c[dic_typ[frames[ACT_BLOCK].var_type[par]]],par)
			
			else:
				translate_printf(name,par)

		else:
			translate_call_stat(name,params)

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
					do_main_set_var(var[i],typ[i].lower())
				else:
					do_frame_set_var(var[i],typ[i].lower(),dic_typ[typ[i].lower()],node.type)			
		else:
			t = typ[0].lower()
			for v in var:
				if ACT_BLOCK == MAIN_BLOCK:
					do_main_set_var(v,t)
				else:
					do_frame_set_var(v,t,dic_typ[t],node.type)

def do_main_set_var(v,t):
	w = set_var(v,t)
	f.write("%s %s;\n" % (w[0],w[1]))

def do_frame_set_var(v,t,dt,node):
	w = frames[ACT_BLOCK].set_var(v,t,dt)	
	if node == "variable_declaration":
		nt = dic_typ[w[0]]
		f.write( "sp->locals[%s]=(%s*)malloc(sizeof(%s));\n" % (w[1],nt,nt) )
	else:
		f.write( "sp->locals[%s]=sp->parent->outgoing[%s];\n" % (w[1],w[1]) )

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

def translate_call_stat(name,par,var=None):
	global return_counter
	if par != None:
		for i in range(len(par)):
			t = None
			act = par[i][0]
			if ACT_BLOCK == MAIN_BLOCK:
				if act in var_type:
					t = dic_typ[var_type[act]]
			else:
				if act in frames[ACT_BLOCK].var_type:
					t = dic_typ[frames[ACT_BLOCK].var_type[act]]
			if t==None:
				t = get_type(act)
			f.write(  "sp->outgoing[%s] = (%s*)malloc(sizeof(%s));\n" % (str(i),t,t) )
			f.write(  "*((%s*)sp->outgoing[%s]) = %s;\n" % (t,str(i),str(act) ) )

	f.write(  "_ra=%d;\n" % (return_counter) )
	f.write(  "goto %s;\n" % (name.lower()) )
	f.write(  "return%d:\n" % (return_counter) )
	if var !=None:
		t = dic_typ[frames[name].return_typ]
		if ACT_BLOCK == MAIN_BLOCK:
			f.write("%s = *((%s*)sp->return_val[0]);\n" % (global_vars[var],t) )
		else:
			if var in frames[ACT_BLOCK].global_vars:
				f.write("%s = *((%s*)sp->return_val[0]);\n" % (frames[ACT_BLOCK].global_vars[var],t) )
			else:
				f.write("%s = *((%s*)sp->return_val[0]);\n" % (global_vars[var],t) )
	return_counter += 1	

def get_type(v):
	if type(v) == type(1):
		return "int"
	elif type(v) == type(1.2):
		return "float"
	elif len(v) == 3:
		return "char"
	else:
		return "int"





