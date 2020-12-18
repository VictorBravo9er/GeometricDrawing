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

p3 = Point.fromMetrics(45, -2, p2)
drawables.append(p3)
l1 = Line.fromPoints(p1,p2)
drawables.append(l1)
dist = 1
l2 = l1.parallelLine(dist)
print(l1)
print(l2)
drawables.append(l2)
assert abs(l1.slope() - l2.slope()) < Drawable.comparisonLimit
dist2 = l1.distanceFrom(line=l2)
print(dist2)
assert abs(dist2 - dist) < Drawable.comparisonLimit

Drawable.draw(drawables)

