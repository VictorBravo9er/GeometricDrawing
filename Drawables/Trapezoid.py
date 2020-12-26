"""Module for Point."""
from Drawables.randoms import *
from Drawables.Drawable import Drawable
from Drawables.Quad import Quadrilateral
from math import degrees, pi, radians, sin
import numpy as np

class Trapezoid(Quadrilateral):
    """Base class of Trapezoid."""

    _parallelogram:str="parallelogram"
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
        """Build trapezoid from provided lines."""
        points = cls.edgeToVertex(listOfLine)
        return cls.fromPoints(points)

    @classmethod
    def fromTrapezoid(cls, trap):
        """Copy from another trapezoid."""
        if isinstance(trap, cls):
            new = type(trap)()
            new.vertices = cls.newVertices(trap.vertices)
            new.size = trap.size
            new.clockwise = trap.clockwise
            return new
        raise TypeError(
            "TypeError:\tExpected Trapezoid, "+
            f"received {type(trap).__name__}"
        )

    @classmethod
    def fromMetrics(
        cls, line=..., angle1:float=...,
        angle2:float=..., height:float=...
    ):
        """Draws a trapezoid from some metrics: a base(or its length and angle), internal angles at its ends, and height."""
        from Drawables.Line import Line
        from Drawables.Point import Point
        a,b=...,...
        if not isinstance(angle1, (float, int)):
            angle1 = randomAngle180()
        if not isinstance(angle2, (float, int)):
            angle2 = randomAngle180()
        if isinstance(line, Line):
            a, b = line.start, line.end
        else:
            a= Point.default()
            if isinstance(line, (float, int)):
                b = Point.fromMetrics(
                    angle=randomAngleFull(),
                    distance=line, point=a
                )
            else:
                b = Point.default()
        angle = a.angleTo(b)
        if not isinstance(height, (float, int)):
            d = Point.fromMetrics(angle1+angle, 1, a)
            c = Point.fromMetrics(pi-angle2+angle, 1, b)
            h = (a.lineToPoint(d)).intersectionWith(b.lineToPoint(c)).distanceTo(a.lineToPoint(b))
            height = randomRange(1,h-1) * 0.9
        d = Point.fromMetrics(angle1+angle, height / sin(angle1), a)
        c = Point.fromMetrics(pi-angle2+angle, height / sin(angle2), b)
        return cls.fromPoints([a,b,c,d])

    @classmethod
    def default(cls, ):
        """Build a random trapezoid."""
        return cls.fromMetrics()


    # Helpers.
    @staticmethod
    def checkClass(trap:Quadrilateral):
        """Check if trapezoid can be constructed."""
        new = trap.checkSubClass()
        if isinstance(new, Trapezoid):
            return new
        raise ValueError(
            "ValueError:\tThe Quadrilateral can't "+
            "be constructed as a trapezoid."
        )
