import __init__
from Drawables.Circle import Circle
from math import degrees, pi, radians
from Drawables.Drawable import Drawable
import math
from random import Random
from Drawables.Point import Point
from Drawables.Line import  Line
from Drawables.Triangle import Triangle

def repeater(i:float=0):
    drawables = []
    
    p1 = Point.fromCoOrdinates(0,0)
    drawables.append(p1)
    d = {"angle":radians(i), "distance":4, "point":p1}
    p2 = Point.fromMetrics(**d)
    drawables.append(p2)
    c1 = Circle.fromMetrics(p1, 2)
    c2 = Circle.fromMetrics(p2, 2)
    drawables.append(c1)
    drawables.append(c2)
    print(degrees(p1.angleTo(p2)))
    try:
        t = c1.commonChord(c2)
        drawables.append(t)
    except Exception as e:
        print(e)
    Drawable.draw(drawables, str(i+1))
    return drawables[-1]

e = repeater(95 - 180)
print(e)