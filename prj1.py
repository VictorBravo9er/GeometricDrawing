"""prj1.py."""
# from Drawables.Drawable import Drawable, main as load
from Drawables.Drawable import Drawable
from Drawables.Point import Point
import math

p = Point.fromCoOrdinates(1,2)

print(p)

p._rotate(180)
print(p)
p._rotate(180)
print(p)
p._reflectLine(math.inf)

print(p)

p._translate(12,0)

a = p + p
print(a)
print(type(a.X))

