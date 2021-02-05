"""Six module."""
from Drawables.Point import Point
from Drawables.Line import Line
from figures.base import base

class six(base):
    """Six class."""

    def __init__(self):
        """Return six figure."""
        super().__init__()
        self.add()

    def add(self):
        """Add mark."""
        self.shapes.append(
            Line.fromPoints(
                Point.fromCoOrdinates(*self.marks["shortvertical"][0]),
                Point.fromCoOrdinates(*self.marks["shortvertical"][1])
            )
        )