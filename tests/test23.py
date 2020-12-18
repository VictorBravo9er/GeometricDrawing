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
p3 = Point.fromMetrics(-45, 2, p2)
drawables.append(p3)
p4 = Point.fromCoOrdinates(0,3)
drawables.append(p4)

l = Line.fromPoints(p1, p2)
t = l.circleAround()
drawables.append(t)
drawables.append(l)
t = l.circleAround(tangentCentre=p3)
drawables.append(t)
try:
    t = l.circleAround(chordCentre=p4)
    drawables.append(t)
except Exception as e:
    print(e)
t = Line.parallelLine(l, 4)
drawables.append(t)

Drawable.draw(drawables)