"""Four module."""
from Drawables.Line import Line
from figures.base import base

class four(base):
    """four class."""

    def __init__(self, marks:dict):
        """Return four figure."""
        super().__init__(marks)
        self.add(marks)

    def add(self, marks):
        """Add mark."""
        self.shapes.add(
            Line.fromPoints(*marks["diagonalup"])
        )