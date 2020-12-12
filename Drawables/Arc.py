"""Module for Arc."""
from math import  pi, sqrt, degrees, radians
from Drawables.Drawable import Drawable
import numpy as np
from numpy import sin,cos

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

    def plotPoints(self):
        """Return plottable graph of a an arc."""
        theta = np.linspace(self.__start, self.__end, 1000)
        x = self.radius * cos(theta) + self.centre.X
        y = self.radius * sin(theta) + self.centre.Y
        return(x,y)

    def draw(self, axes):
        """Draw a circle."""
        x,y = self.plotPoints()
        axes.plot(x,y)