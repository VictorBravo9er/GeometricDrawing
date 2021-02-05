"""Eight module."""
from figures._6 import six
from figures._2 import two

class eight(two, six):
    """Eight class."""

    def __init__(self, marks:dict):
        """Return eight figure."""
        super().__init__(marks)
        six.add(self, marks)
        