"""Module for Point."""
from Drawables.randoms import *
from Drawables.Drawable import Drawable
from Drawables.Quad import Quadrilateral
from Drawables.Rhombus import Rhombus
from Drawables.Rectangle import Rectangle
from math import degrees, pi, radians
import numpy as np

class Square(Rectangle, Rhombus):
    """Base class of Parallelogram."""

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
    def fromSquare(cls, sqre):
        """Copy another parallelogram."""
        if isinstance(sqre, cls):
            new = type(sqre)()
            points = cls.newVertices(sqre.vertices)
            new.setPolygon(vertexList=points)
            return new
        raise TypeError(
            "TypeError:\tExpected Quadrilateral, "+
            f"received {type(sqre).__name__}"
        )

    @classmethod
    def fromMetrics(cls, line=..., angle:float=...,):
        """Draws a parallelogram from some metrics: a line(/line length), an internal angle, other length."""
        from Drawables.Line import Line
        from Drawables.Point import Point
        a,b=...,...
        if isinstance(line, Line):
            a, b = line.start, line.end
            angle = line.angle() + pi * 0.5
            line = line.length()
        else:
            a= Point.default()
            if not isinstance(angle, (float, int)):
                angle = randomAngle180()
            if not isinstance(line, (float, int)):
                line = randomLength()
            b = Point.fromMetrics(
                angle=angle,
                distance=line, point=a
            )
        angle += pi * 0.5
        d = Point.fromMetrics(angle, line, a)
        c = Point.fromMetrics(angle, line, b)
        return cls.fromPoints([a,b,c,d])

    @classmethod
    def default(cls, ):
        """Build a random Quadrilateral."""
        return cls.fromMetrics()


    # Helpers.
    @staticmethod
    def checkClass(trap:Quadrilateral):
        """Check if Square can be constructed."""
        new = trap.checkSubClass()
        if isinstance(new, Square):
            return new
        raise ValueError(
            "ValueError:\tThe Quadrilateral can't "+
            "be constructed as a parallelogram."
        )