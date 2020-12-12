"""Module Line."""
from numpy.core.numeric import ComplexWarning
from Drawables.Drawable import Drawable
import numpy as np
from math import inf, pi, radians, degrees, atan, sin, sqrt, cos


class Line(Drawable):
    """Description of class."""

    __name__ = "Line"
    def __init__(self):
        """Construct default."""
        from Drawables.Point import Point
        super().__init__()
        # Drawable.__init__(self)
        self.start:Point
        self.end:Point


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
            print(m1, m2)
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
        """Sector of line in a ratio."""
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
        return self.sector(m,n)

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

    def circleAround(self, chordDistance:float=None, tangentPoint=None, chordPoint=None):
        """Draw circle with line as diameter, chord or tangent."""
        from Drawables.Point import Point
        if chordPoint is None and tangentPoint is None and chordDistance is None:
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
        elif isinstance(tangentPoint, Point):
            return Point.circleFrom(tangentPoint, tangent=self)
        elif isinstance(chordPoint, Point):
            return Point.circleFrom(chordPoint, chord=self)
        raise Exception("invalid arguements.")

    def square(self, direction:str="up"):
        pass

    def rectangle(self, sideLength:float, direction:str="up"):
        pass


    # Helpers
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

    def _scale(self, sx:float=1, sy:float=1):
        self.start._scale(sx, sy)
        self.end._scale(sx, sy)

    def _translate(self, tx:float=0, ty:float=0):
        self.start._translate(tx, ty)
        self.end._translate(tx, ty)

    def _rotate(self, centre=None,angle:float=0):
        from Drawables.Point import Point
        if not isinstance(centre, Point):
            centre = Point()
        self.start._rotate(centre, angle)
        self.end._rotate(centre, angle)

    def _reflectPoint(self, point):
        self.start._reflectPoint(point)
        self.end._reflectPoint(point)

    def _reflectLine(self, line):
        self.start._reflectLine(line)
        self.end._reflectLine(line)

    def __ne__(self, o) -> bool:
        """'!=' operator overload."""
        return not self == o

    def __eq__(self, o) -> bool:
        """'==' operator overload."""
        return(self.start == o.start and self.end == o.end)


    # Output interface
    def __str__(self) -> str:
        """Text return."""
        return f"({self.start.X}, {self.start.Y}), ({self.end.X}, {self.end.Y})"

    def draw(self, axes):
        """Draw plots."""
        x = self.start.X, self.end.X
        y = self.start.Y, self.end.Y
        axes.plot(x,y)