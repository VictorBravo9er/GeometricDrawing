import __init__
from Drawables.Point import Point
from Drawables.Drawable import Drawable
from math import inf, pi
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1)
a = Drawable()

r = a.reftectionMatrix(inf, 2)

print(r)

arr = np.reshape((1,2,1), (3,1))
print(arr)

x = np.dot(r,arr)

print(x)
print()
a = Point.angleFromPoints
print(a)
b = Point.__mro__
p1 = Point.fromCoOrdinates(0,0)
p2 = Point.fromMetrics(45, 2, p1)
p3 = Point.fromMetrics(-45, 2, p2)

c = a(p1,p2,p3)

print(c)

print(b)

