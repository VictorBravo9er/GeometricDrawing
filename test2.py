import math
from Drawables.Point import Point
from Drawables.Line import  Line

p1 = Point.fromCoOrdinates(0,0)

p2 = Point.fromPoint(p1)
p2._translate(2,2)

p3 = Point.fromPoint(p1)
p3._translate(0,-2)

print(p1, "\n", p2, "\n", p3, "\n")
"""
print(p1.slopeTo(p2))
print(p1.angleTo(p2))
print(p2.angleTo(p1))
print()
"""
l1 = Line.fromPoints(p2,p3)

dist = p1.angleFromLine(l1)
print(l1)
print(math.degrees(dist),"\n")


print(p1.slopeTo(p3))
print(p3.slopeTo(p1))

p4 = Point.middlePoint(p1, p2)
print(p4)

a = p1.squaredDistance(p2)
b = p1.distanceToPoint(p2)
print(a,b)