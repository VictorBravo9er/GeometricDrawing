"""Module for Point."""
from Drawables.randoms import *
from Drawables.Drawable import Drawable
from Drawables.Polygon import Polygon
from math import degrees, pi
import numpy as np

class Triangle(Polygon):
    """Triangle class."""

    _acute:str = "acute"
    _obtuse:str= "obtuse"
    _right:str = "right"
    _equilateral:str= "equilateral"
    _isoscales:str = "isoscales"

    def __init__(self):
        """Initialize method."""
        super().__init__()

    @classmethod
    def fromLine(cls, line, point):
        """Draw Triangle from a line and a point."""
        from Drawables.Point import Point
        from Drawables.Line import Line
        new = cls()
        if isinstance(point, Point) and isinstance(line, Line):
            raise TypeError(
                "TypeError:\tExpected: (Line, Point), received"+
                f": ({type(line).__name__}, {type(point).__name__})"
            )
        points = [point, line.start, line.end]
        new.setPolygon(vertexList=points)
        return(new)

    @classmethod
    def fromLines(cls, listOfLine:list):
        """Draw Triangle from list of lines."""
        l = len(listOfLine)
        if l != 3:
            raise ValueError(
                f"ValueError:\tExpected 3 lines, received {l}."
            )
        new = cls()
        new.setPolygon(edgeList=listOfLine)
        return new

    @classmethod
    def fromPoints(cls, listOfPoint:list):
        """Draw Triangle list of points."""
        l = len(listOfPoint)
        if l != 3:
            raise ValueError(
                f"ValueError:\tExpected 3 lines, received {l}."
            )
        new = cls()
        new.setPolygon(vertexList=listOfPoint)
        return new

    @classmethod
    def fromTriangle(cls, triangle):
        """Draw Triangle copied from another triangle."""
        new = cls()
        if isinstance(triangle, Triangle):
            new.vertices = Triangle.newVertices(triangle.vertices)
            new.size = triangle.size
            new.clockwise = triangle.clockwise
            return new
        raise TypeError(
            f"TypeError:\tExpected: Triangle, received: {type(triangle).__name__}."
        )

    @classmethod
    def fromAngles(cls, angle1:float, angle2:float, base=...):
        """Draw a triangle from given angles and an optional base."""
        from Drawables.Line import Line
        if angle1 + angle2 >= 6.2:
            raise ValueError(
                "ValueError:\tUnexpected values for the angles"+
                "Expected: angle1 + angle2 < 180, received: "+
                f"angle1 = {degrees(angle1)}, angle2 = {degrees(angle2)}"
            )
        if isinstance(base, (float,int)):
            from Drawables.Point import Point
            base = Line.fromMetrics(
                angle=randomAngle180(),
                length=randomLength(),
                point=Point.default()
            )
        if not isinstance(base, Line):
            base = Line.default(Line._xAxis)
        angle = base.angle()
        l1 = Line.fromMetrics(angle1+angle, 2, base.start)
        l2 = Line.fromMetrics(pi-angle2+angle, 2, base.end)
        point = l1.intersectionWith(l2)
        if base.end.Y == base.start.Y:
            if point.Y < base.start.Y:
                point.Y = -point.Y
        return cls.fromLine(base, point)

    @classmethod
    def default(cls, _type:str=...):
        """Provide a random triangle, with type if provided(acute, obtuse, and right angled, equilateral and isoscales)."""
        angle1 = randomRange(0.1, 3)
        angle2 = randomRange(0.1, 3 - angle1)
        if isinstance(_type, str):
            if _type == cls._acute:
                angle1 = randomRange(0.1, 1.45)
                angle2 = randomRange(0.1, 1.45)
            elif _type == cls._right:
                angle1 = (pi * 0.5)
                angle2 = randomRange(0.1, 1.45)
            elif _type == cls._obtuse:
                angle1 = randomRange(1.6, 1.4)
                angle2 = randomRange(0.1, 3 - angle1)
            elif _type == cls._equilateral:
                angle1 = pi / 3
                angle2 = angle1
            elif _type == cls._isoscales:
                angle1 = randomRange(0.1, 1.45)
                angle2 = angle1
        cls.fromAngles(angle1, angle2)


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
        (a, b, c) = self.vertices[0:3]
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

    def medianFromPoint(self, point=..., idx:int=...):
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
        raise ValueError(
            f"TypeError:\tExpected {Line.__name__},"+
            f" received {type(line).__name__}"
        )

    def angleBisector(self, point=..., idx:int=...):
        """Angle Bisector from a certain point."""
        from Drawables.Line import Line
        (a, point, b) = self.resolvePoint(point=point, idx=idx)
        bisector = super().angleBisector(point=point)
        bisector.setLine(
            end=bisector.intersectionWith(
                Line.fromPoints(a, b)
            )
        )
        return bisector

    def angleBisectorOnLine(self, line):
        """Angle Bisector on a certain line."""
        from Drawables.Line import Line
        if isinstance(line, Line):
            return self.angleBisector(point=self.pointOppLine(line))
        raise ValueError(
            f"TypeError:\tExpected: {Line.__name__},"+
            f" received {type(line).__name__}"
        )

    def perpendicularFromPoint(self, point=..., idx:int=...):
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
        raise ValueError(
            f"TypeError:\tExpected: {Line.__name__}, "+
            f"received {type(line).__name__}"
        )


    # Helpers.
    def lineOppPoint(self, point=..., idx:int=...):
        """Determine line opposite to a point."""
        from Drawables.Line import Line
        (a, point, b) = self.resolvePoint(point=point, idx=idx)
        return Line.fromPoints(a, b)

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
        raise ValueError(
            "ValueError:\tProvided line doesn't allign "+
            "with any of the sides of the triangle."
        )

    def resolvePoint(self, point, idx:int):
        """Resolve availability of vertex in Triangle."""
        from Drawables.Point import Point
        point, idx =  super().resolvePoint(point=point, idx=idx)
        a:Point = self.vertices[idx - 1]
        c:Point = self.vertices[(idx + 1) % 3]
        return a, point, c
