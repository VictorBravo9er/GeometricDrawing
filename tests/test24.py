import __init__
from Drawables.Circle import Circle
from math import degrees, radians
from Drawables.Drawable import Drawable
import math
from Drawables.Point import Point
from Drawables.Line import  Line
from Drawables.Triangle import Triangle
drawables = []

p1 = Point.fromCoOrdinates(0,0)
drawables.append(p1)
d = {"angle":radians(90), "distance":2, "point":p1}
p2 = Point.fromMetrics(**d)
drawables.append(p2)
t = p1.bisect(p2)
drawables.append(t)

Drawable.draw(drawables)