import __init__
from Drawables.Circle import Circle
from math import degrees, radians
from Drawables.Drawable import Drawable
import math
from Drawables.Point import Point
from Drawables.Line import  Line
from Drawables.Triangle import Triangle
drawables = []

p1 = Point.fromCoOrdinates(0,0)
drawables.append(p1)
d = {"angle":radians(90), "distance":2, "point":p1}
p2 = Point.fromMetrics(**d)
drawables.append(p2)

p3 = Point.fromMetrics(-45, 2, p2)
drawables.append(p3)

p4 = Point.fromCoOrdinates(0,3)

t = Triangle.fromPoints([p1,p2,p3])
drawables.append(t)

p = t.incenter()
drawables.append(p)


d1 = p.distanceSquared(t.vertices[0])
d2 = p.distanceSquared(t.vertices[1])
d3 = p.distanceSquared(t.vertices[2])
c = t.incircle()

drawables.append(c)
c2 = Circle.fromMetrics(p1, p1.distanceTo(p3))
c3 = Circle.fromMetrics(p1, 1)

drawables.append(c2)
drawables.append(c3)
a = p3.bisectAnglePoints(p2, p1)
#ch = c.commonChord(c3)
#drawables.append(ch)

drawables.append(a)

t = a.triangleTo(p1)
drawables.append(t)

Drawable.draw(drawables)