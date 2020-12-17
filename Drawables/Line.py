"""Module Line."""
import numpy as np
from Drawables.Drawable import Drawable
from math import inf, pi, atan, cos, sin


class Line(Drawable):
    """Description of class."""

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
        """Derive another line from an existing one."""
        from Drawables.Point import Point
        if not isinstance(line, cls):
            raise TypeError("Type mismatch")
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
        new = cls()
        new.start = point1
        new.end = point2
        return new

    @classmethod
    def fromMetrics(cls, angle:float, length:float, point):
        """Draw Line using some metrics."""
        from Drawables.Point import Point
        new = cls()
        new.start = point
        new.end = Point.fromMetrics(angle, length, point)
        return new


    # Getters and Setters
    def getLine(self):
        """Getter Method."""
        return (self.start, self.end)

    def setLine(self, start, end):
        """Setter Method."""
        (self.start, self.end) = (start, end)


    # Methods
    def slope(self):
        """Return slope of line."""
        return(self.start.slopeTo(self.end))

    def angle(self):
        """Angle subtended by line with x-axis."""
        return self.start.angleTo(self.end)

    def length(self):
        """Find length of the Line segment."""
        try:
            return self._length
        except(Exception):
            self._length = self.start.distanceTo(self.end)
            return(self._length)

    def distanceFrom(self, o):
        """Distance from point or line."""
        from Drawables.Point import Point
        if isinstance(o, Point):
            return o.distanceTo(self.projectionOf(o))
        if isinstance(o, Line):
            (m1, c1) = self.getMetrics()
            (m2, c2) = o.getMetrics()
            if abs(m1 - m2) > self.comparisonLimit:
                raise Exception(
                    f"Lines intersect at{self.intersectionWith(o)}"
                    )
            angle_rad = atan(abs(m1))
            return abs(c1 - c2) * cos(angle_rad)
        raise TypeError("Unsupported Type.")

    def bisector(self):
        """Bisector of the line."""
        from Drawables.Point import Point
        return(Point.middlePoint(self.start, self.end))
        #return self.sector(1)

    def sector(self, m:float = 1, n:float = 1):
        """Sector of line in a ratio of m:n."""
        from Drawables.Point import Point
        return(Point.fromSection(self.start, self.end, m, n))

    def intersectionWith(self, line):
        """Point intersection of two lines."""
        from Drawables.Point import Point
        (m1, c1) = self.getMetrics()
        (m2, c2) = line.getMetrics()
        x = (c1 - c2) / (m2 - m1)
        y = m1 * x + c1
        return(Point.fromCoOrdinates(x, y))

    def parallelLine(self, distance:float=None, point=None):
        """Draw a parallel Line."""
        from Drawables.Point import Point
        if isinstance(point, Point):
            distance = point.distanceTo(self)
        if isinstance(distance, float) or isinstance(distance, int):
            return Line.fromLine(line=self, distance=distance)
        raise Exception("Invalid parameter(s).")

    def projectionOf(self, point):
        """Point projection."""
        l  = self.start.distanceTo(self.end)
        l1 = self.start.distanceTo(point)
        l2 = self.end.distanceTo(point)
        n = ((l ** 2) + (l2 ** 2) - (l1 ** 2)) / (2 * l)
        m = l - n
        return self.sector(m, n)

    def perpendicularFrom(self, point):
        """Perpendicular from a point to the line."""
        return Line.fromPoints(self.projectionOf(point), point)

    def perpendicularAt(self, var):
        """Perpendicular at a point or ratio on the line."""
        if isinstance(var, float):
            return(self.perpendicularAt(self.sector(var)))
        from Drawables.Point import Point
        if isinstance(var, Point):
            from Drawables.Point import Point
            len_ = self.length() / 2
            angle = atan(-1/self.slope())
            point1 = Point.fromMetrics( angle, len_, var)
            point2 = Point.fromMetrics( angle,-len_, var)
            return(Line.fromPoints(point1, point2))
        raise TypeError("Unsupported Type.")

    def perpendicularBisector(self):
        """Perpendicular bisector."""
        return(self.perpendicularAt(self.bisector()))

    def triangleTo(self, point):
        """Draw a Triangle."""
        from Drawables.Triangle import Triangle
        return Triangle.fromLine(self, point)

    def circleAround(self, chordDistance:float=None, tangentCentre=None, chordCentre=None):
        """Draw circle with line as diameter, chord or tangent."""
        from Drawables.Point import Point
        if chordCentre is None and tangentCentre is None and chordDistance is None:
            mid = self.bisector()
            radius = self.length() / 2
            return mid.circle(radius)
        if isinstance(chordDistance, float):
            from Drawables.Circle import Circle
            centre = Point.fromMetrics(
                    (self.angle() + pi / 2) % (2 * pi),
                    chordDistance,
                    self.bisector()
                )
            return Circle.fromMetrics(centre, centre.distanceTo(self.end))
        elif isinstance(tangentCentre, Point):
            return Point.circleFrom(tangentCentre, tangent=self)
        elif isinstance(chordCentre, Point):
            return Point.circleFrom(chordCentre, chord=self)
        raise Exception("invalid arguements.")

    def square(self, direction:str="up"):
        pass

    def rectangle(self, sideLength:float, direction:str="up"):
        pass


    # Helpers
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
                raise Exception("Point is non coliniar.")
            _x, x_, l = (
                    Point.distanceSquared(point, self.start),
                    Point.distanceSquared(point, self.end),
                    Point.distanceSquared(self.start, self.end)
                )
            if abs(_x + x_ - l) < Drawable.comparisonLimit:
                self.__extend, self.extend__ =  0, 0
            elif _x < x_:
                self.__extend, self.extend__ = _x, 0
            else:
                self.__extend, self.extend__ = 0, x_

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
        try:
            return self._length
        except(Exception):
            self._lengthL1 = self.start.distanceL1(self.end)
            return self.start.distanceL1(self.end)

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
        transform = self.reflectionPointmatrix(point)
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
        if not isinstance(o, self.__class__):
            raise TypeError(f"Uncomparable Types. Can't compare {self.__class__} with {type(o)}")
        return(self.start == o.start and self.end == o.end)


    # Output interface
    def __str__(self) -> str:
        """Text return."""
        return f"({self.start.X}, {self.start.Y}), ({self.end.X}, {self.end.Y})"

    def draw(self, axes):
        """Draw plots."""
        a = self.angle()
        c, s = cos(a), sin(a)
        x = (self.start.X - c * self.__extend, self.end.X + c * self.extend__)
        y = (self.start.Y - s * self.__extend, self.end.Y + s * self.extend__)
        axes.plot(x,y)