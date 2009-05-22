from code.display import *
from lib.get_program import get_program
from parser.yaccFile import *


s = get_program()

yacc.yacc()
run_tree(yacc.parse(s))
#display(yacc.parse(s))
print stack.length()
print stack.display()
print 'number of func/proc:', len(stack.proc_func)
for i in stack.proc_func:	print i,i.r_type
