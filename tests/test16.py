import __init__
from Drawables.Drawable import Drawable
import math
from Drawables.Point import Point
from Drawables.Line import  Line
drawables = []

p1 = Point.fromCoOrdinates(0,0)
drawables.append(p1)
p2 = Point.fromMetrics(45, 2, p1)
drawables.append(p2)

p3 = Point.fromMetrics(-45, 2, p2)
drawables.append(p3)
p4 = Point.fromCoOrdinates(0,1)
drawables.append(p4)


l = Point.bisector(p1,p2)
drawables.append(l)

p = l.sector(1.2)
drawables.append(p)
l1 = Line.fromPoints(p,p1)
l2 = Line.fromPoints(p,p2)
drawables.append(l1)
drawables.append(l2)
assert abs(l1.length() - l2.length()) < 0.00001

Drawable.draw(drawables)
