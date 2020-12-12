"""Module for Point."""
from Drawables.Circle import Circle
from numpy import sqrt
from Drawables.Polygon import Polygon

class Triangle(Polygon):
    """Triangle class."""
    
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
    def fromPoints(cls, pointList: list):
        new = cls()
        new.setPolygon(pointList)
        return new

    @classmethod
    def fromTriangle(cls, triangle):
        new = cls()
        new.setPolygon(Triangle.newVertices(triangle.vertices))
        return new

    def area(self):
        """Heron's Formula."""
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
        try:
            centre = self._incentre
        except: 
            centre = self.incenter()
        from Drawables.Line import Line
        distance = Line.fromPoints(
                self.vertices[0], self.vertices[1]
            ).distanceFrom(centre)
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

    def medianFromPoint(self, point):
        """Draw a median from a specified point."""
        if isinstance(point, int):
            point = self.vertices[point]
        if isinstance(point, Point):
            if point not in self.vertices:
                raise ValueError("Point not in Triangle.")
            from Drawables.Line import Line
            other = [x for x in self.vertices if x != point]
            median = Line.fromPoints(point,
                Point.middlePoint(other[0], other[1]))
            return median
        raise TypeError("Unsupported Type. Support: int,Point")

    def perpendicularFromPoint(self, point):
        """Draw a perpendicular from a specified point."""
        if isinstance(point, int):
            point = self.vertices[point]
        if isinstance(point, Point):
            if point not in self.vertices:
                raise ValueError("Point not in Triangle.")
            from Drawables.Line import Line
            other = [x for x in self.vertices if x != point]
            perpendicular = Line.fromPoints(
                            other[0], other[1]
                        ).perpendicularFrom(point)
            return perpendicular
        raise TypeError("Unsupported Type. Support: int,Point")

    def _rotate(self, centre=None,angle:float=0):
        from Drawables.Point import Point
        if not isinstance(centre, Point):
            centre = Point()
        for point in self.vertices:
            point._rotate(centre, angle)

    def draw(self, axes):
        """Draw Triangle."""
        x = [p.X for p in self.vertices]
        x.append(x[0])
        y = [p.Y for p in self.vertices]
        y.append(y[0])
        axes.plot(x,y)