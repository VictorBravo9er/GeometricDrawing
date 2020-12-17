import __init__
from Drawables.Drawable import Drawable
from Drawables.Polygon import Polygon
from Drawables.Triangle import Triangle
from Drawables.Line import Line
from Drawables.Point import Point
from Drawables.Arc import  Arc
from math import degrees, pi

drawables = []

p1 = Point.fromCoOrdinates(0, 1)
drawables.append(p1)
p2 = Point.fromCoOrdinates(2, 3)
drawables.append(p2)
p3 = Point.fromCoOrdinates(4,7)
drawables.append(p3)

t = Triangle.fromPoints([p1,p2,p3])
drawables.append(t)
drawables.append(t.vertexCentroid())
print(t.clockwise)

#drawables.append(t.centroidVectorized())
c = t.circumcircle()
#drawables.append(c)
print(t.centroid(), t.vertexCentroid(), Polygon.centroid(t, vectorized=False))
print(t.area(), Polygon.area(t))
a = p1.bisectAnglePoints(p2,p3)
drawables.append(a)
Drawable.draw(drawables)
