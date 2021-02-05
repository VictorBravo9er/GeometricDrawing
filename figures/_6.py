"""Six module."""
from Drawables.Line import Line
from figures.base import base

class six(base):
    """Six class."""

    def __init__(self, marks:dict):
        """Return six figure."""
        super().__init__(marks)
        self.add(marks)

    def add(self, marks):
        """Add mark."""
        self.shapes.add(
            Line.fromPoints(*marks["shortvertical"])
        )