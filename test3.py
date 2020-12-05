import math
from Drawables.Point import Point
from Drawables.Line import  Line

p1 = Point.fromCoOrdinates(0,0)

p2 = Point.fromMetrics(45, 2, p1)

p3 = Point.fromMetrics(45, -2, p2)

print(p1, "\n", p2, "\n", p3, "\n")
"""
print(p1.slopeTo(p2))
print(p1.angleTo(p2))
print(p2.angleTo(p1))
print()
"""
p4 = Point.fromCoOrdinates(0.000000000000000000000000000000000000001,2000000000000000000000000000000000000000000)
m = p1.slopeTo(p4)
a = p1.angleTo(p4)
print(m,a)