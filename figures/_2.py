"""Two module."""
from Drawables.Point import Point
from Drawables.Line import Line
from figures.base import base

class two(base):
    """Two class."""

    def __init__(self):
        """Return two figure."""
        super().__init__()
        self.add()

    def add(self):
        """Add mark."""
        self.shapes.append(
            Line.fromPoints(
                Point.fromCoOrdinates(*self.marks["midhorizontal"][0]),
                Point.fromCoOrdinates(*self.marks["midhorizontal"][1])
            )
        )
