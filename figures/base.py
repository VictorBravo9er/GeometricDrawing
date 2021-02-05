"""Class with base functions."""
from math import pi
from Drawables.Line import Line
from Drawables.Point import Point

class base():
    """Base class."""

    from figures.marks import markings
    step = 1
    marks = markings()
    limit = 10000
    commonLine = Line.fromPoints(
        Point.fromCoOrdinates(*marks["vertical"][0]),
        Point.fromCoOrdinates(*marks["vertical"][1])
    )
    centre = Point.fromCoOrdinates(*marks["horizon"][0])
    vertLine = commonLine
    horiLine = Line.fromPoints(
        Point.fromCoOrdinates(*marks["horizon"][0]),
        Point.fromCoOrdinates(*marks["horizon"][1])
    )



    def __init__(self) -> None:
        """Nothing."""
        self.shapes = []

    def getShapes(self):
        """Getter."""
        return list(self.shapes)

    @staticmethod
    def rotate(s):
        """Rotate shape."""
        if isinstance(s, base):
            temp = s.shapes
        elif isinstance(s, (tuple, list, set)):
            temp = s
        else:
            raise Exception("Type Mismatch")
        for line in temp:
            line._reflectPoint(
                base.centre
            )
        return temp

    @staticmethod
    def reflect(s, vertical:bool=True):
        """Reflect shape."""
        if isinstance(s, base):
            temp = s.shapes
        elif isinstance(s, (tuple, list, set)):
            temp = s
        else:
            raise Exception("Type Mismatch")
        for line in temp:
            if vertical:
                line._reflectLine(base.vertLine)
                continue
            line._reflectLine(base.horiLine)
        return temp

    @staticmethod
    def translate(s, idx):
        """Translate per 10000s."""
        temp = ...
        if isinstance(s, base):
            temp = s.shapes
        elif isinstance(s, (tuple, list, set)):
            temp = s
        else:
            raise Exception("Type Mismatch")
        for line in temp:
            line._translate(-base.step * idx)
        return temp

    @staticmethod
    def modify(number:int):
        """Arrange number."""
        draws = []
        numbers = []
        if number == 0:
            numbers.append(0)
        while number > 0:
            numbers.append(number % base.limit)
            number = number // base.limit
        for idx in range(len(numbers)):
            baseDraw = []
            from figures.figure import figures
            number = numbers[idx]
            one, number = number % 10, number //10
            two, number = number % 10, number //10
            three, number = number % 10, number //10
            four = number
            one, two, three, four = (
                figures[one](), figures[two](),
                figures[three](), figures[four]()
            )

            baseDraw.extend(base.getShapes(one))
            
            baseDraw.extend(
                base.reflect(base.getShapes(two))
            )
            baseDraw.extend(
                base.reflect(base.getShapes(three), vertical=False)
            )
            
            baseDraw.extend(
                base.rotate(base.getShapes(four))
            )
            baseDraw.append(Line.fromLine(base.commonLine))
            base.translate(baseDraw, idx)
            draws.extend(baseDraw)
        return draws


    def draw(self):
        """Draw figure."""
        from Drawables.Drawable import Drawable
        Drawable.draw(list(self.shapes))