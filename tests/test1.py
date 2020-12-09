import __init__
from Drawables.Point import Point
from Drawables.Line import  Line
from math import radians

import matplotlib.pyplot as plt
fg, ax = plt.subplots(1)
ax.set_aspect(1)

p = Point.fromCoOrdinates(1,1)
a = Point.fromCoOrdinates(0,1)
b = Point.fromCoOrdinates(1,0)
k = Point.fromMetrics(radians(180),10, p)
print(p)
print(k)
print()
o = Point()
l = Line.fromMetrics(radians(135), 3, o)

print(p)
print(l)

d = o.distanceTo(l)
print(d)
l3 = Line.fromMetrics(radians(180), 3, p)
l2 = Line.fromPoints(a,b)
print(o,a,b,l2)
d = o.distanceTo(l2)
print(d)


p.draw(ax)
a.draw(ax)
b.draw(ax)
k.draw(ax)
l.draw(ax)
l2.draw(ax)
l3.draw(ax)
plt.show()