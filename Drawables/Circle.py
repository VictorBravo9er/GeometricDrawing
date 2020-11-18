"""Module for Circle."""
from math import pi, sqrt, degrees, radians
from Drawables.Drawable import Drawable

class Circle(Drawable):
    """Description of class."""

    __name__ = "Circle"
    def __init__(self):
        """Cunstruct a default, empty container."""
        super().__init__()
        from Drawables.Point import Point
        self.centre:Point
        self.radius:float

    def setCentre(self, point):
        """Set centre."""
        self.centre = point

    def setRadius(self, radius:float):
        """Set radius."""
        self.radius = radius

    @classmethod
    def fromMetrics(cls, point, radius:float):
        """Construct a circle using a centre and a radius."""
        new = cls()
        new.setCentre(point)
        new.setRadius(radius)
        return new

    @classmethod
    def fromDiameter(cls, diameter):
        """Draw Circle around a given diameter."""
        new = cls()
        from Drawables.Point import Point
        new.setCentre(Point.middlePoint(diameter.start, diameter.end))
        new.setRadius(diameter.length / 2)

    @classmethod
    def fromCircle(cls, circle):
        """Copy another circle."""
        from Drawables.Point import Point
        point = Point.fromPoint(circle.centre)
        new = cls.fromMetrics(point, 0 + circle.radius)
        return new

    def area(self):
        """Calculate area."""
        try:
            return self._area
        except(Exception):
            self._area = pi * (self.radius) ** 2
            return self._area


    def centroid(self):
        """Centroid is the radius itself."""
        return self.radius

    def diameterLength(self):
        """Diameter is twice the radius."""
        return(2 * self.radius)

    def diameterAlongPoint(self, point):
        
        """Return a diameter along the direction of a certain point."""
        from Drawables.Point import Point
        from Drawables.Line import Line
        newPoint = Point.fromPoint(point)
        newPoint._reflectPoint(self.centre)
        diameter = Line.fromPoints(point, newPoint)
        return diameter

    def diameterAlongPointOnCircle(self, point):
        """Return a diameter along the direction of a certain point on circle."""
        from Drawables.Point import Point
        from Drawables.Line import Line
        newPoint = Point.fromPoint(point)
        newPoint._reflectPoint(self.centre)
        diameter = Line.fromPoints(point, newPoint)
        return diameter

    def diameterAlongSlope(self, slope:float):
        """Return a diameter along a certain direction."""
        from Drawables.Point import Point
        point = Point.fromMetrics(slope, self.radius, self.centre)
        diameter = self.diameterAlongPoint(point)
        return diameter

    def commonChord(self, circle):
        """Calculate common chord with another circle.""" 
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

    def __str__(self) -> str:
        """Text return."""
        return(f"{self.__name__} has centre {self.centre} and radius {self.radius}")