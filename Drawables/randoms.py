"""Module containing frequently of most likely used random generators."""
from random import random
from math import pi
from Drawables.Drawable import Drawable

randomAngleFull = lambda : (1000 * random()) % (2 * pi)
randomAngle180Par = lambda x: x + (1000 * random()) % 3
randomAngle180 = lambda : randomAngle180Par(0.1)
randomAngle90 = lambda : 0.1 + (1000 * random()) % 1.5
randomAngle90plus = lambda : 1.6 + (1000 * random()) % 1.5
randomLengthPar = lambda x: x + (1000 * random()) % (Drawable._maxX - Drawable._minX)
randomPointRangePar = lambda x: randomLengthPar(x)
randomLength = lambda : randomLengthPar(4)
randomRange = lambda x, y: x + (1000 * random()) % y
randomPointRangeX = lambda : randomRange(Drawable._minX, (Drawable._maxX - Drawable._minX))
randomPointRangeY = lambda : randomRange(Drawable._minY, (Drawable._maxY - Drawable._minY))
