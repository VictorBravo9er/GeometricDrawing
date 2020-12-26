"""Module for Point."""
from Drawables.randoms import *
from Drawables.Drawable import Drawable
from Drawables.Quad import Quadrilateral
from Drawables.Parallelogram import Parallelogram
from Drawables.Kite import Kite
from math import degrees, pi, radians, sin
import numpy as np

class Rhombus(Parallelogram, Kite):
    """Base class of kite."""

    _square:str = "square"
    def __init__(self):
        """Class constructor."""
        super().__init__()

    @classmethod
    def fromPoints(cls, listOfPoint: list):
        """Build rhombus from provided points."""
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
        """Build rhombus from provided lines."""
        points = cls.edgeToVertex(listOfLine)
        return cls.fromPoints(points)

    @classmethod
    def fromRhombus(cls, rhom):
        """Copy another rhombus."""
        if isinstance(rhom, cls):
            new = type(rhom)()
            points = cls.newVertices(rhom.vertices)
            new.setPolygon(vertexList=points)
            return new
        raise TypeError(
            "TypeError:\tExpected Kite, "+
            f"received {type(rhom).__name__}"
        )

    @classmethod
    def fromMetrics(
        cls, line=..., angleLine:float=...,
        angleInternal:float=...,
    ):
        """Draws a kite from some metrics: a line(/line length), an internal angle, other length."""
        from Drawables.Line import Line
        from Drawables.Point import Point
        a,b=...,...
        if not isinstance(angleInternal, (float, int)):
            angleInternal = randomAngle180()
        if isinstance(line, Line):
            a, b = line.start, line.end
            angleLine = line.angle()
        else:
            a= Point.default()
            if not isinstance(angleLine, (float, int)):
                angleLine = randomAngleFull()
            if not isinstance(line, (float, int)):
                line = randomLength()
            b = Point.fromMetrics(
                angle=angleLine,
                distance=line, point=a
            )
        line = a.distanceTo(point=b)
        d = Point.fromMetrics(angleInternal+angleLine, line, a)
        c = Point.fromMetrics(angleInternal+angleLine, line, b)
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
        if isinstance(new, Rhombus):
            return new
        raise ValueError(
            "ValueError:\tThe Quadrilateral can't "+
            "be constructed as a kite."
        )

