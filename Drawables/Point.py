from Drawables.Line import Line
from Drawables.Drawable import Drawable
import numpy as np
from math import radians, atan, degrees, sqrt, cos, sin, inf


class Point(Drawable):
    """description of class"""

    def __init__(self):
        super().__init__()
        self.X = 0
        self.Y = 0

    @classmethod
    def fromPoint(cls, point):
        new = cls()
        new.setPoint(point.X, point.Y)
        return(new)
        
    @classmethod
    def fromCoOrdinates(cls, x:float, y:float):
        new = cls()
        new.setPoint(x, y)
        return(new)

    @classmethod
    def fromMetrics(cls, angle:float, distance:float, point):
        new = cls.fromPoint(point)
        angle2 = radians(angle)
        new._translate(distance * sin(angle2), distance * cos(angle2))
        #new._rotate(point, angle)
        return new

    def setPoint(self, x:float, y:float):
        (self.X, self.Y) = (x, y)

    def angleFromPoints(self, pointA, pointB):
        m1 = self.slopeTo(pointA)
        m2 = self.slopeTo(pointB)
        m = ((m2 - m1) / (1 + m1 * m2))
        return(degrees(atan(m)))

    def slopeTo(self, point):
        den = (self.X - point.X)
        if den == 0:
            return inf
        m = (self.Y - point.Y) / den
        return(m)

    def angleFromLine(self, line):
        return(self.angleFromPoints(line.start, line.end))

    def getPoints(self):
        return(self.X, self.Y)
   
    def _scale(self, sx:float=1, sy:float=1):
        if sx == 1 and sy == 1:
            return
        homoCoord = np.array((self.X, self.Y, 1)).reshape(3,1)
        newCoord:np.array = np.dot(self.scaleMatrix(sx,sy), homoCoord)
        (self.X, self.Y) = newCoord.reshape(-1)[0:2]#np.round(newCoord[0:2]).astype(int)

    def __ne__(self, point):
        return not self.__eq__(point)

    def __eq__(self, point):
        if self.X == point.X and self.Y == point.Y:
            return True
        return False

    def _translate(self, tx:float=0, ty:float=0):
        if tx == 0 and ty == 0:
            return
        homoCoord = np.array((self.X, self.Y, 1)).reshape(3,1)
        newCoord:np.array = np.dot(self.translateMatrix(tx,ty), homoCoord)
        (self.X, self.Y) = newCoord.reshape(-1)[0:2]#np.round(newCoord[0:2]).astype(int)

    def __add__(self, other):
        new = Point.fromCoOrdinates(self.X + other.X, self.Y + other.Y)
        return new

    def _rotate(self, centre=None,angle:float=0):
        if angle == 0:
            return
        if not isinstance(centre, Point):
            centre = Point()
        self._translate(centre.X, centre.Y)
        angle = radians(angle)
        homoCoord = np.array((self.X, self.Y, 1)).reshape(3,1)
        newCoord:np.array = np.dot(self.rotateMatrix(angle), homoCoord)
        (self.X, self.Y) = newCoord.reshape(-1)[0:2]#np.round(newCoord[0:2]).astype(int)
        self._translate(-centre.X, -centre.Y)

    def _normalize(self):
        self.X = int(self.X)
        self.Y = int(self.Y)



    @staticmethod
    def middlePoint(point1, point2):
        return(Point.fromCoOrdinates((point1.X + point2.X)/2, (point1.Y + point2.Y)/2))


    def _reflectPoint(self, point):
        self.X = 2 * point.X - self.X
        self.Y = 2 * point.Y - self.Y

    def squaredDistance(self, point):
        return(((self.Y - point.Y) ** 2) + ((self.X - point.X) ** 2))

    def lengthTo(self, point):
        return sqrt(self.squaredDistance(point))

    def projectionOn(self, line):
        return line.projectionOf(self)

    def distanceToLine(self, line):
        return self.distanceToPoint(line.projectionOf(self))

    def distanceToPoint(self, point):
        return sqrt(((self.Y - point.Y) ** 2) + ((self.X - point.X) ** 2))

    def _reflectLine(self, angle:float=0, intercept:float=0):
        homoCoord = np.array((self.X, self.Y, 1)).reshape(3,1)
        newCoord:np.array = np.dot(self.reftectionMatrix(angle,intercept), homoCoord)
        (self.X, self.Y) = newCoord.reshape(-1)[0:2]#np.round(newCoord[0:2]).astype(int)

    def bisectAround(self, pointA, pointB):
        from Drawables.Line import Line
        angle = self.angleFromPoints(pointA, pointB)
        vLen = (self.lengthTo(pointA) + self.lengthTo(pointB)) / 2
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