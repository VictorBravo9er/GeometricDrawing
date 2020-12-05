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
l1 = Line.fromPoints(p1,p2)
drawables.append(l1)
dist = 1
l2 = l1.fromPoints(p3,p4)
print(l1)
print(l2)
drawables.append(l2)
y = l2.bisector()
x = l1.intersectionWith(l2)
drawables.append(x)
drawables.append(y)
dist2 = l1.distanceFrom(l2)
assert y.distanceTo(p3) == y.distanceTo(p4)

Drawable.draw(drawables)

