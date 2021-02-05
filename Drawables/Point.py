"""Module for Point."""
from Drawables.Drawable import Drawable
import numpy as np
from math import inf, pi, atan, sqrt, cos, sin

class Point(Drawable):
    """Description of class."""

    def __init__(self):
        """Construct new Point."""
        super().__init__()
        self.X = 0.0
        self.Y = 0.0


    # Constructors
    @classmethod
    def fromSection(cls, point1, point2, m:float=1, n:float=1):
        """Point that divides two points in ratio m:n."""
        tot = m + n
        x = (n * point1.X + m * point2.X) / tot
        y = (n * point1.Y + m * point2.Y) / tot
        return cls.fromCoOrdinates(x, y)

    @classmethod
    def fromPoint(cls, point):
        """Copy from another point."""
        new = cls()
        if isinstance(point, cls):
            new.setPoint(point.X, point.Y)
            return(new)
        raise TypeError(
            f"TypeError:\tExpected {cls.__name__}, received {type(point).__name__}."
        )

    @classmethod
    def fromCoOrdinates(cls, x:float, y:float):
        """Point using point Coordinates."""
        new = cls()
        new.setPoint(x, y)
        return(new)

    @classmethod
    def fromMetrics(cls, angle:float, distance:float, point):
        """Point along an angle at a distance from another point."""
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
        if isinstance(x,(float, int)) and isinstance(y,(float,int)):
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
        """Find slope to another point."""
        num:float = (self.Y - point.Y)
        den:float = (self.X - point.X)
        if den == 0:
            if num == 0:
                return 0.0
            return inf
        return(num / den)

    def angleTo(self, point):
        """Find angle to another point."""
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
        """Find angle subtended from two points."""
        a1 = self.angleTo(point1)
        a2 = self.angleTo(point2)
        angle = (a2 - a1) % (2* pi)
        return(angle)

    def angleFromLine(self, line):
        """Find angle subtended from endpoints of a line."""
        return(self.angleFromPoints(line.start, line.end))

    def distanceTo(self, line=..., point=...):
        """Distance to/from a Line or a point."""
        return sqrt(
            self.distanceSquared(line=line, point=point)
            )

    def middlePoint(self, point):
        """Mid point of two points."""
        return(Point.fromCoOrdinates((self.X + point.X)/2, (self.Y + point.Y)/2))

    def projectionOn(self, line):
        """Projection on a line."""
        return line.projectionOf(self)

    def bisect(self, point):
        """Draws perpendicular bisector with respect to another point."""
        from Drawables.Line import Line
        return Line.perpendicularBisector(
            Line.fromPoints(self, point)
            )

    def bisectAnglePoints(
        self, point1, point2,
        bidirectional:bool=False
    ):
        """Bisector of angle subtended by two other points."""
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
        """Bisector of angle sublended from ends of a line."""
        return self.bisectAnglePoints(line.start, line.end)

    def perpendicularTo(self, line):
        """Perpendicular to a line provided."""
        from Drawables.Line import Line
        return Line.perpendicularFrom(line, self)

    def lineToPoint(self, point):
        """Line to another point."""
        from Drawables.Line import Line
        return(Line.fromPoints(self, point))

    def lineTo(self, angle:float, distance:float):
        """Line along a direction(angle) of given length."""
        from Drawables.Line import Line
        return(Line.fromMetrics(angle, distance, self))


    # Helpers
    def extendLimits(self, bound:float=1):
        """Redefine boundaries."""
        (x,y) = self.getPoint()
        if Drawable._minX > x - bound:
            Drawable._minX = x - bound
        if Drawable._maxX < x + bound:
            Drawable._maxX = x + bound
        if Drawable._minY > y - bound:
            Drawable._minY = y - bound
        if Drawable._maxY < y + bound:
            Drawable._maxY = y + bound

    def distanceSquared(self, line=..., point=...):
        """Return square of pythagorean distance."""
        from Drawables.Line import Line
        if isinstance(line, Line):
            point = line.projectionOf(self, False)
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
            point = line.projectionOf(self, False)
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
        ) < Drawable._comparisonLimit and abs(
            self.Y - point.Y
        ) < Drawable._comparisonLimit:
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
        transform = self.reflectionPointMatrix(point)
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