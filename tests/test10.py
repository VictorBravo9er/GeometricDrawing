import __init__
import math
from math import degrees, radians, sqrt
from Drawables.Point import Point
from Drawables.Line import  Line

o = Point()
print(o)

a = Point.fromCoOrdinates(1,0)
print(a)
l = o.lineToPoint(a)

b = Point.fromCoOrdinates(3,1)
print(b)
t = b.triangleTo(l)
print(t)

c = o.circleAroundRadius(20)

print(c)