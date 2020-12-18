import __init__
from Drawables.Drawable import Drawable
from Drawables.Polygon import Polygon
from Drawables.Triangle import Triangle
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
m1 = p1.middlePoint(p2)
m2 = p1.middlePoint(p3)
m3 = p2.middlePoint(p3)
l1 = Line.fromPoints(m1, p3)
l2 = Line.fromPoints(p1, m3)
l3 = Line.fromPoints(m2, p2)
l1.__extend = 1.0
l2.extend(extension=(0,0))
l1.extend(extension=(1,1))
l3.extend(extension=(1,1))

drawables.append(l1)
drawables.append(l2)
drawables.append(l3)


t = Polygon.fromPoints([p3,p2,p1])
t2 = Polygon.fromPoints([p2, p3, p1])
drawables.append(t)
print(degrees(t.internAngle(idx=0)))
print(degrees(t.internAngle(point=p2)))
print(degrees(t.internAngle(idx=2)))

c = t.centroid()
drawables.append(c)
t = Triangle.fromTriangle(t)
print(t.signedArea(), t2.signedArea())
print(t)
print(t2)
print(l1.__extend)
print()
print(round(Triangle.area(t), ndigits=3), Polygon.area(t), type(t))
Drawable.draw(drawables)
