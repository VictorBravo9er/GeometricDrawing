from time import sleep
import __init__
from Parser.parse import Parser


p = Parser()
p.tokenChecker("inp.file")

li, fi = p.draw(_show=True ,_store=False)

p.print()