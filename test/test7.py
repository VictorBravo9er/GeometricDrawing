import math
from math import degrees, radians, sqrt
from Drawables.Point import Point
from Drawables.Line import  Line

c = Point()
a = Point.fromPoint(c)
a._translate(-1,4)
print(a)
b = Point.fromPoint(c)
b._translate(4,-3)
print(b)
c._translate(3,0)
print(c,end="\n\n")

l = Line.fromPoints(c,b)
print(l)
l = Line.fromLine(l, -2)
print(l)