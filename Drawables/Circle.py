from math import pi, sqrt, degrees, radians
from Drawables.Drawable import Drawable

class Circle(Drawable):
    """description of class"""

    def __init__(self):
        super().__init__()

    def setCentre(self, point):
        self.centre = point

    def setRadius(self, radius:float):
        self.radius = radius

    @classmethod
    def fromMetrics(cls, point, radius:float):
        new = cls()
        new.setCentre(point)
        new.setRadius(radius)
        return new

    @classmethod
    def fromCircle(cls, circle):
        from Drawables.Point import Point
        point = Point.fromPoint(circle.centre)
        new = cls.fromMetrics(point, circle.radius)
        return new

    def area(self):
        try:
            return self._area
        except(Exception):
            self._area = pi * (self.radius) ** 2
            return self._area


    def centroid(self):
        return self.radius

    def diameterLength(self):
        return(2 * self.radius)

    def diameterAlongPoint(self, point):
        from Drawables.Point import Point
        from Drawables.Line import Line
        newPoint = Point.fromPoint(point)
        newPoint._reflectPoint(self.centre)
        diameter = Line.fromPoints(point, newPoint)
        return diameter

    def diameterAlongSlope(self, slope:float):
        from Drawables.Point import Point
        point = Point.fromMetrics(slope, self.radius, self.centre)
        diameter = self.diameterAlongPoint(point)
        return diameter

    def commonChord(self, circle):
        from Drawables.Point import Point
        c1 = Point.fromPoint(self.centre)
        (tx, ty) = (c1.X, c1.Y)
        c1._translate(-tx, -ty)
        c2 = Point.fromPoint(circle.centre)
        c2._translate(-tx, -ty)
        angle = c1.angleFromPoints(c2, Point.fromCoOrdinates(2, 0))
        c2._rotate(self.centre, angle)
        R = self.radius
        R = R ** 2
        d = c2.X
        d = d ** 2
        r = circle.radius
        r = r ** 2
        x = (d - r + R) / (2 * d)
        y = sqrt(R - (x ** 2))
        p1 = Point.fromCoOrdinates(x, y)
        p2 = Point.fromCoOrdinates(x,-y)
        angle *= -1
        p1._rotate(self.centre, angle)
        p2._rotate(self.centre, angle)
        p1._translate(tx, ty)
        p2._translate(tx, ty)
        from Drawables.Line import Line
        return(Line.fromPoints(p1, p2))