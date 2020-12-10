import __init__
from json import dumps, loads
file = open("rules/point.json")
s = file.read()
file.close()
a:dict = loads(s)
d = (int, float)
a[d] = "args"
for p,c in a.items():
    print(p,"\t",c)