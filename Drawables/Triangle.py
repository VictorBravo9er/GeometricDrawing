"""Module for Point."""
from Drawables.Drawable import Drawable
from numpy import sqrt
from Drawables.Polygon import Polygon

class Triangle(Polygon):
    """Triangle class."""
    
    __name__ = "Triangle"
    def __init__(self):
        """Initializer method."""
        super().__init__()

    @classmethod
    def fromLine(cls, line, point):
        """Draw Triangle from a line and a point."""
        new = cls()
        points = [point, line.start, line.end]
        new.setPolygon(vertexList=points)
        return(new)

    @classmethod
    def fromLines(cls, lineList: list):
        """Draw Triangle from list of lines."""
        new = cls()
        new.setPolygon(edgeList=lineList)
        return new

    @classmethod
    def fromPoints(cls, pointList: list):
        """Draw Triangle list of points."""
        new = cls()
        new.setPolygon(vertexList=pointList)
        return new

    @classmethod
    def fromTriangle(cls, triangle):
        """Draw Triangle copied from another triangle."""
        new = cls()
        new.setPolygon(vertexList=Triangle.newVertices(triangle.vertices))
        return new

    def area(self):
        """Heron's Formula."""
        try:
            return self._area
        except(Exception):
            from Drawables.Point import Point
            lengths = list()
            s = 0
            prev = self.vertices[-1]
            for cur in self.vertices:
                l = Point.distanceTo(prev, cur)
                lengths.append(l)
                s += l
                prev = cur
            A = s / 2
            s = A
            for length in lengths:
                A = A * (s - length)
            A = sqrt(A)
            self._area = A
            return A

    def centroid(self):
        pass

    def orthocentre(self):
        try:
            return self._orthocentre
        except(Exception):
            pass
            self._orthocentre = None

    def circumcenter(self):
        pass

    def incircle(self):
        """Draw incircle of triangle."""
        centre = self.incenter()
        from Drawables.Line import Line
        distance = Line.fromPoints(
                self.vertices[0], self.vertices[1]
            ).distanceFrom(centre)
        from Drawables.Circle import Circle
        circ = Circle.fromMetrics(centre, distance)
        return circ

    def incenter(self):
        """Find incentre of triangle."""
        try:
            return self._incentre
        except:            
            from Drawables.Line import Line
            from Drawables.Point import Point
            a,b,c = self.vertices[0:3]
            l1 = a.bisectAnglePoints(c,b)
            l2 = b.bisectAnglePoints(a,c)
            p:Point = l1.intersectionWith(l2)
            self._incentre = p
            return p

    def medianFromPoint(self, point=None, idx=None):
        """Draw a median from a specified point."""
        from Drawables.Point import Point
        from Drawables.Line import Line
        (point, idx) = self.resolvePoint(point=point, idx=idx)
        other = [x for x in self.vertices if x != point]
        median = Line.fromPoints(
            point,
            Point.middlePoint(other[0], other[1])
            )
        return median

    def medianOnLine(self, line):
        """Draw a median on a specified line."""
        from Drawables.Line import Line
        if isinstance(line, Line):
            return self.medianFromPoint(point=self.pointOppLine(line))
        raise ValueError(f"Expected: {Line.__name__}, received {type(line).__name__}")

    def perpendicularFromPoint(self, point=None, idx=None):
        """Draw a perpendicular from a specified point."""
        (point, idx) = self.resolvePoint(point=point, idx=idx)
        from Drawables.Line import Line
        other = [x for x in self.vertices if x != point]
        perpendicular = Line.fromPoints(
                        other[0], other[1]
                    ).perpendicularFrom(point)
        return perpendicular

    def perpendicularOnLine(self, line):
        """Draw a perpendicular on a specified line."""
        from Drawables.Line import Line
        if isinstance(line, Line):
            return self.perpendicularFromPoint(point=self.pointOppLine(line))
        raise ValueError(f"Expected: {Line.__name__}, received {type(line).__name__}")

    def _rotate(self, centre=None,angle:float=0):
        from Drawables.Point import Point
        if not isinstance(centre, Point):
            centre = Point()
        for point in self.vertices:
            point._rotate(centre, angle)

    def lineOppPoint(self, point=..., idx:int=...):
        """Determine line opposite to a point."""
        from Drawables.Line import Line
        point, idx = self.resolvePoint(point=point, idx=idx)
        return Line.fromPoints(
                self.vertices[idx - 1],
                self.vertices[(idx + 1) % 3]
            )

    def pointOppLine(self, line):
        """Determine point opposite to a line."""
        from Drawables.Point import Point
        x = []
        count = 0
        for point in self.vertices:
            if Drawable.orientation(
                line.start, line.end, point
                ) == 0:
                count += 1
                continue
            x.append(point)
        if count == 2 and len(x) == 1:
            point:Point = x[0]
            return point
        raise ValueError("Line doesn't constitute the triangle.")


