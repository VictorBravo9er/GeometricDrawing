from math import pi
from Drawables.Point import Point
from Drawables.Line import Line
from figures.base import base
from Drawables.Drawable import Drawable as dw
i = 1000
"""a = base.modify(i)
dw.draw(
    drawables=a
)"""

a = Line.fromPoints(
    Point.fromCoOrdinates(0,0)
    , Point.fromCoOrdinates(0,2)
)
print(a)
print(base.centre)

a._reflectPoint(
    base.centre
)

print(a)
dw.draw([a])