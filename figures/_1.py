"""One module."""
from Drawables.Point import Point
from Drawables.Line import Line
from figures.base import base

class one(base):
    """One class."""

    def __init__(self):
        """Return one figure."""
        super().__init__()
        self.add()

    def add(self):
        """Add mark."""
        self.shapes.append(
            Line.fromPoints(
                Point.fromCoOrdinates(*self.marks["tophorizontal"][0]),
                Point.fromCoOrdinates(*self.marks["tophorizontal"][1])
            )
        )
