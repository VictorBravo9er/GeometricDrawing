"""Module for Point."""
from Drawables.Drawable import Drawable
import numpy as np
from math import radians, atan, degrees, sqrt, cos, sin, inf, pi


class Point(Drawable):
    """Description of class."""

    __name__ = "Point"
    def __init__(self):
        """Construct new Point."""
        super().__init__()
        self.X = 0
        self.Y = 0


    # Constructors
    @classmethod
    def fromSection(cls, point1, point2, m:float=1, n:float=1):
        """Point sector using ratio m:n, and points point1 and point2."""
        from Drawables.Line import Line
        tot = m + n
        x = (n * point1.X + m * point2.X) / tot
        y = (n * point1.Y + m * point2.Y) / tot
        return Point.fromCoOrdinates(x, y)

    @classmethod
    def fromPoint(cls, point):
        """Construct new point from existing Point."""
        new = cls()
        new.setPoint(point.X, point.Y)
        return(new)

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
            new._translate(distance * cos(angle), distance * sin(angle))
        #new._translate(distance, 0)
        #new._rotate(point, angle)
        return new


    # Getters and Setters
    def setPoint(self, x:float, y:float):
        """Set x and y."""
        (self.X, self.Y) = (x, y)

    def getPoint(self):
        """Return point coordinates as a tuple."""
        return(self.X, self.Y)


    # Methods
    def slopeTo(self, point):
        """Find slope(directionless) to another point w.r.t. X-axis. -ve allowed."""
        num = (self.Y - point.Y)
        den = (self.X - point.X)
        if den == 0:
            if num == 0:
                return 0
            return inf
        return(num / den)

    def angleTo(self, point):
        """Find angle(radians) to another point w.r.t. X-axis. -ve allowed."""
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

    def distanceTo(self, obj):
        """Distance to/from a Line or a point. Expected arguements: [line], [point]."""
        return sqrt(self.distanceSquared(obj))

    def middlePoint(self, point):
        """Return midPoint of 2 points."""
        return(Point.fromCoOrdinates((self.X + point.X)/2, (self.Y + point.Y)/2))

    def projectionOn(self, line):
        """Return self-projection on a line."""
        return line.projectionOf(self)

    def bisect(self, point):
        """Draws perpendicular bisector between two points."""
        """
        distance = self.distanceTo(point) / 2
        slope = atan(-1 / point.slopeTo(self))
        point = Point.middlePoint(self, point)
        p2 = Point.fromMetrics(slope,-distance, point)
        point = Point.fromMetrics(slope, distance, point)
        """
        from Drawables.Line import Line
        return Line.perpendicularBisector(
            Line.fromPoints(self, point)
            )

    def bisectAnglePoints(self, point1, point2):
        """Bisector of angle AXB."""
        from Drawables.Line import Line
        vLen = (self.distanceTo(point1) + self.distanceTo(point2)) / 2
        angle = (( self.angleTo(point1) + self.angleTo(point2) ) / 2) % (2 * pi)

        end = Point.fromMetrics(angle, vLen, self)
        if Point.orientation(point1, self, end) < 0:
            return Line.fromPoints(self, end)
        end = Point.fromMetrics(angle, -vLen, self)
        return Line.fromPoints(self, end)

    def bisectAngleLine(self, line):
        """Bisector of angle sublended at point from ends of a line."""
        return self.bisectAnglePoints(line.start, line.end)

    def perpendicularTo(self, line):
        """Return a perpendicular from self to a line provided."""
        return line.perpendicularTo(self)

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
            return Circle.fromMetrics(self, self.distanceTo(tangent))
        if isinstance(chord, Line):
            from Drawables.Circle import Circle
            e = self.distanceSquared(chord.start)
            if e != self.distanceSquared(chord.end):
                raise Exception("Can not be constructed")
            return(Circle.fromMetrics(self, sqrt(e)))
        raise Exception("Invalid arguements.")

    def circle(self, radius:float):
        """Create a circle using a centre and a radius."""
        from Drawables.Circle import Circle
        return Circle.fromMetrics(self, radius)


    # Helpers
    def distanceSquared(self, o):
        """Return square of pythagorean distance."""
        from Drawables.Line import Line
        if isinstance(o, Line):
            o = o.projectionOf(self)
        if isinstance(o,Point):
            return(((self.Y - o.Y) ** 2) + ((self.X - o.X) ** 2))
        return inf

    def distanceL1(self, o):
        """L1 distance."""
        from Drawables.Line import Line
        if isinstance(o, Line):
            o = o.projectionOf(self)
        if isinstance(o,Point):
            return( abs(self.Y - o.Y) + abs(self.X - o.X) )
        return inf

    def __add__(self, other):
        """'+' operator overload."""
        new = Point.fromCoOrdinates(self.X + other.X, self.Y + other.Y)
        return new

    def __ne__(self, point):
        """'!=' operator overload."""
        return not self.__eq__(point)

    def __eq__(self, point):
        """'==' operator overload."""
        if abs(self.X - point.X
                ) < Drawable.comparisonLimit and abs(self.Y - point.Y
                ) < Drawable.comparisonLimit:
            return True
        return False

    def _scale(self, sx:float=1, sy:float=1):
        """Scale the point. Has no effect on point itself, but affects the coorginates."""
        if sx == 1 and sy == 1:
            return
        homoCoord = np.array((self.X, self.Y, 1)).reshape(3,1)
        newCoord = np.dot(self.scaleMatrix(sx,sy), homoCoord)
        (self.X, self.Y) = newCoord.reshape(-1)[0:2]#np.round(newCoord[0:2]).astype(int)

    def _normalize(self):
        """Convert everything to int representation."""
        self.X = int(self.X)
        self.Y = int(self.Y)

    def _translate(self, tx:float=0, ty:float=0):
        """Move the point around.""" 
        if tx == 0 and ty == 0:
            return
        homoCoord = np.array((self.X, self.Y, 1)).reshape(3,1)
        newCoord = np.dot(self.translateMatrix(tx,ty), homoCoord)
        (self.X, self.Y) = newCoord.reshape(-1)[0:2]#np.round(newCoord[0:2]).astype(int)

    def _rotate(self, centre=None,angle:float=0):
        """Rotate the point around a centre."""
        if angle == 0:
            return
        if centre is None:
            centre = Point()
        self._translate(centre.X, centre.Y)
        homoCoord = np.array((self.X, self.Y, 1)).reshape(3,1)
        newCoord = np.dot(self.rotateMatrix(angle), homoCoord)
        (self.X, self.Y) = newCoord.reshape(-1)[0:2]#np.round(newCoord[0:2]).astype(int)
        self._translate(-centre.X, -centre.Y)

    def _reflectPoint(self, point):
        """Reflect point about another point."""
        self.X = 2 * point.X - self.X
        self.Y = 2 * point.Y - self.Y

    def _reflectLine(self, line):
        """Reflect point about a line."""
        slope, intercept = line.getMetrics()
        homoCoord = np.array((self.X, self.Y, 1)).reshape(3,1)
        newCoord = np.dot(self.reftectionMatrix(slope,intercept), homoCoord)
        (self.X, self.Y) = newCoord.reshape(-1)[0:2]#np.round(newCoord[0:2]).astype(int)


    # Output interface
    def __str__(self):
        """Text return."""
        return(f"({self.X}, {self.Y})")

    def draw(self, axes):
        """Draw plots."""
        axes.scatter(self.X, self.Y, s=10)