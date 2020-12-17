"""Module for Circle."""
from math import pi
from Drawables.Drawable import Drawable
from Drawables.Arc import Arc
from numpy import sqrt

class Circle(Arc):
    """Description of class."""

    def __init__(self):
        """Cunstruct a default, empty container."""
        super().__init__(None, -1)


    # Constructors
    @classmethod
    def fromMetrics(cls, centre, radius:float):
        """Construct a circle using a centre and a radius."""
        new = cls()
        new.setCentre(centre)
        new.setRadius(radius)
        return new

    @classmethod
    def fromDiameter(cls, diameter):
        """Draw Circle around a given diameter."""
        from Drawables.Line import Line
        if isinstance(diameter, Line):
            new = cls()
            from Drawables.Point import Point
            new.setCentre(Point.middlePoint(diameter.start, diameter.end))
            new.setRadius(Line.length(diameter) / 2)
            return new
        raise Exception("Invalid arguement.")

    @classmethod
    def fromCircle(cls, self):
        """Copy another circle."""
        from Drawables.Point import Point
        new = cls.fromMetrics(
            Point.fromPoint(self.centre),
            self.radius+0
            )
        return new


    # Getters and Setters
    def setCentre(self, point):
        """Set centre."""
        self.centre = point

    def setRadius(self, radius:float):
        """Set radius."""
        self.radius = radius

    def getRadius(self):
        """Get radius."""
        return self.radius

    def getCentre(self):
        """Get the radius itself."""
        return self.centre


    # Methods
    def area(self):
        """Calculate area."""
        return pi * (self.radius) ** 2

    def diameterLength(self):
        """Diameter is twice the radius."""
        return(2 * self.radius)

    def diameterAlongPoint(self, point):
        """Return a diameter along the direction of a certain point."""
        from Drawables.Point import Point
        from Drawables.Line import Line
        if self.radius != Point.distanceTo(self.centre, point=point):
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
        X2 = Point.distanceTo(circle.centre, point=self.centre)
        R1 = self.radius
        R2 = circle.radius
        if R1 + R2 < X2 or\
            R1 - X2 > R2 or\
            R2 - X2 > R1:
            raise Exception("Circles not intersecting.")
        (tx, ty) = (self.centre.X, self.centre.Y)
        origin = Point.fromCoOrdinates(0, 0)
        p1 = origin
        p2 = Point.fromPoint(circle.centre)
        p2._translate(-tx, -ty)
        angle = self.centre.angleTo(circle.centre)
        p2._rotate(self.centre, -angle)
        R1 = R1 ** 2
        R2 = R2 ** 2
        x = ((X2 ** 2) - R2 + R1) / (2 * X2)
        y = sqrt(R1 - (x ** 2))
        if y < Drawable.comparisonLimit:
            y = (X2) * 0.5
        p1 = Point.fromCoOrdinates(x, y)
        p2 = Point.fromCoOrdinates(x,-y)
        p1._rotate(origin, angle)
        p2._rotate(origin, angle)
        p1._translate(tx, ty)
        p2._translate(tx, ty)
        from Drawables.Line import Line
        return(Line.fromPoints(p1, p2))

    def tangentAt(self, point=None, angle:float=None):
        """Draw a tangent on circle, with radius along a point, or an angle. Expected arguements: [point], [angle]."""
        from Drawables.Point import Point
        from Drawables.Line import Line
        status = True
        if isinstance(point, Point):
            status = Point.distanceTo(self.centre, point=point) != self.radius
            angle = 0
            if status:
                angle = self.centre.angleTo(point)
        if isinstance(angle, float) or isinstance(angle, int):
            if status:
                point = Point.fromMetrics(angle, self.radius, self.centre)
            return Line.fromPoints(self.centre, point).perpendicularAt(point)


    # Output interface
    def __str__(self) -> str:
        """Text return."""
        return(f"Centre {self.centre}, radius {self.radius}")
