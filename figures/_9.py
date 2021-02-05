"""Nine module."""
from figures._6 import six
from figures._1 import one
from figures._2 import two

class nine(one, two, six):
    """Nine class."""

    def __init__(self, marks:dict):
        """Return nine figure."""
        super().__init__(marks)
        two.add(self, marks)
        six.add(self, marks)
