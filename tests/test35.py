import __init__
from Drawables.Drawable import Drawable
from Drawables.Trapezoid import Trapezoid
from Drawables.Rhombus import Rhombus
from Drawables.Kite import Kite
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
a = Line.fromPoints(p1 ,p2)

drawables.append(a)
r = Kite.fromMetrics()
drawables.append(r)

Drawable.draw(drawables)
