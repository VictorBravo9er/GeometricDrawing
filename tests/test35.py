import __init__
import re
from Parser.parse import *
from sys import argv
#tokenChecker("inp.file")
a = argv[1]

a = re.match('^[A-Za-z_]\w*$', a)
print(a)
print(a is None)
