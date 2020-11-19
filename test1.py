from Drawables.Point import Point
from Drawables.Line import  Line

p = Point.fromCoOrdinates(1,1)
a = Point.fromCoOrdinates(0,1)
b = Point.fromCoOrdinates(1,0)
k = Point.fromMetrics(180,10, p)
print(p)
print(k)
print()
o = Point()
l = Line.fromMetrics(135, 3, o)

print(p)
print(l)

d = o.distanceTo(l)
print(d)

l2 = Line.fromPoints(a,b)
print(o,a,b,l2)
d = o.distanceTo(l2)
print(d)
