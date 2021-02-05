"""Three module."""
from Drawables.Point import Point
from Drawables.Line import Line
from figures.base import base

class three(base):
    """Three class."""

    def __init__(self):
        """Return three figure."""
        super().__init__()
        self.add()

    def add(self):
        """Add mark."""
        self.shapes.append(
            Line.fromPoints(
                Point.fromCoOrdinates(*self.marks["diagonaldown"][0]),
                Point.fromCoOrdinates(*self.marks["diagonaldown"][1])
            )
        )
