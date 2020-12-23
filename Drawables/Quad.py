"""Module for Point."""
from Drawables.Drawable import Drawable
from Drawables.Polygon import Polygon
from math import degrees, pi, radians
import numpy as np

class Quadrilateral(Polygon):
    """Base class of quadrilaterals."""

    _parallelogram:str = "parallelogram"
    _trapezoid:str = "trapezoid"
    _kite:str ="kite"

    def __init__(self):
        """Class constructor."""
        super().__init__()

    @classmethod
    def fromPoints(cls, listOfPoint: list):
        """Build Quad from provided points."""
        if len(listOfPoint) != 4:
            raise ValueError(
                "ValueError:\tThe Polygon can't be constructed"+
                " as a quadrilateral."
            )
        new = cls()
        new.setPolygon(listOfPoint)
        return new.checkSubClass()

    @classmethod
    def fromLines(cls, listOfLine: list):
        """Build Quad from provided lines."""
        points = cls.edgeToVertex(listOfLine)
        return cls.fromPoints(points)

    @classmethod
    def fromQuad(cls, quad):
        """Copy another Quad."""
        new = cls()
        if isinstance(quad, cls):
            points = cls.newVertices(quad.vertices)
            new.setPolygon(vertexList=points)
            return new
        raise TypeError(
            "TypeError:\tExpected Quadrilateral, "+
            f"received {type(quad).__name__}"
        )

    @classmethod
    def default(cls):
        """Build a random Quadrilateral."""
        from Drawables.Point import Point
        new = cls()
        while True:
            points = [
                Point.default(), Point.default(),
                Point.default(), Point.default()
            ]
            try:
                new.setPolygon(vertexList=points, allowAbnormal=False)
                return new
            except:
                continue


    # Methods.
    def diagonalAtPoint(self, point=..., idx:int=...):
        """Draw diagonal from specified point/index of point."""
        point, idx = self.resolvePoint(point=point, idx=idx)
        return point.lineToPoint(self.vertices[idx-2])

    def bimedianOnLine(self, line=..., idx:int=...):
        """Draw bimedian from specified line/index of line."""
        from Drawables.Point import Point
        from Drawables.Line import Line
        if isinstance(idx, (int, float)):
            idx = round(idx)
        elif isinstance(line, Line):
            a = (self.lineInQuad(line))
            if a == None:
                raise ValueError(
                    "ValueError:\tLine not in quad."
                )
            else:
                idx = round(a)
        else:
            raise TypeError(
                "TypeError:\tExpected Line or float, received "+
                f"{type(line).__name__} and {type(idx).__name__}."
            )
        p1 = Point.middlePoint(
            self.vertices[idx], self.vertices[idx-1]
        )
        idx = (idx + 2) % 4
        p2 = Point.middlePoint(
            self.vertices[idx], self.vertices[idx-1]
        )
        return Line.fromPoints(p1, p2)

    def diagonalIntersection(self):
        """Find diagonal intersection point."""
        l1 = self.diagonalAtPoint(idx=0)
        l2 = self.diagonalAtPoint(idx=1)
        return l1.intersectionWith(l2)

    def bimedianIntersection(self):
        """Find bimedian intersection point."""
        l1 = self.bimedianOnLine(idx=0)
        l2 = self.bimedianOnLine(idx=1)
        return l1.intersectionWith(l2)


    # Helpers.
    def checkSubClass(self, checkSub:bool=True):
        """Check if object could fit into a more specific subclass of quadrilateral."""
        lines = self.edges()
        slope = [x.slope() for x in lines]
        length = [x.length() for x in lines]
        if (
            abs(slope[0]- slope[2]) < Drawable._comparisonLimit and
            abs(slope[1] - slope[3]) < Drawable._comparisonLimit
        ):
            from Drawables.Parallelogram import Parallelogram
            new = Parallelogram()
            rectangle = abs((slope[1] * slope[2]) +1) < Drawable._comparisonLimit
            rhombus = abs(length[1] - length[2]) < Drawable._comparisonLimit
            if rectangle and rhombus:
                square_
            if rectangle:
                rectangle_
            if rhombus:
                rhombus_
            new.vertices = self.vertices
            new.size = self.size
            new.clockwise = self.clockwise
            return new
        if slope[0] == slope[2] or slope[1] == slope[3]:
            from Drawables.Trapezoid import Trapezoid
            new = Trapezoid()
            new.vertices = self.vertices
            new.size = self.size
            new.clockwise = self.clockwise
            return new
        if (
            (length[0] == length[1] and length[2] == length[3]) or
            (length[0] == length[3] and length[1] == length[2])
        ):
            from Drawables.Kite import Kite
            new = Kite()
            new.vertices = self.vertices
            new.size = self.size
            new.clockwise = self.clockwise
            return new
        return self

    def lineInQuad(self, line):
        """Check if Line is in Quad."""
        from Drawables.Line import Line
        for idx in range(-1, 3):
            if Line.orientation(line, self.vertices[idx]) == 0:
                if Line.orientation(line, self.vertices[idx+1]) == 0:
                    return idx+1
                if Line.orientation(line, self.vertices[idx-1]) == 0:
                    return idx
                return None
        return None
