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
    d = {"angle":radians(r.randint(0,360)) % (2*pi), "distance":3 + r.random() % 10, "point":p1}
    p2 = Point.fromMetrics(**d)
    drawables.append(p2)
    """ 
    t = p1.bisect(p2)
    drawables.append(t)
    """
    c1 = Circle.fromMetrics(p1, 5 + r.random() % 12)
    c2 = Circle.fromMetrics(p2, 2 + r.random() % 12)
    drawables.append(c1)
    drawables.append(c2)
    try:
        t = c1.commonChord(c2)
        drawables.append(t)
    except Exception as e:
        print(e)
    Drawable.draw(drawables, f"data/cache{i+1}", _store=True)
r = Random()
r.seed(1)
for i in range(50):
    print(f"Iteration {i}")
    repeater(i, r)
