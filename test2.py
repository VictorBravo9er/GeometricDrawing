from Drawables.Point import Point
from Drawables.Line import  Line

p1 = Point.fromCoOrdinates(1,2)

p2 = Point.fromPoint(p1)
p2._translate(2,3)

print(p1, "\n", p2)