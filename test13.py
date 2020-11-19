from Drawables.Drawable import Drawable
import math
from Drawables.Point import Point
from Drawables.Line import  Line

p1 = Point.fromCoOrdinates(0,0)

p2 = Point.fromMetrics(45, 2, p1)

p3 = Point.fromMetrics(45, -2, p2)

l1 = Line.fromPoints(p1,p2)

dist = 1
l2 = l1.parallelLine(dist)
print(l1, l2)
assert abs(l1.slope() - l2.slope()) < Drawable.comparisonLimit
dist2 = l1.distanceFromLine(l2)
print(dist2)
assert dist2 == dist