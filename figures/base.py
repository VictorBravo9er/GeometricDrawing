"""Class with base functions."""
from math import pi
from Drawables.Line import Line
from Drawables.Point import Point

class base():
    """Base class."""

    step = 1
    centre = Point.fromCoOrdinates(0.0, 0.5)
    vertLine = Line.fromPoints(
        Point.fromCoOrdinates(0.0, 0.5),
        Point.fromCoOrdinates(0.5, 0.5)
    )
    horiLine = Line.fromPoints(
        Point.fromCoOrdinates(0.0, 0.0),
        Point.fromCoOrdinates(0.0, 1)
    )

    def __init__(self, marks) -> None:
        """Nothing."""
        self.shapes = {
            Line.fromPoints(*marks["vertical"])
        }

    def rotate(self):
        """Rotate shape."""
        for line in self.shapes:
            line._rotate(
                base.centre,
                pi
            )

    def reflect(self, vertical:bool=True):
        """Reflect shape."""
        for line in self.shapes:
            if vertical:
                line._reflectLine(self.vertLine)
                continue
            line._reflectLine(self.horiLine)

    def translate(self, idx):
        """Translate per 10000s."""
        for line in self.shapes:
            line._translate(-self.step * idx)

    def modify():
        pass

    def draw(self):
        from Drawables.Drawable import Drawable
        Drawable.draw(list(self.shapes))