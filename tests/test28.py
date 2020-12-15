import __init__
from Drawables.Drawable import Drawable
from Drawables.Point import Point
from Drawables.Arc import  Arc
from math import pi

drawables = []

p1 = Point.fromCoOrdinates(1, 1)
drawables.append(p1)
p2 = Point.fromCoOrdinates(0, 2)
drawables.append(p2)
p3 = Point.fromCoOrdinates(0, 2)
drawables.append(p3)

c = Arc.formArc(centre=p2, radius=3, startAngle=2, endAngle=0)
drawables.append(c)

c2 = Arc.copy(c)
print(c2.centre)
c2._rotate(p1, pi)
drawables.append(c2)

p3._rotate(p1, pi)

print(c2.centre)

Drawable.draw(drawables)

