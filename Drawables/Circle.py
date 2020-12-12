"""Module for Circle."""
from math import  pi, sqrt, degrees, radians
from Drawables.Drawable import Drawable
from Drawables.Arc import Arc
import numpy as np
from numpy import sin,cos

class Circle(Arc):
    """Description of class."""

    def __init__(self):
        """Cunstruct a default, empty container."""
        super().__init__(None, -1)
        from Drawables.Point import Point


    # Constructors
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


    # Getters and Setters
    def setCentre(self, point):
        """Set centre."""
        self.centre = point

    def setRadius(self, radius:float):
        """Set radius."""
        self.radius = radius


    # Methods
    def area(self):
        """Calculate area."""
        try:
            return self._area
        except(Exception):
            self._area = pi * (self.radius) ** 2
            return self._area

    def centroid(self):
        """Centroid is the radius itself."""
        return self.centre

    def diameterLength(self):
        """Diameter is twice the radius."""
        return(2 * self.radius)

    def diameterAlongPoint(self, point):
        """Return a diameter along the direction of a certain point."""
        from Drawables.Point import Point
        from Drawables.Line import Line
        if self.radius != Point.distanceTo(self.centre, point):
            point = Point.fromMetrics(
                    Point.angleTo(self.centre, point),
                    self.radius, self.centre
                )
        newPoint = Point.fromMetrics(
                Point.angleTo(self.centre, point),
                -self.radius, self.centre
            )
        return Line.fromPoints(point, newPoint)

    def diameterAlongSlope(self, angle:float):
        """Return a diameter along a certain direction."""
        from Drawables.Point import Point
        point = Point.fromMetrics(angle, self.radius, self.centre)
        diameter = self.diameterAlongPoint(point)
        return diameter

    def commonChord(self, circle):
        """Calculate common chord with another circle.""" 
        from Drawables.Point import Point
        (tx, ty) = (self.centre.X, self.centre.Y)
        origin = Point.fromCoOrdinates(0, 0)
        p1 = origin
        p2 = Point.fromPoint(circle.centre)
        p2._translate(-tx, -ty)
        angle = self.centre.angleTo(circle.centre)
        p2._rotate(self.centre, -angle)
        R1 = self.radius ** 2
        X2 = p2.X
        R2 = circle.radius ** 2
        x = ((X2 ** 2) - R2 + R1) / (2 * X2)
        y = sqrt(R1 - (x ** 2))
        print(p2.X , p1.distanceTo(p2), p2.Y, end="\n\n")
        p1 = Point.fromCoOrdinates(x, y)
        p2 = Point.fromCoOrdinates(x,-y)
        p1._rotate(origin, angle)
        p2._rotate(origin, angle)
        p1._translate(tx, ty)
        p2._translate(tx, ty)
        from Drawables.Line import Line
        return(Line.fromPoints(p1, p2))


    # Output interface
    def __str__(self) -> str:
        """Text return."""
        return(f"{Circle.__name__} has centre {self.centre} and radius {self.radius}")
