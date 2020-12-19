"""Module for Point."""
from Drawables.Drawable import Drawable
import numpy as np
from math import inf, pi, atan, sqrt, cos, sin


class Point(Drawable):
    """Description of class."""

    def __init__(self):
        """Construct new Point."""
        super().__init__()
        self.X = 0
        self.Y = 0


    # Constructors
    @classmethod
    def fromSection(cls, point1, point2, m:float=1, n:float=1):
        """Point sector using ratio m:n, and points point1 and point2."""
        tot = m + n
        x = (n * point1.X + m * point2.X) / tot
        y = (n * point1.Y + m * point2.Y) / tot
        return cls.fromCoOrdinates(x, y)

    @classmethod
    def fromPoint(cls, point):
        """Construct new point from existing Point."""
        new = cls()
        if isinstance(point, cls):
            new.setPoint(point.X, point.Y)
            return(new)
        raise TypeError(
            f"TypeError:\tExpected {cls.__name__}, received {type(point).__name__}."
        )

    @classmethod
    def fromCoOrdinates(cls, x:float, y:float):
        """Construct new Point using point Coordinates."""
        new = cls()
        new.setPoint(x, y)
        return(new)

    @classmethod
    def fromMetrics(cls, angle:float, distance:float, point):
        """Construct point using some Metrics. Angle in radians."""
        new = cls.fromPoint(point)
        if distance != 0:
            try:
                new._translate(distance * cos(angle), distance * sin(angle))
            except:
                raise TypeError(
                    "TypeError:\tExpected int, received "+
                    f"{type(angle).__name__} and {type(distance).__name__}"
                )
        return new


    # Getters and Setters
    def setPoint(self, x:float, y:float):
        """Set x and y."""
        if isinstance(x,float) and isinstance(y,float):
            (self.X, self.Y) = (x, y)
        else:
            raise TypeError(
                "TypeError:\tExpected: (float, float), "+
                f"received: ({type(x).__name__}, {type(y).__name__})"
            )

    def getPoint(self):
        """Return point coordinates as a tuple."""
        return(self.X, self.Y)


    # Methods
    def slopeTo(self, point):
        """Find slope(directionless) to another point w.r.t. X-axis. -ve allowed."""
        num:float = (self.Y - point.Y)
        den:float = (self.X - point.X)
        if den == 0:
            if num == 0:
                return 0.0
            return inf
        return(num / den)

    def angleTo(self, point):
        """Find angle(radians) to another point w.r.t. X-axis. -ve allowed."""
        if not isinstance(point, Point):
            raise TypeError(
                f"TypeError:\tExpected: Point, received: {type(point).__name__}"
            )
        slope = self.slopeTo(point)
        angle = atan(slope)
        if self.X < point.X:
            return angle % (2 * pi)
        if slope == inf and self.Y < point.Y:
            return pi / 2
        return((angle + pi) % (2 * pi))

    def angleFromPoints(self, point1, point2):
        """Find angle(radian) subtended on self from A and B. -ve allowed."""
        a1 = self.angleTo(point1)
        a2 = self.angleTo(point2)
        angle = (a2 - a1) % (2* pi)
        return(angle)

    def angleFromLine(self, line):
        """Find angle(radian) subtended on self from endpoints of a line. -ve allowed."""
        return(self.angleFromPoints(line.start, line.end))

    def distanceTo(self, line=..., point=...):
        """Distance to/from a Line or a point. Expected arguements: [line], [point]."""
        return sqrt(
            self.distanceSquared(line=line, point=point)
            )

    def middlePoint(self, point):
        """Return midPoint of 2 points."""
        return(Point.fromCoOrdinates((self.X + point.X)/2, (self.Y + point.Y)/2))

    def projectionOn(self, line):
        """Return self-projection on a line."""
        return line.projectionOf(self)

    def bisect(self, point):
        """Draws perpendicular bisector between two points."""
        from Drawables.Line import Line
        return Line.perpendicularBisector(
            Line.fromPoints(self, point)
            )

    def bisectAnglePoints(
        self, point1, point2,
        bidirectional:bool=False
    ):
        """Bisector of angle AXB."""
        from Drawables.Line import Line
        vLen = (self.distanceTo(point=point1) + self.distanceTo(point=point2)) / 2
        angle = (( self.angleTo(point1) + self.angleTo(point2) ) / 2) % (2 * pi)
        start = Point.fromMetrics(angle, vLen, self)
        end = Point.fromMetrics(angle, -vLen, self)
        if bidirectional:
            return Line.fromPoints(start, end)
        if Point.orientation(point1, self, start) < 0:
            return Line.fromPoints(self, start)
        return Line.fromPoints(self, end)

    def bisectAngleLine(self, line):
        """Bisector of angle sublended at point from ends of a line."""
        return self.bisectAnglePoints(line.start, line.end)

    def perpendicularTo(self, line):
        """Return a perpendicular from self to a line provided."""
        from Drawables.Line import Line
        return Line.perpendicularFrom(line, self)

    def lineToPoint(self, point):
        """Return a line from current point to another point."""
        from Drawables.Line import Line
        return(Line.fromPoints(self, point))

    def lineTo(self, angle:float, distance:float):
        """Return a line using certain metrics."""
        from Drawables.Line import Line
        return(Line.fromMetrics(angle, distance, self))

    def triangleTo(self, line):
        """Draw a triangle, provided a side of the triangle."""
        from Drawables.Triangle import Triangle
        return Triangle.fromLine(line, self)

    def circleFrom(self, chord=None, tangent=None):
        """Create a circle using a centre and a chord\
            or a tangent."""
        from Drawables.Line import Line
        if isinstance(tangent, Line):
            from Drawables.Circle import Circle
            return Circle.fromMetrics(self, self.distanceTo(line=tangent))
        if isinstance(chord, Line):
            from Drawables.Circle import Circle
            e = self.distanceSquared(chord.start)
            if e != self.distanceSquared(chord.end):
                raise Exception("Can not be constructed")
            return(Circle.fromMetrics(self, sqrt(e)))
        raise TypeError(
            "TypeError:\tExpected: Line, received: "+
            f"{type(chord).__name__} and {type(tangent).__name__}"
        )

    def circle(self, radius:float):
        """Create a circle using a centre and a radius."""
        from Drawables.Circle import Circle
        return Circle.fromMetrics(self, radius)


    # Helpers
    def distanceSquared(self, line=..., point=...):
        """Return square of pythagorean distance."""
        from Drawables.Line import Line
        if isinstance(line, Line):
            point = line.projectionOf(self)
        if isinstance(point, Point):
            return float(
                ((self.Y - point.Y) ** 2) + ((self.X - point.X) ** 2)
                )
        raise TypeError(
            "TypeError:\tExpected: Line or Point, received: "+
            f"{type(line).__name__} or {type(point).__name__}"
        )

    def distanceL1(self, line=...,point=...):
        """L1 distance."""
        from Drawables.Line import Line
        if isinstance(line, Line):
            point = line.projectionOf(self)
        if isinstance(point, Point):
            return( abs(self.Y - point.Y) + abs(self.X - point.X) )
        raise TypeError(
            "TypeError:\tExpected: Line or Point, received: "+
            f"{type(line).__name__} or {type(point).__name__}"
        )

    def __add__(self, other):
        """'+' operator overload."""
        if isinstance(other, Point):
            return Point.fromCoOrdinates(self.X + other.X, self.Y + other.Y)
        raise TypeError(
            f"TypeError:\tExpected: Point, received: {type(other).__name__}"
        )

    def __sub__(self, other):
        """'+' operator overload."""
        if isinstance(other, Point):
            return Point.fromCoOrdinates(self.X - other.X, self.Y - other.Y)
        raise TypeError(
            f"TypeError:\tExpected: Point, received: {type(other).__name__}"
        )

    def __ne__(self, point):
        """'!=' operator overload."""
        return not self.__eq__(point)

    def __eq__(self, point):
        """'==' operator overload."""
        if not isinstance(point, Point):
            raise TypeError(f"TypeError:\tExpected: Point, received: {type(point).__name__}")
        if abs(
            self.X - point.X
        ) < Drawable.comparisonLimit and abs(
            self.Y - point.Y
        ) < Drawable.comparisonLimit:
            return True
        return False

    def _normalize(self):
        """Convert everything to int representation."""
        self.X = float(self.X)
        self.Y = float(self.Y)

    def _scale(self, sx:float=1, sy:float=1, point=...):
        """Scale the point. Has no effect on point itself, but affects the coorginates."""
        if sx == 1 and sy == 1:
            return
        transform = self.scaleMatrix(sx, sy, point)
        self._applyTransform(transform)

    def _translate(self, tx:float=0, ty:float=0):
        """Move the point around.""" 
        if tx == 0 and ty == 0:
            return
        transform = self.translateMatrix(tx,ty)
        self._applyTransform(transform)

    def _rotate(self, centre=...,angle:float=0):
        """Rotate the point around a centre."""
        if angle == 0:
            return
        transform = self.rotateMatrix(angle, centre)
        self._applyTransform(transform)

    def _reflectPoint(self, point):
        """Reflect point about another point."""
        transform = self.reflectionPointmatrix(point)
        self._applyTransform(transform)

    def _reflectLine(self, line):
        """Reflect point about a line."""
        slope, intercept = line.getMetrics()
        transform = self.reftectionLineMatrix(slope,intercept)
        self._applyTransform(transform)

    def _applyTransform(self, transform):
        homoCoord = np.array((self.X, self.Y, 1)).reshape(3,1)
        homoCoord = np.dot(transform, homoCoord)
        (self.X, self.Y) = [float(x) for x in np.reshape(homoCoord, -1)[0:2]]


    # Output interface
    def __str__(self):
        """Text return."""
        return(f"({self.X}, {self.Y})")

    def draw(self, axes):
        """Draw plots."""
        axes.scatter(self.X, self.Y, s=10)