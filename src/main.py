from code.display import *
from lib.get_program import get_program
from parser.yaccFile import *
from gen.generate import *


s = get_program()

yacc.yacc()
t = yacc.parse(s)
run_tree(t)
#display(t)
print EXCEPTIONS
if not EXCEPTIONS.list:
	#print 'generation'
	generate(t)


#print 'number of func/proc:', len(stack.proc_func)
#for i in stack.proc_func:	print i.name,i,i.r_type

