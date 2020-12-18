import __init__
from Drawables.Drawable import Drawable
from Drawables.Polygon import Polygon
from Drawables.Triangle import Triangle
from Drawables.Line import Line
from Drawables.Point import Point
from Drawables.Arc import  Arc
from math import degrees, pi

drawables = []

p1 = Point.fromCoOrdinates(1, -1)
drawables.append(p1)
p2 = Point.fromCoOrdinates(19, 3)
drawables.append(p2)
p3 = Point.fromCoOrdinates(10,7)
drawables.append(p3)
p4 = Point.fromCoOrdinates(8, 10)
drawables.append(p4)
p5 = Point.fromCoOrdinates(2, 11)
drawables.append(p5)
p6 = Point.fromCoOrdinates(-1,7)
drawables.append(p6)
p7 = Point.fromCoOrdinates(2, -2)
drawables.append(p7)
p8 = Point.fromCoOrdinates(-10, -3)
drawables.append(p8)
p9 = Point.fromCoOrdinates(-4, -7)
drawables.append(p9)
t = Polygon.fromPoints(drawables)
drawables.append(t)
print(t.centroid(), t.vertexCentroid(), Polygon.centroid(t, vectorized=True))
print(t.area(), Polygon.area(t))

Drawable.draw(drawables)
