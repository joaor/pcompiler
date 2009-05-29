#f = open("c_code/output.c",'w')
returncounter = 0

def translate():
	translate_header()
	translate_global_list()
	translate_block_list()
	translate_footer()
	f.close()

def translate_header():
	f.write(  "#include \"frame.h\"\n"
			"#include <stdlib.h>\n"
			"#include <stdio.h>\n\n"
			"int main()\n{\n"
			"int _ra;\n"
			"frame* fp=NULL;\n"
			"frame* sp=NULL;\n"
		)

def translate_global_list():
	#TODO 
	#1- Criar um offset para cada variavel global
	#2- Percorrer todas as variaveis globais
	#3- Consoante o tipo de variavel:
	'''f.write("VAR_TYPE g%d;\n" % offset)''' 
	pass
		
def translate_block_list():
	#TODO
	#1- Para cada bloco de codigo (frame), verifica se e main ou proc/func
	#Se main:
	'''f.write(  "\n/*BLOCO MAIN */\n"
			"sp=(frame*)malloc(sizeof(frame));\n"
			"\n/*vardecs*/\n"
		)
	declare_local_vars()
	f.write("\n/*statements*/\n")
	translate_statements()'''
	#Se proc/func:
	'''translate_procedure()'''
	pass
	
def declare_local_vars():
	#TODO
	#1- Percorrer todas as variaveis locais
	#2- Consoante o tipo de variavel:
	'''f.write("sp->locals[%d]=(VAR_TYPE*)malloc(sizeof(VAR_TYPE));\n")'''
	pass

def translate_statements():
	#TODO
	#1- Verificar se e do tipo write, assigment ou call 
	#Se write:
	#Verificar se e local ou global
	#Se global
	'''f.write(\"%%VAR_TYPE\\n\", g%d);\n" % t->offset)'''
	#Se local
	'''f.write("printf(\"%%VAR_TYPE\\n\", *((VAR_TYPE*)(sp->locals[%d])));\n" % t->offset)'''
	#Se assigment:
	#Verificar se e local ou global
	#Se global
	'''f.write("g%d=%VAR_TYPE;\n" % (t->offset, value))'''
	#Se local
	'''f.write("*((VAR_TYPE*)sp->locals[%d])=%VAR_TYPE;\n" % (t->offset, value))'''
	#Se call: 
	'''translate_call_stat()'''
	pass

def translate_call_stat():
	'''
	f.write("_ra=%d;\n" % returncounter)		#guarda de endereco de retorno
	f.write("goto %s;\n" % ias->proc)			#Salto para codigo do procedimento
	f.write("return%d:\n" % returncounter);		#label de retorno
	returncounter += 1'''	
	pass

def translate_procedure():
	'''
	#localenv= variaveis locais ao proc	

	f.write("\n/*BLOCO DO PROCEDIMENTO %s */\n", ip->name)
	f.write("/*Prologo*/\n")
	f.write("goto %sskip;\n" % ip->name) #nao executar codigo quando o main for corrido da primeira vez		 
	f.write("%s:\n" % ip->name)	
	f.write("fp=sp;\n")				#Guarda do endereco da frame anterior (sp), no frame pointer (fp)
	f.write("sp=(frame*)malloc(sizeof(frame));\n")	#Criacao de uma nova frame
	f.write("sp->parent=fp;\n")			#Guarda do endereco para a frame anterior, na propria frame
	f.write("sp->return_address=_ra;\n")		#Guarda do endereco de retorno na frame
	
	#Corpo do procedimento
	f.write("/*Corpo do procedimento*/\n")
	translate_vardecs(localenv)			
	translate_statements(localenv)		

	#Epilogo
	f.write("/*Epilogo*/\n")
	f.write("_ra=sp->return_address;\n")		#Restauro do valor de retorno
	f.write("sp=sp->parent;\n")			#"pop" da pilha de frames
	f.write("fp=sp->parent;\n")			#actualizacao do registo FP de acordo
	f.write("goto redirector;\n")			#Instrucao especifica para a nossa implementacao em C "restringido"
	f.write("%sskip:\n" % ip->name) 			#label para acesso a instruccao seguinte ao codigo do procedimento
	'''
	pass

def translate_footer():
	translate_redirector()
	f.write("\n}\n\n")

def translate_redirector():
	f.write("/*Redirector*/\n")
	f.write("goto exit;\n")
	f.write("redirector:\n")

	for i in range(returncounter):
		f.write("if(_ra==%d) goto return%d;\n" % (i,i))   #Para cada endereco de retorno, sua label associada
		
	f.write("exit:\n;\n")

if __name__=="__main__":
	translate()

