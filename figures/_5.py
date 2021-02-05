"""Five module."""
from Drawables.Line import Line
from figures._1 import one
from figures._4 import four

class five(one, four):
    """five class."""

    def __init__(self, marks:dict):
        """Return five figure."""
        super().__init__(marks)
        four.add(self, marks)
