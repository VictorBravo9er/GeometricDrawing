import __init__
import math
from math import degrees, sqrt
from Drawables.Point import Point
from Drawables.Line import  Line

o = Point()
print(o)

a = Point.fromMetrics(math.radians(90), sqrt(2), o)
print(a)
b = Point.fromPoint(o)
b._translate(2,0)
print(b,end="\n\n")
l = o.bisectAround(a,b)
print(o.angleTo(a), o.angleTo(b),o.angleFromPoints(a,b))
print(l)