import __init__
import __init__
import math
from math import degrees, radians, sqrt
from Drawables.Point import Point
from Drawables.Line import  Line

c = Point()
a = Point.fromPoint(c)
a._translate(1,4)
print(a)
b = Point.fromPoint(a)
b._translate(22,-11)
print(b)
c._translate(3,0)
print(c,end="\n\n")

l = Line.fromPoints(a,c)
print(b)
print(l,l.getMetrics(), end="\n\n")
b._reflectLine(l)
print(b)
