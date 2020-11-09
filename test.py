from math import sqrt
from Drawables.Point import Point
from Drawables.Line import  Line

p = Point.fromCoOrdinates(1,1)

k = Point.fromMetrics(180,10, p)
print(p)
print(k)
print()

l = Line.fromMetrics(135, 3, Point())

print(p)
print(l)

d = p.distanceToLine(l)
print(d)
