"""Module for Point."""
from Drawables.randoms import *
from Drawables.Drawable import Drawable
from Drawables.Quad import Quadrilateral
from math import acos, degrees, pi, radians, sin
import numpy as np

class Kite(Quadrilateral):
    """Base class of kite."""

    _rhombus:str = "rhombus"
    def __init__(self):
        """Class constructor."""
        super().__init__()

    @classmethod
    def fromPoints(cls, listOfPoint: list):
        """Build kite from provided points."""
        if len(listOfPoint) != 4:
            raise ValueError(
                "ValueError:\tThe Polygon can't even be "+
                "constructed as a quadrilateral."
            )
        new = Quadrilateral()
        new.setPolygon(listOfPoint)
        return cls.checkClass(new)

    @classmethod
    def fromLines(cls, listOfLine: list):
        """Build kite from provided lines."""
        points = cls.edgeToVertex(listOfLine)
        return cls.fromPoints(points)

    @classmethod
    def fromKite(cls, kite):
        """Copy from another kite."""
        if isinstance(kite, cls):
            new = type(kite)()
            new.vertices = cls.newVertices(kite.vertices)
            new.size = kite.size
            new.clockwise = kite.clockwise
            return new
        raise TypeError(
            "TypeError:\tExpected Kite, "+
            f"received {type(kite).__name__}"
        )

    @classmethod
    def fromMetrics(
        cls, line=..., angleLine:float=..., lengthOther:float=...,
        angle:float=...
    ):
        """Draws a kite from some metrics: a line(or its length and angle), an internal angle, other length."""
        from Drawables.Line import Line
        from Drawables.Point import Point
        a,b=...,...
        if not isinstance(angle, (float, int)):
            angle = randomAngle90()
        if isinstance(line, Line):
            a, b = line.start, line.end
            angleLine = line.angle()
            line = line.length()
        else:
            a= Point.default()
            if not isinstance(angleLine, (float, int)):
                angleLine = randomAngle90plus()
                print(angleLine)
            if isinstance(line, (float, int)):
                b = Point.fromMetrics(
                    angle=angleLine,
                    distance=line, point=a
                )
            else:
                line = randomLength()
                b = Point.fromMetrics(
                    angle=angleLine, distance=line,
                    point=a
                )
        if not isinstance(lengthOther, (float, int)):
            lengthOther = randomLength()
        theta1 = (pi - angle) / 2
        smiBse = line * sin(angle / 2)
        theta2 = acos(smiBse / lengthOther)
        angleCommon = theta1 + theta2
        d = Point.fromMetrics((angle+angleLine), line, a)
        c = Point.fromMetrics(pi-angleCommon+angleLine, lengthOther, b)
        return cls.fromPoints([a,b,c,d])

    @classmethod
    def default(cls, ):
        """Build a random kite."""
        return cls.fromMetrics()


    # Helpers.
    @staticmethod
    def checkClass(trap:Quadrilateral):
        """Check if trapezoid can be constructed."""
        new = trap.checkSubClass()
        if isinstance(new, Kite):
            return new
        a,b,c,d = trap.vertices
        print(
            a.distanceTo(point=b),
            b.distanceTo(point=c),
            c.distanceTo(point=d),
            d.distanceTo(point=a)
        )
        raise ValueError(
            "ValueError:\tThe Quadrilateral can't "+
            "be constructed as a kite."
        )

