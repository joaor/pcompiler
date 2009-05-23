def translate():
	f = open("c_code/output.c",'w')
	translate_header(f)
	translate_global_list(f)
	translate_block_list(f)
	translate_footer(f)
	f.close()

def translate_header(f):
	f.write(  "#include \"frame.h\"\n"
			"#include <stdlib.h>\n"
			"#include <stdio.h>\n\n"
			"int main()\n{\n"
			"frame* sp=NULL;\n"
		)

def translate_global_list(f):
	#TODO 
	#1- Criar um offset para cada variavel global
	#2- Percorrer todas as variaveis globais
	#3- Consoante o tipo de variavel:
	'''f.write("VAR_TYPE g%d;\n", offset)''' 
	pass
		
def translate_block_list(f):
	#TODO
	#1- Para cada bloco de codigo (frame), verifica se e main ou proc/func
	#Se main:
	'''f.write(  "\n/*BLOCO MAIN */\n"
			"sp=(frame*)malloc(sizeof(frame));\n"
			"\n/*vardecs*/\n"
		)
	declare_local_vars(f)
	f.write("\n/*statements*/\n")
	translate_statements(f)'''
	#Se proc/func:
	'''pass'''
	pass
	
def declare_local_vars(f):
	#TODO
	#1- Percorrer todas as variaveis locais
	#2- Consoante o tipo de variavel:
	'''f.write("sp->locals[%d]=(VAR_TYPE*)malloc(sizeof(VAR_TYPE));\n")'''
	pass

def translate_statements(f):
	#TODO
	#1- Verificar se e do tipo write, assigment ou call 
	#Se write:
	#Verificar se e local ou global
	#Se global
	'''f.write(\"%%VAR_TYPE\\n\", g%d);\n", t->offset)'''
	#Se local
	'''f.write("printf(\"%%VAR_TYPE\\n\", *((VAR_TYPE*)(sp->locals[%d])));\n", t->offset)'''
	#Se assigment:
	#Verificar se e local ou global
	#Se global
	'''f.write("g%d=%VAR_TYPE;\n", t->offset, value)'''
	#Se local
	'''f.write("*((VAR_TYPE*)sp->locals[%d])=%VAR_TYPE;\n", t->offset, value)'''
	#Se call: 
	'''pass'''
	pass

def translate_footer(f):
	f.write("\n}\n\n")

if __name__=="__main__":
	translate()

