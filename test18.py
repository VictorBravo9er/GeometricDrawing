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

t = Triangle.fromPoints([p1,p2,p3])
drawables.append(t)
l = t.medianFromPoint(0)
drawables.append(l)
l2 = t.perpendicularFromPoint(p1)
drawables.append(l2)

t2 = Triangle.fromTriangle(t)
t2._rotate(angle=radians(180))
drawables.append(t2)
Drawable.draw(drawables)

