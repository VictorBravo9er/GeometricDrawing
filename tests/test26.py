import __init__
from Drawables.Circle import Circle
from math import degrees, pi, radians
from Drawables.Drawable import Drawable
import math
from random import Random
from Drawables.Point import Point
from Drawables.Line import  Line
from Drawables.Triangle import Triangle

drawables = []

p1 = Point.fromCoOrdinates(0,0)
drawables.append(p1)
p2 = Point.fromCoOrdinates(0,2)
p3 = Point.fromCoOrdinates(1,4)
p4 = Point.fromCoOrdinates(1,1)

c1 = Circle.fromMetrics(p1, 2)
drawables.append(c1)

c =     c1.tangentAt(p2)
drawables.append(c)

c=    c1.tangentAt(p3)
drawables.append(c)
c=    c1.tangentAt(p4)
drawables.append(c)
c=    c1.tangentAt(angle=pi)
drawables.append(c)
print(type(c))



Drawable.draw(drawables)

