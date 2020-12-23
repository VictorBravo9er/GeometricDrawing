"""Module for Point."""
from Drawables.Drawable import Drawable
from Drawables.Quad import Quadrilateral
from math import degrees, pi, radians, sin
from random import random
import numpy as np

class Kite(Quadrilateral):
    """Base class of kite."""

    _rhombus:str = "rhombus"
    def __init__(self):
        """Class constructor."""
        super().__init__()

    @classmethod
    def fromPoints(cls, listOfPoint: list):
        """Build trapezoid from provided points."""
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
        """Build parallelogram from provided lines."""
        points = cls.edgeToVertex(listOfLine)
        return cls.fromPoints(points)

    @classmethod
    def fromKite(cls, trap):
        """Copy another Trapezoid."""
        new = cls()
        if isinstance(trap, cls):
            points = cls.newVertices(trap.vertices)
            new.setPolygon(vertexList=points)
            return new
        raise TypeError(
            "TypeError:\tExpected Kite, "+
            f"received {type(trap).__name__}"
        )

    @classmethod
    def fromMetrics(
        cls, line=..., lengthOther:float=...,
        angle:float=..., angleCommon:float=...
    ):
        """Draws a kite from some metrics: a line(/line length), an internal angle, other length."""
        from Drawables.Line import Line
        from Drawables.Point import Point
        a,b=...,...
        if not isinstance(angle, (float, int)):
            angle = 0.1 + (random() % 3)
        if not isinstance(angleCommon, (float, int)):
            angleCommon = 0.1 + (random() % 3)
        if isinstance(line, Line):
            a, b = line.start, line.end
            line = line.length()
        else:
            a= Point.default()
            if isinstance(line, (float, int)):
                b = Point.fromMetrics(
                    angle=(random() % pi),
                    distance=line, point=a
                )
            else:
                b = Point.default()
                line = a.distanceTo(b)
        if not isinstance(lengthOther, (float, int)):
            lengthOther = (
                Drawable._minX + 
                random() % (Drawable._maxX -Drawable._minX)
            )
        angle = a.angleTo(b)
        d = Point.fromMetrics(angle+angle, line, a)
        c = Point.fromMetrics(pi-angleCommon+angle, lengthOther, b)
        return cls.fromPoints([a,b,c,d])

    @classmethod
    def default(cls, ):
        """Build a random Quadrilateral."""
        return cls.fromMetrics()


    # Helpers.
    @staticmethod
    def checkClass(trap:Quadrilateral):
        """Check if trapezoid can be constructed."""
        new = trap.checkSubClass()
        if isinstance(new, Kite):
            return new
        raise ValueError(
            "ValueError:\tThe Quadrilateral can't "+
            "be constructed as a kite."
        )

