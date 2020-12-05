import math
from math import degrees, radians, sqrt
from Drawables.Point import Point
from Drawables.Line import  Line

c = Point()
a = Point.fromPoint(c)
a._translate(1,4)
print(a)
b = Point.fromPoint(a)
b._translate(2,-1)
print(b)
print(c,end="\n\n")

b._reflectPoint(a)
print(b)
b._reflectPoint(a)

l = Line.fromPoints(b,c)
print(a)
print(l, end="\n\n")
a._reflectLine(l)
print(a)
