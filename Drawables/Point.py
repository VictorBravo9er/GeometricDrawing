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

    def setPoint(self, x:float, y:float):
        """Set x and y."""
        (self.X, self.Y) = (x, y)

    def angleTo(self, point):
        """Find angle(radians) to another point w.r.t. X-axis. -ve allowed."""
        angle = atan(self.slopeTo(point))
        if self.Y < point.Y:
            return angle
        return(angle * -1)

    def angleFromPoints(self, pointA, pointB):
        """Find angle(radian) subtended on self from A and B. -ve allowed."""
        a1 = self.angleTo(pointA)
        a2 = self.angleTo(pointB)
        angle = a2 - a1
        return(angle)

    def slopeTo(self, point):
        """Find slope(directionless) to another point w.r.t. X-axis. -ve allowed."""
        num = (self.Y - point.Y)
        den = (self.X - point.X)
        if den == 0:
            if num == 0:
                return 0
            return inf
        return(num / den)

    def angleFromLine(self, line):
        """Find angle(radian) subtended on self from endpoints of a line. -ve allowed."""
        return(self.angleFromPoints(line.start, line.end))

    def getPoint(self):
        """Return point coordinates as a tuple."""
        return(self.X, self.Y)
   
    def _scale(self, sx:float=1, sy:float=1):
        """Scale the point. Has no effect on point itself, but affects the coorginates."""
        if sx == 1 and sy == 1:
            return
        homoCoord = np.array((self.X, self.Y, 1)).reshape(3,1)
        newCoord = np.dot(self.scaleMatrix(sx,sy), homoCoord)
        (self.X, self.Y) = newCoord.reshape(-1)[0:2]#np.round(newCoord[0:2]).astype(int)

    def __ne__(self, point):
        """'!=' operator overload."""
        return not self.__eq__(point)

    def __eq__(self, point):
        """'==' operator overload."""
        if self.X == point.X and self.Y == point.Y:
            return True
        return False

    def _translate(self, tx:float=0, ty:float=0):
        """Move the point around.""" 
        if tx == 0 and ty == 0:
            return
        homoCoord = np.array((self.X, self.Y, 1)).reshape(3,1)
        newCoord = np.dot(self.translateMatrix(tx,ty), homoCoord)
        (self.X, self.Y) = newCoord.reshape(-1)[0:2]#np.round(newCoord[0:2]).astype(int)

    def __add__(self, other):
        """'+' operator overload."""
        new = Point.fromCoOrdinates(self.X + other.X, self.Y + other.Y)
        return new

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

    def _normalize(self):
        """Convert everything to int representation."""
        self.X = int(self.X)
        self.Y = int(self.Y)



    @classmethod
    def middlePoint(cls, point1, point2):
        """Return midPoint of 2 points."""
        return(cls.fromCoOrdinates((point1.X + point2.X)/2, (point1.Y + point2.Y)/2))


    def _reflectPoint(self, point):
        """Reflect point about another point."""
        self.X = 2 * point.X - self.X
        self.Y = 2 * point.Y - self.Y

    def distanceSquared(self, o):
        """Return square of pythagorean distance."""
        from Drawables.Line import Line
        if isinstance(o, Line):
            o = o.projectionOf(self)
        if isinstance(o,Point):
            return(((self.Y - o.Y) ** 2) + ((self.X - o.X) ** 2))
        return inf

    def projectionOn(self, line):
        """Return self-projection on a line."""
        return line.projectionOf(self)

    def distanceL1(self, o):
        """L1 distance."""
        from Drawables.Line import Line
        if isinstance(o, Line):
            o = o.projectionOf(self)
        if isinstance(o,Point):
            return( abs(self.Y - o.Y) + abs(self.X - o.X) )
        return inf


    def distanceTo(self, o):
        """Distance to/from a point."""
        return sqrt(self.distanceSquared(o))

    def _reflectLine(self, line):
        """Reflect point about a line."""
        slope, intercept = line.getMetrics()
        homoCoord = np.array((self.X, self.Y, 1)).reshape(3,1)
        newCoord = np.dot(self.reftectionMatrix(slope,intercept), homoCoord)
        (self.X, self.Y) = newCoord.reshape(-1)[0:2]#np.round(newCoord[0:2]).astype(int)

    def bisectAround(self, pointA, pointB):
        """Bisector of angle AXB."""
        from Drawables.Line import Line
        vLen = (self.distanceTo(pointA) + self.distanceTo(pointB)) / 2
        angle = ( self.angleTo(pointA) + self.angleTo(pointB) ) / 2
        bisector = Line.fromMetrics(angle, vLen, self)
        return bisector

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

    def circleAroundChord(self, chord):
        """Create a circle using a centre and a chord."""
        from Drawables.Circle import Circle
        e = self.distanceSquared(chord.start)
        if e != self.distanceSquared(chord.end):
            raise Exception("Can not construct")
        return(Circle.fromMetrics(self, sqrt(e)))

    def circleAroundRadius(self, radius:float):
        """Create a circle using a centre and a radius."""
        from Drawables.Circle import Circle
        return Circle.fromMetrics(self, radius)

    def perpendicularTo(self, line):
        """Return a perpendicular from self to a line provided."""
        return line.perpendicularTo(self)

    def __str__(self):
        """Text return."""
        return(f"{self.__name__}: ({self.X}, {self.Y})")

    def draw(self, axes):
        """Draw plots."""
        axes.scatter(self.X, self.Y, s=10)