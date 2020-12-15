import __init__
from Drawables.Drawable import Drawable
from Drawables.Polygon import Polygon
from Drawables.Line import Line
from Drawables.Point import Point
from Drawables.Arc import  Arc
from math import degrees, pi

drawables = []

p1 = Point.fromCoOrdinates(1, 1)
drawables.append(p1)
p2 = Point.fromCoOrdinates(0, 2)
drawables.append(p2)
p3 = Point.fromCoOrdinates(4, 4)
drawables.append(p3)

t = Polygon.fromPoints([p1,p2,p3])

drawables.append(t)
print( t.clockwise)
Drawable.draw(drawables)
