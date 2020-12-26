"""Module containing frequently of most likely used random generators."""
from random import random
from math import pi
from Drawables.Drawable import Drawable

randomAngleFull = lambda : random() % (2 * pi)
randomAngle180Par = lambda x: x + random() % 3
randomAngle180 = lambda : randomAngle180Par(0.1)
randomLengthPar = lambda x: x + random() % (Drawable._maxX - Drawable._minX)
randomPointRangePar = lambda x: randomLengthPar(x)
randomLength = lambda : randomLengthPar(2)
randomRange = lambda x, y: x + random() % y
randomPointRangeX = lambda : randomRange(Drawable._minX * 0.5, Drawable._maxX - Drawable._minX)
randomPointRangeY = lambda : randomRange(Drawable._minY * 0.5, Drawable._maxY - Drawable._minY)
