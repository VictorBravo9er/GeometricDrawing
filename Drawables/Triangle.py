from typing import Any
from Drawables.Point import Point
from math import sqrt
from Drawables.Polygon import Polygon

class Triangle(Polygon):

    __name__ = "Triangle"
    def __init__(self):
        super().__init__()

    @classmethod
    def fromLine(cls, line, point):
        new = cls()
        points = [point, line.start, line.end]
        new.setPolygon(points)
        return(new)

    @classmethod
    def fromTriangle(cls, triangle):
        return super().fromPolygon(triangle)

    def area(self):
        # Heron's Formula
        try:
            return self._area
        except(Exception):
            lengths = list()
            s = 0
            for edge in self.edges:
                lengths.append(edge.length())
                s += edge.length()
            A = s / 2
            for length in lengths:
                A = A * (s - length)
            A = sqrt(A)
            self._area = A
            return A

    def centroid(self):
        return super().centroid()

    def orthocentre(self):
        try:
            return self._orthocentre
        except(Exception):
            pass
            self._orthocentre = None

    def circumcenter(self):
        pass

    def incenter(self):
        pass

    def medianFromPoint(self, point):
        if isinstance(point, Point):
            pass
            return None
        idx = self.vertices.index(point)
        return(self.medianFromPoint(idx))

    def perpendicularFromPoint(self, point):
        if isinstance(point, int):
            pass
            return None
        idx = self.vertices.index(point)
        return(self.perpendicularFromPoint(idx))
        