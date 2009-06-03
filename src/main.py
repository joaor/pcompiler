from code.display import *
from lib.get_program import get_program
from parser.yaccFile import *
from gen.generate import *


s = get_program()

yacc.yacc()
t = yacc.parse(s)
run_tree(t)
#display(t)
#generate(t)
#print stack.length()
print '##################################################'
print EXCEPTIONS
print '##################################################'
print '-----------------'
print stack.display()
print '-----------------'
print 'number of func/proc:', len(stack.proc_func)
for i in stack.proc_func:	print i.name,i,i.r_type

