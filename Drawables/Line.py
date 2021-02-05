"""Module Line."""
from Drawables.randoms import *
from Drawables.Drawable import Drawable
from math import inf, pi, atan, cos, sin
import numpy as np

class Line(Drawable):
    """Description of class."""

    _xAxis, _yAxis = "x-axis", "y-axis"
    def __init__(self):
        """Construct default."""
        from Drawables.Point import Point
        super().__init__()
        # Drawable.__init__(self)
        self.start:Point
        self.end:Point
        self.__extend:float = 0
        self.extend__:float = 0


    # Constructors
    @classmethod
    def fromLine(cls, line, distance:float=0):
        """Copy from another line."""
        from Drawables.Point import Point
        if not isinstance(line, cls):
            raise TypeError(
                f"TypeError:\tExpected Line, recceived {type(line).__name__}"
            )
        new = cls()
        angle = line.slope()
        angle = atan(angle) + (pi / 2)
        if line.start.Y > line.end.Y:
            distance *= -1
        new.start = Point.fromMetrics(angle, distance, line.start)
        new.end = Point.fromMetrics(angle, distance, line.end)
        return new

    @classmethod
    def fromPoints(cls, point1, point2):
        """Construct a line provided two end-points are given."""
        from Drawables.Point import Point
        if isinstance(point1, Point) and isinstance(point2, Point):
            new = cls()
            new.setLine(start=point1, end=point2)
            return new
        raise TypeError(
            "TypeError:\tExpected (Point, Point), received"+
            f"({type(point1).__name__}, {type(point2).__name__})"
        )

    @classmethod
    def fromMetrics(cls, angle:float, length:float, point):
        """Draw line along an angle of some length from a point."""
        from Drawables.Point import Point
        new = cls()
        new.setLine(
            start=point,
            end=Point.fromMetrics(angle, length, point)
        )
        return new

    @classmethod
    def default(cls, parallelAxis:str=...):
        """Construct a random line or axis parallel line(X or Y axis), if notified."""
        from Drawables.Point import Point
        if isinstance(parallelAxis, str):
            angle = -1
            if parallelAxis == cls._xAxis:
                angle = 0
            elif parallelAxis == cls._yAxis:
                angle = pi * 0.5
            if angle != -1:
                return Line.fromMetrics(
                    angle=angle,
                    point=Point.default(),
                    length=randomLength()
                )
        return cls.fromMetrics(
            angle=randomAngle180(), point=Point.default(),
            length=randomLength()
        )


    # Getters and Setters
    def getLine(self):
        """Getter Method."""
        return (self.start, self.end)

    def setLine(self, start=..., end=...):
        """Setter Method."""
        from Drawables.Point import Point
        if isinstance(start, Point):
            self.start = start
        if isinstance(end, Point):
            self.end = end


    # Methods
    def slope(self):
        """Slope of line."""
        return(self.start.slopeTo(self.end))

    def angle(self):
        """Angle subtended by line with +ve direction of  x-axis."""
        return self.start.angleTo(self.end)

    def length(self):
        """Find length of the Line segment."""
        return self.start.distanceTo(point=self.end)

    def distanceFrom(self, line=..., point=...):
        """Distance from a point or line(if parallel)."""
        from Drawables.Point import Point
        if isinstance(point, Point):
            return point.distanceTo(point=self.projectionOf(point, False))
        if isinstance(line, Line):
            (m1, c1) = self.getMetrics()
            (m2, c2) = line.getMetrics()
            if abs(m1 - m2) > self._comparisonLimit:
                raise ValueError(
                    f"ValueError:\tLines intersect at{self.intersectionWith(line, False)}"
                )
            angle_rad = atan(abs(m1))
            return abs(c1 - c2) * cos(angle_rad)
        raise TypeError(
            "TypeError:\tExpected: Line or Point, received: "+
            f"{type(line).__name__} and {type(point).__name__}."
        )

    def bisector(self):
        """Bisector(mid point) of the line."""
        from Drawables.Point import Point
        return(Point.middlePoint(self.start, self.end))
        #return self.sector(1)

    def sector(self, m:float = 1, n:float = 1):
        """Point that divides line in ratio of m:n."""
        from Drawables.Point import Point
        return(Point.fromSection(self.start, self.end, m, n))

    def intersectionWith(self, line, _extend:bool=True):
        """Intersection point of two lines."""
        from Drawables.Point import Point
        if isinstance(line, Line):
            (m1, c1) = self.getMetrics()
            (m2, c2) = line.getMetrics()
            x = (c1 - c2) / (m2 - m1)
            y = m1 * x + c1
            inter = (Point.fromCoOrdinates(x, y))
            if _extend:
                self.extend(inter)
                line.extend(inter)
            return inter
        raise TypeError(
            f"TypeError:\tExpected: Line, received {type(line).__name__}"
        )

    def parallelLine(self, distance:float=None, point=None):
        """Draw a parallel line that is either at a certain distance or passes through a given point."""
        from Drawables.Point import Point
        if isinstance(point, Point):
            distance = point.distanceTo(line=self)
            distance *= -self.orientation(point)
        if isinstance(distance, (float, int)):
            return Line.fromLine(line=self, distance=distance)
        raise TypeError(
            "TypeError:\tExpected: float or Point, received: "+
            f"{type(distance).__name__} and {type(point).__name__}."
        )

    def projectionOf(self, point, _extend:bool=True):
        """Projection of point on the line."""
        l  = self.start.distanceTo(point=self.end)
        l1 = self.start.distanceTo(point=point)
        l2 = self.end.distanceTo(point=point)
        n = ((l ** 2) + (l2 ** 2) - (l1 ** 2)) / (2 * l)
        m = l - n
        projected = self.sector(m, n)
        if _extend:
            self.extend(projected)
        return projected

    def perpendicularFrom(self, point, _extend:bool=True):
        """Perpendicular from a point to the line."""
        prjkt = self.projectionOf(point, _extend)
        if prjkt.distanceTo(point=point) < 1:
            return self.perpendicularAt(point=prjkt)
        return Line.fromPoints(prjkt, point)

    def perpendicularAt(self, point=..., ratio:float=..., _extend:bool=True):
        """Perpendicular at a point or a point that divides the line ina certain ratio."""
        if isinstance(ratio, (float, int)):
            point = self.sector(m=ratio)
        from Drawables.Point import Point
        if isinstance(point, Point):
            from Drawables.Point import Point
            len_ = self.length() / 2
            if _extend:
                self.extend(point)
            angle = atan(-1/self.slope())
            point1 = Point.fromMetrics( angle, len_, point)
            point2 = Point.fromMetrics( angle,-len_, point)
            return(Line.fromPoints(point1, point2))
        raise TypeError(
            "TypeError:\tExpected a Point or float, received "+
            f"{type(point).__name__} and {type(ratio).__name__}."
        )

    def perpendicularBisector(self):
        """Perpendicular bisector of the line."""
        return(self.perpendicularAt(point=self.bisector()))

    def triangleTo(self, point):
        """Draw a triangle with the line and an additional point."""
        from Drawables.Triangle import Triangle
        return Triangle.fromLine(self, point)

    def circleAround(
        self, chordDistance:float=...,
        tangentCentre=..., chordCentre=...
    ):
        """Draw circle with line as diameter, or as a chord or tangent if their respective centres are given."""
        from Drawables.Point import Point
        if isinstance(chordDistance, (float, int)):
            from Drawables.Circle import Circle
            centre = Point.fromMetrics(
                    (self.angle() + pi / 2) % (2 * pi),
                    chordDistance,
                    self.bisector()
                )
            return Circle.fromMetrics(centre, centre.distanceTo(point=self.end))
        if isinstance(tangentCentre, Point):
            return Point.circleFrom(tangentCentre, tangent=self)
        if isinstance(chordCentre, Point):
            return Point.circleFrom(chordCentre, chord=self)
        if chordCentre is ... or tangentCentre is ... and chordCentre is ...:
            mid = self.bisector()
            radius = self.length() / 2
            return mid.circle(radius)
        raise TypeError(
            "TypeError:\tExpected a float, Point or Point, received "
            f"{type(chordDistance).__name__}, {type(tangentCentre).__name__}"+
            f", and {type(chordCentre).__name__}"
        )

    def square(self):
        """Draw a square with the line as one of it's sides."""
        from Drawables.Square import Square
        return Square.fromMetrics(self)

    def rectangle(self, sideLength:float,):
        """Draw a rectangle with the line as one of it's sides and length of adjacent side."""
        from Drawables.Rectangle import Rectangle
        return Rectangle.fromMetrics(line=self, lengthOther=sideLength)


    # Helpers
    def orientation(self, point):
        """Orientation test. 0 - coliniar, 1 - left, -1 - right."""
        return Drawable.orientation(self.start, self.end, point)

    def extendLimits(self):
        """Extend Drawable extents."""
        self.start.extendLimits()
        self.end.extendLimits()

    def extend(self, point=..., extension=...):
        """Extend the ends of line as displayed when drawn."""
        if isinstance(extension, tuple) and len(extension) == 2:
            (self.__extend, self.extend__) = extension
            return
        from Drawables.Point import Point
        if isinstance(point, Point):
            if Drawable.orientation(
                self.start, self.end, point
            ) != 0:
                return
                raise ValueError("Point is non coliniar with Line")
            _x, x_, l = (
                Point.distanceTo(point, point=self.start),
                Point.distanceTo(point, point=self.end),
                self.length()
            )
            if abs(_x + x_ - l) < Drawable._comparisonLimit:
                return
            if _x < x_:
                if self.__extend < _x:
                    self.__extend = _x
                return
            if self.extend__ < x_:
                self.extend__ = x_

    def getMetrics(self):
        """Return slope and y-intercept of Line segment."""
        #y = mx + c
        m = self.slope()
        if m == inf:
            return(inf, self.start.X)
        (x, y) = self.start.getPoint()
        c = (y - m * x)
        return(m, c)

    def lengthl1(self):
        """Find length of the Line segment."""
        return self.start.distanceL1(point=self.end)

    def _scale(self, sx:float=1, sy:float=1, point=...):
        if sx == 1 and sy == 1:
            return
        transform = self.scaleMatrix(sx, sy, point)
        self._applyTransform(transform)

    def _translate(self, tx:float=0, ty:float=0):
        if tx == 0 and ty == 0:
            return
        transform = self.translateMatrix(tx, ty)
        self._applyTransform(transform)

    def _rotate(self, centre=...,angle:float=0):
        if angle == 0:
            return
        transform = self.rotateMatrix(angle, centre)
        self._applyTransform(transform)

    def _reflectPoint(self, point):
        transform = self.reflectionPointMatrix(point)
        self._applyTransform(transform)

    def _reflectLine(self, line):
        transform = self.reftectionLineMatrix(*Line.getMetrics(line))
        self._applyTransform(transform)

    def _applyTransform(self, transform):
        homoCoord = np.array(
            [
                [self.start.X, self.end.X,],
                [self.start.Y, self.end.Y,],
                [1, 1]
            ]
        )
        homoCoord = np.array(homoCoord)
        homoCoord = np.reshape(
            np.dot(transform, homoCoord), (3, -1)
            ).T
        (self.start.X, self.start.Y) = [float(x) for x in homoCoord[0][0:2]]
        (self.end.X  , self.end.Y  ) = [float(x) for x in homoCoord[1][0:2]]

    def __ne__(self, o) -> bool:
        """'!=' operator overload."""
        return not self == o

    def __eq__(self, o) -> bool:
        """'==' operator overload."""
        if isinstance(o, Line):
            return (self.getMetrics() == o.getMetrics())
        raise TypeError(
            f"TypeError:\tCan't compare {self.__class__} with {type(o).__name__}"
        )

    def __hash__(self) -> int:
        """Hash function."""
        return  (
            (int(self.angle()*1024) << 22) +
            (int(self.start.X * 1024) << 15) +
            (int(self.start.Y * 1024) << 10) +
            (int(self.end.X * 1024) << 5) +
            int(self.end.Y * 1024)
        )


    # Output interface
    def __str__(self) -> str:
        """Text return."""
        return f"({self.start.X}, {self.start.Y}), ({self.end.X}, {self.end.Y})"

    def draw(self, axes):
        """Draw plots."""
        a = self.angle()
        c, s = cos(a), sin(a)
        if self.__extend != 0 or self.extend__ != 0:
            x = (self.start.X - c * self.__extend, self.end.X + c * self.extend__)
            y = (self.start.Y - s * self.__extend, self.end.Y + s * self.extend__)
            axes.plot(x,y)
        axes.plot(
            (self.start.X, self.end.X),(self.start.Y, self.end.Y)
        )
