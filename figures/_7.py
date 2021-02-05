"""Seven module."""
from figures._6 import six
from figures._1 import one

class seven(one, six):
    """Seven class."""

    def __init__(self, marks:dict):
        """Return seven figure."""
        super().__init__(marks)
        six.add(self, marks)