"""Four module."""
from Drawables.Point import Point
from Drawables.Line import Line
from figures.base import base

class four(base):
    """four class."""

    def __init__(self):
        """Return four figure."""
        super().__init__()
        self.add()

    def add(self):
        """Add mark."""
        self.shapes.append(
            Line.fromPoints(
                Point.fromCoOrdinates(*self.marks["diagonalup"][0]),
                Point.fromCoOrdinates(*self.marks["diagonalup"][1])
            )
        )
