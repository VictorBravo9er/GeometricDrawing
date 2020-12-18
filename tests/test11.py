import __init__
import math
from Drawables.Point import Point
from Drawables.Line import  Line

p1 = Point.fromCoOrdinates(0,0)

p2 = Point.fromMetrics(45, 2, p1)

p3 = Point.fromMetrics(-45, 2, p2)

l = Line.fromPoints(p1,p2)

print(p1, p2, p3)

print(l)

perp = p3.perpendicularTo(l)

print(perp)

m1,_ = l.getMetrics()
m2,_ = perp.getMetrics()

assert m1 * m2 == -1
print(f"done {m1*m2}")