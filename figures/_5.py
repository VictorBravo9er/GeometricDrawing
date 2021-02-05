"""Five module."""
from figures._1 import one
from figures._4 import four

class five(one, four):
    """five class."""

    def __init__(self):
        """Return five figure."""
        super().__init__()
        four.add(self)
