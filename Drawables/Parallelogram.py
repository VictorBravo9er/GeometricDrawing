"""Module for Point."""
from Drawables.randoms import *
from Drawables.Drawable import Drawable
from Drawables.Quad import Quadrilateral
from Drawables.Trapezoid import Trapezoid
from math import degrees, pi, radians
import numpy as np

class Parallelogram(Trapezoid):
    """Base class of Parallelogram."""

    _rectangle:str = "rectangle"
    _rhombus:str = "rhombus"
    def __init__(self):
        """Class constructor."""
        super().__init__()

    @classmethod
    def fromPoints(cls, listOfPoint: list):
        """Build parallelogram from provided points."""
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
    def fromParallelogram(cls, parallelo):
        """Copy another parallelogram."""
        if isinstance(parallelo, cls):
            new = type(parallelo)()
            new.vertices = cls.newVertices(parallelo.vertices)
            new.size = parallelo.size
            new.clockwise = parallelo.clockwise
            return new
        raise TypeError(
            "TypeError:\tExpected Quadrilateral, "+
            f"received {type(parallelo).__name__}"
        )

    @classmethod
    def fromMetrics(cls, line=...,angleLine:float=..., angle:float=..., length:float=...):
        """Draws a parallelogram from some metrics: a line(/line length), an internal angle, other length."""
        from Drawables.Line import Line
        from Drawables.Point import Point
        a,b=...,...
        if isinstance(line, Line):
            a, b = line.start, line.end
            angleLine = a.angleTo(b)
        else:
            if not isinstance(angleLine, (int, float)):
                angleLine = randomAngle180()
            a= Point.default()
            if isinstance(line, (float, int)):
                b = Point.fromMetrics(
                    angle=angleLine,
                    distance=line, point=a
                )
            else:
                b = Point.default()
        if not isinstance(angle, (float, int)):
            angle = randomAngle180()
        if not isinstance(length, (float, int)):
            length = randomLength()
        angle += angleLine
        d = Point.fromMetrics(angle, length, a)
        c = Point.fromMetrics(angle, length, b)
        return cls.fromPoints([a,b,c,d])

    @classmethod
    def default(cls, ):
        """Build a random Quadrilateral."""
        return cls.fromMetrics()


    # Helpers.
    @staticmethod
    def checkClass(trap:Quadrilateral):
        """Check if parallelogram can be constructed."""
        new = trap.checkSubClass()
        if isinstance(new, Parallelogram):
            return new
        raise ValueError(
            "ValueError:\tThe Quadrilateral can't "+
            "be constructed as a parallelogram."
        )