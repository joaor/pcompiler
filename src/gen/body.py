def translate():
	f = open("c_code/output.c",'w')
	translate_header(f)
	translate_footer(f)
	f.close()

def translate_header(f):
	f.write(  "#include \"frame.h\"\n"
			"#include <stdlib.h>\n"
			"#include <stdio.h>\n\n"
			"int main()\n{\n"
			"frame* sp=NULL;\n"
		)

def translate_footer(f):
	f.write("\n}\n\n")

if __name__=="__main__":
	translate()

