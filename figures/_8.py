"""Eight module."""
from figures._6 import six
from figures._2 import two

class eight(two, six):
    """Eight class."""

    def __init__(self):
        """Return eight figure."""
        super().__init__()
        six.add(self,)
        