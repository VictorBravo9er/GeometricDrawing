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
p2 = Point.fromMetrics(45, 2, p1)
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
c2 = Circle.fromMetrics(p1, 2)
c3 = Circle.fromMetrics(p1, 1)


"""
print(degrees(p1.angleTo(p2)))
print(degrees(p2.angleTo(p1)))
print(degrees(p1.angleTo(p4)))
print(degrees(p4.angleTo(p1)))

print(degrees(p3.angleTo(p2)))
print(degrees(p2.angleTo(p3)))
""" 
"""
print(degrees(p1.angleFromPoints(p3,p2)))
print(degrees(p2.angleFromPoints(p1,p3)))
print(degrees(p3.angleFromPoints(p2,p1)))
"""
drawables.append(c2)
drawables.append(c3)
a = p3.bisectAround(p2, p1)
ch = c.commonChord(c3)
drawables.append(ch)

drawables.append(a)

Drawable.draw(drawables)