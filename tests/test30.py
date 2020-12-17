import __init__
from Drawables.Drawable import Drawable
from Drawables.Polygon import Polygon
from Drawables.Triangle import Triangle
from Drawables.Line import Line
from Drawables.Point import Point
from Drawables.Arc import  Arc
from math import degrees, pi

drawables = []

p1 = Point.fromCoOrdinates(4, -1)
drawables.append(p1)
p2 = Point.fromCoOrdinates(0, 2)
drawables.append(p2)
p3 = Point.fromCoOrdinates(5,5)
drawables.append(p3)

t = Polygon.fromPoints([p1,p2,p3])
drawables.append(t)
c = Polygon.centroid(t)
drawables.append(c)
t._rotate(c, pi)
print(t.signedArea(), t.signedAreaVectorized(), t.area())

assert t.centroidVectorized() == Polygon.centroid(t)
Drawable.draw(drawables)
