"""Module for Point."""
from Drawables.Line import Line
from Drawables.Drawable import Drawable
import numpy as np
from math import radians, atan, degrees, sqrt, cos, sin, inf, pi


class Point(Drawable):
    """Description of class."""

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
        newCoord:np.array = np.dot(self.scaleMatrix(sx,sy), homoCoord)
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
        newCoord:np.array = np.dot(self.translateMatrix(tx,ty), homoCoord)
        (self.X, self.Y) = newCoord.reshape(-1)[0:2]#np.round(newCoord[0:2]).astype(int)

    def __add__(self, other):
        """'+' operator overload."""
        new = Point.fromCoOrdinates(self.X + other.X, self.Y + other.Y)
        return new

    def _rotate(self, centre=None,angle:float=0):
        """Rotate the point around a centre."""
        if angle == 0:
            return
        if centre == None:
            centre = Point()
        self._translate(centre.X, centre.Y)
        homoCoord = np.array((self.X, self.Y, 1)).reshape(3,1)
        newCoord:np.array = np.dot(self.rotateMatrix(angle), homoCoord)
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

    def squaredDistance(self, point):
        """Return square of pythagorean distance."""
        return(((self.Y - point.Y) ** 2) + ((self.X - point.X) ** 2))

    def projectionOn(self, line):
        """Return self-projection on a line."""
        return line.projectionOf(self)

    def distanceToLine(self, line):
        """Distance(perpendicular) from a line."""
        return self.distanceToPoint(line.projectionOf(self))

    def distanceL1(self, point):
        """L1 distance."""
        return( abs(self.Y - point.Y) + abs(self.X - point.X) )

    def distanceToPoint(self, point):
        """Distance to/from a point."""
        return sqrt(self.squaredDistance(point))

    def _reflectLine(self, line):
        """Reflect point about a line."""
        slope, intercept = line.getMetrics()
        homoCoord = np.array((self.X, self.Y, 1)).reshape(3,1)
        newCoord:np.array = np.dot(self.reftectionMatrix(slope,intercept), homoCoord)
        (self.X, self.Y) = newCoord.reshape(-1)[0:2]#np.round(newCoord[0:2]).astype(int)

    def bisectAround(self, pointA, pointB):
        """Bisector of angle AXB."""
        from Drawables.Line import Line
        angle = self.angleFromPoints(pointA, pointB)
        vLen = (self.distanceToPoint(pointA) + self.distanceToPoint(pointB)) / 2
        bisector = Line.fromMetrics(angle/2, vLen, self)
        return bisector

    def lineToPoint(self, point):
        from Drawables.Line import Line
        return(Line.fromPoints(self, point))

    def lineTo(self, angle:float, distance:float):
        from Drawables.Line import Line
        return(Line.fromMetrics(angle, distance, self))

    def triangleTo(self, line):
        from Drawables.Triangle import Triangle
        Triangle.fromLine(line, self)

    def circleAroundChord(self, chord, distance:float):
        from Drawables.Circle import Circle
        e = self.squaredDistance(chord.start)
        if e != self.squaredDistance(chord.end):
            raise Exception("Can not construct")
        return(Circle.fromMetrics(self, sqrt(e)))

    def circleAroundRadius(self, radius:float):
        from Drawables.Circle import Circle
        return Circle.fromMetrics(self, radius)

    def perpendicularTo(self, line):
        return line.perpendicularTo(self)

    def __str__(self):
        return(f"Point: ({self.X}, {self.Y})")