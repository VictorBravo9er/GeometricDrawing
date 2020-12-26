"""Module for Circle."""
from Drawables.randoms import *
from Drawables.Drawable import Drawable
from Drawables.Arc import Arc
from math import pi, sqrt

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
        raise TypeError(
            "TypeError:\tExpected: Line, received: "+
            f"{type(diameter).__name__}"
        )

    @classmethod
    def fromCircle(cls, circle):
        """Copy another circle."""
        from Drawables.Point import Point
        new = cls.fromMetrics(
            Point.fromPoint(circle.centre),
            circle.radius+0
        )
        return new

    @classmethod
    def default(cls):
        """Draws a random circle."""
        from Drawables.Point import Point
        return cls.fromMetrics(
            Point.default(),
            randomLengthPar(2)
        )


    # Getters and Setters
    def setCentre(self, point):
        """Set centre."""
        from Drawables.Point import Point
        if isinstance(point, Point):
            self.centre = point
            return
        raise TypeError(
            "TypeError:\tExpected: Point, received: "+
            f"{type(point).__name__}"
        )


    def setRadius(self, radius:float):
        """Set radius."""
        if isinstance(radius, (float, int)):
            self.radius = radius
            return
        raise TypeError(
            "TypeError:\tExpected: float, received: "+
            f"{type(radius).__name__}"
        )

    def getRadius(self):
        """Get radius."""
        return self.radius

    def getCentre(self):
        """Get the radius itself."""
        return self.centre


    # Methods
    def area(self):
        """Calculate area."""
        return pi * ((self.radius) ** 2)

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
        return self.diameterAlongPoint(point)

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
        if y < Drawable._comparisonLimit:
            y = (X2) * 0.5
        p1 = Point.fromCoOrdinates(x, y)
        p2 = Point.fromCoOrdinates(x,-y)
        p1._rotate(origin, angle)
        p2._rotate(origin, angle)
        p1._translate(tx, ty)
        p2._translate(tx, ty)
        from Drawables.Line import Line
        return(Line.fromPoints(p1, p2))

    def tangentAt(self, point=..., angle:float=...):
        """Draw a tangent on circle, with radius along a point, or an angle. Expected arguements: [point], [angle]."""
        from Drawables.Point import Point
        from Drawables.Line import Line
        status = True
        if isinstance(point, Point):
            status = Point.distanceTo(self.centre, point=point) != self.radius
            angle = 0
            if status:
                angle = self.centre.angleTo(point)
        if isinstance(angle, (float, int)):
            if status:
                point = Point.fromMetrics(angle, self.radius, self.centre)
            return Line.fromPoints(self.centre, point).perpendicularAt(point=point)
        raise TypeError(
            "TypeError:\tExpected a Point or float, received "+
            f"{type(point).__name__} and {type(angle).__name__}."
        )


    # Output interface
    def __str__(self) -> str:
        """Text return."""
        return(f"Centre {self.centre}, radius {self.radius}")
