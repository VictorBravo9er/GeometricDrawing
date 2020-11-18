import math
from math import degrees, sqrt
from Drawables.Point import Point
from Drawables.Line import  Line

c = Point()
a = Point.fromMetrics(math.radians(90), sqrt(2), c)
print(a)
b = Point.fromPoint(a)
b._translate(2,0)
print(b)

m = c.angleFromPoints(a,b)
print(degrees(m))
m = a.angleTo(a)
print(m)
b._scale(0.5,1)
print(b)