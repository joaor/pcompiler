from code.display import *
from lib.get_program import get_program
from parser.yaccFile import *


s = get_program()
d = Display()

yacc.yacc()
d.display(yacc.parse(s))

print d.stack.length()
print d.stack.display()
