import __init__
from Drawables.Circle import Circle
from math import degrees, pi, radians
from Drawables.Drawable import Drawable
import math
from random import Random
from Drawables.Point import Point
from Drawables.Line import  Line
from Drawables.Triangle import Triangle

def repeater(i:int, r:Random):
    drawables = []
    
    p1 = Point.fromCoOrdinates(0,0)
    drawables.append(p1)
    d = {"angle":r.random() % (2*pi), "distance":1 + r.random() % 2, "point":p1}
    p2 = Point.fromMetrics(**d)
    drawables.append(p2)
    """ 
    t = p1.bisect(p2)
    drawables.append(t)
    """
    c1 = Circle.fromMetrics(p1, 4)
    c2 = Circle.fromMetrics(p2, 3)
    drawables.append(c1)
    drawables.append(c2)

    t = c1.commonChord(c2)
    drawables.append(t)

    Drawable.draw(drawables, str(i+1))
r = Random()
r.seed(1)
for i in range(20):
    print(f"Iteration {i}")
    repeater(i, r)
