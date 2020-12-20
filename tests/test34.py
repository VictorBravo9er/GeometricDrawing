import __init__

from Parser.collect import Collector as ctr

adt = ctr()
file = None
with open("a.txt", "w") as file:
    adt.print(file)

adt.processSuper()

with open("b.txt", "w") as file:
    adt.print(file)
