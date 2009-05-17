from code.display import *
from lib.get_program import get_program
from parser.yaccFile import *


s = get_program()

yacc.yacc()
run_tree(yacc.parse(s))
#display(yacc.parse(s))

print stack.length()
print stack.display()
