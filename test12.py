import math
from Drawables.Point import Point
from Drawables.Line import  Line

p1 = Point.fromCoOrdinates(0,0)

p2 = Point.fromMetrics(45, 2, p1)

p3 = Point.fromMetrics(45, -2, p2)

l1 = Line.fromPoints(p1,p2)
l2 = Line.fromMetrics(45, 2, p1)

d1 = l1.length()
d2 = l2.length()

print(l1, d1)
print(l2, d1)
assert l1 == l2 and d1 == d2
print("done")

a = b = d1

print(a, b)