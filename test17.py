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

l1 = Line.fromPoints(p2,p1)
l2 = l1.perpendicularFrom(p3)
l4 = l1.perpendicularAt(1.5)
l3 = l1.perpendicularBisector()
drawables.append(l1)
drawables.append(l2)
drawables.append(l3)
drawables.append(l4)

Drawable.draw(drawables)
