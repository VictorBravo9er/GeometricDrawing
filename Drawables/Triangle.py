"""Module for Point."""
import numpy as np
from Drawables.Drawable import Drawable
from math import sqrt
from Drawables.Polygon import Polygon

class Triangle(Polygon):
    """Triangle class."""
    
    def __init__(self):
        """Initialize method."""
        super().__init__()

    @classmethod
    def fromLine(cls, line, point):
        """Draw Triangle from a line and a point."""
        new = cls()
        points = [point, line.start, line.end]
        new.setPolygon(vertexList=points)
        return(new)

    @classmethod
    def fromLines(cls, lineList: list):
        """Draw Triangle from list of lines."""
        new = cls()
        new.setPolygon(edgeList=lineList)
        return new

    @classmethod
    def fromPoints(cls, pointList: list):
        """Draw Triangle list of points."""
        new = cls()
        new.setPolygon(vertexList=pointList)
        return new

    @classmethod
    def fromTriangle(cls, triangle):
        """Draw Triangle copied from another triangle."""
        new = cls()
        new.setPolygon(vertexList=Triangle.newVertices(triangle.vertices))
        return new


    # Methods
    def area(self):
        """Heron's Formula."""
        from Drawables.Point import Point
        lengths = list()
        prev = self.vertices[-1]
        for cur in self.vertices:
            l = Point.distanceTo(prev, point=cur)
            lengths.append(l)
            prev = cur
        lengths = np.array(lengths)
        s = np.sum(lengths) / 2
        A = s * np.prod(s - lengths)
        return float(A ** 0.5)

    def centroid(self):
        """Find centroid of triangle."""
        l1 = self.angleBisector(idx=0)
        l2 = self.angleBisector(idx=1)
        return l1.intersectionWith(l2) 

    def orthocentre(self):
        """Find orthocentre of triangle."""
        l1 = self.perpendicularFromPoint(idx=0)
        l2 = self.perpendicularFromPoint(idx=1)
        return l1.intersectionWith(l2)

    def circumcenter(self):
        """Find circumcentre of triangle."""
        from Drawables.Line import Line
        from Drawables.Point import Point
        a,b,c = self.vertices[0:3]
        l1 = Point.bisect(a, b)
        l2 = Point.bisect(a, c)
        return Line.intersectionWith(l1, l2)

    def circumcircle(self):
        """Draw circumcircle of triangle."""
        from Drawables.Circle import Circle
        x = self.circumcenter()
        return Circle.fromMetrics(x, x.distanceTo(point=self.vertices[0]))

    def incenter(self):
        """Find incentre of triangle."""
        from Drawables.Line import Line
        a,b,c = self.vertices[0:3]
        l1 = a.bisectAnglePoints(c,b)
        l2 = b.bisectAnglePoints(a,c)
        return Line.intersectionWith(l1, l2)

    def incircle(self):
        """Draw incircle of triangle."""
        centre = self.incenter()
        from Drawables.Line import Line
        distance = Line.fromPoints(
                self.vertices[0], self.vertices[1]
            ).distanceFrom(point=centre)
        from Drawables.Circle import Circle
        return Circle.fromMetrics(centre, distance)

    def medianFromPoint(self, point=None, idx:int=None):
        """Draw a median from a specified point."""
        from Drawables.Point import Point
        from Drawables.Line import Line
        (a, point, c) = self.resolvePoint(point=point, idx=idx)
        median = Line.fromPoints(
            point,
            Point.middlePoint(a, c)
            )
        return median

    def medianOnLine(self, line):
        """Draw a median on a specified line."""
        from Drawables.Line import Line
        if isinstance(line, Line):
            return self.medianFromPoint(point=self.pointOppLine(line))
        raise ValueError(f"Expected: {Line.__name__}, received {type(line).__name__}")

    def angleBisector(self, point=..., idx:int=...):
        """Angle Bisector from a certain point."""
        from Drawables.Line import Line
        bisector = super().angleBisector(point=point, idx=idx)
        bisector.setLine(
            end=bisector.intersectionWith(
                Line.fromPoints(
                    self.vertices[idx-1],
                    self.vertices[(idx + 1) % 3]
                    )
                )
            )
        return bisector

    def angleBisectorOnLine(self, line):
        """Angle Bisector on a certain line."""
        from Drawables.Line import Line
        if isinstance(line, Line):
            return self.angleBisector(point=self.pointOppLine(line))
        raise ValueError(f"Expected: {Line.__name__}, received {type(line).__name__}")

    def perpendicularFromPoint(self, point=None, idx:int=None):
        """Draw a perpendicular from a specified point."""
        from Drawables.Line import Line
        (a, point, c) = self.resolvePoint(point=point, idx=idx)
        perpendicular = Line.fromPoints(
                        a, c
                    ).perpendicularFrom(point)
        return perpendicular

    def perpendicularOnLine(self, line):
        """Draw a perpendicular on a specified line."""
        from Drawables.Line import Line
        if isinstance(line, Line):
            return self.perpendicularFromPoint(point=self.pointOppLine(line))
        raise ValueError(f"Expected: {Line.__name__}, received {type(line).__name__}")


    # Helpers.
    def lineOppPoint(self, point=..., idx:int=...):
        """Determine line opposite to a point."""
        from Drawables.Line import Line
        point, idx = self.resolvePoint(point=point, idx=idx)
        return Line.fromPoints(
                self.vertices[idx - 1],
                self.vertices[(idx + 1) % 3]
            )

    def pointOppLine(self, line):
        """Determine point opposite to a line."""
        from Drawables.Point import Point
        x = []
        count = 0
        for point in self.vertices:
            if Drawable.orientation(
                line.start, line.end, point
                ) == 0:
                count += 1
                continue
            x.append(point)
        if count == 2 and len(x) == 1:
            point:Point = x[0]
            return point
        raise ValueError("Line doesn't constitute the triangle.")

    def resolvePoint(self, point, idx: int):
        """Resolve availability of vertex in Triangle."""
        point, idx =  super().resolvePoint(point=point, idx=idx)
        a, c = (
            self.vertices[idx - 1], 
            self.vertices[(idx + 1) % 3]
            )
        return a, point, c
