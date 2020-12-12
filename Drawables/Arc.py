"""Module for Arc."""
from math import pi
from Drawables.Drawable import Drawable
import numpy as np
from numpy import sin, cos

class Arc(Drawable):
    """Description of class."""

    def __init__(self, centre, radius:float, start:float=0, end:float=2*pi):
        """Cunstruct a default, empty container."""
        super().__init__()
        from Drawables.Point import Point
        self.centre:Point = centre
        self.radius:float = radius
        self.__start = start
        self.__end = end


    # Constructor
    @classmethod
    def copy(cls, self):
        """Make a copy of an arc."""
        new = cls(
                self.centre, self.radius,
                self.__start, self.__end
            )
        return new


    # Method
    @classmethod
    def formArc(
        cls, centre, point=None, angle=None,
        radius:float=None, startAngle:float=None, endAngle:float=None
    ):
        """Construct the class."""
        from Drawables.Point import Point
        try:
            if isinstance(point, Point):
                assert isinstance(angle, (int, float))
                radius = Point.distanceTo(centre, point)
                startAngle = Point.angleTo(centre, point)
                endAngle = startAngle + angle
            else:
                assert isinstance(startAngle, (int, float))
                assert isinstance(endAngle, (int, float))
                assert isinstance(radius, (float, int,))
                if startAngle > endAngle:
                    endAngle += (2*pi)
            return cls(centre, radius, startAngle, endAngle)
        except:
            raise Exception("Invalid arguement(s).")


    # Helpers
    def plotPoints(self):
        """Return plottable graph of a an arc."""
        theta = np.linspace(self.__start, self.__end, 1000)
        x = self.radius * cos(theta) + self.centre.X
        y = self.radius * sin(theta) + self.centre.Y
        return(x,y)

    def _scale(self, scale:float):
        self.radius *= scale

    def _translate(self, tx:float=0, ty:float=0):
        self.centre._translate(tx, ty)

    def _rotate(self, centre=None,angle:float=0):
        from Drawables.Point import Point
        if not isinstance(angle, (float, int)):
            raise Exception("Invalid Arguement(s).")
        self.centre._rotate(centre, angle)
        self.__start += angle
        self.__end += angle

    def _reflectPoint(self, point):
        self.centre._reflectPoint(point)
        angle = self.centre.angleTo(point)
        angle -= pi
        self.__start += angle
        self.__end  += angle

    def _reflectLine(self, line):
        point = self.centre.projectionOn(line)
        self.centre._reflectPoint(point)
        angle = self.centre.angleTo(point)
        angle += pi
        self.__start = angle - self.__start
        self.__end = angle - self.__end
    
    def __ne__(self, o) -> bool:
        """'!=' operator overload."""
        return not self == o

    def __eq__(self, o) -> bool:
        """'==' operator overload."""
        if not isinstance(o, self.__class__):
            raise TypeError(f"Uncomparable Types. Can't compare {type(self)} with {type(o)}")
        try:
            assert self.centre == o.centre and self.radius == o.radius
            assert self.__start == o.__start and self.__end == o.__end
        except:
            return False
        return True


    # Output interface
    def draw(self, axes):
        """Draw a circle."""
        x,y = self.plotPoints()
        axes.plot(x,y)