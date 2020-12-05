import math
from math import degrees, radians, sqrt
from Drawables.Point import Point
from Drawables.Line import  Line

o = Point()
print(o)

a = Point.fromCoOrdinates(1,0)
print(a)
l = o.lineToPoint(a)

print(l)
l._rotate(angle=radians(-90))
print(o,a)
print(l)