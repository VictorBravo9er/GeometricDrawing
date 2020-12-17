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

l1 = Line.fromPoints(p1,p2)

l3 = Line.fromLine(l1)
l2 = Line.fromPoints(p3,p2)
l3._reflectLine(l2)


drawables.append(l3)

drawables.append(l2)
drawables.append(l1)

Drawable.draw(drawables)
