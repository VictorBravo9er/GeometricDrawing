import __init__

from rules.collect import Collector as ctr

adt = ctr()
adt.collect()
file = None
with open("a.txt", "w") as file:
    adt.print(file)

adt.processSuper()

with open("b.txt", "w") as file:
    adt.print(file)
