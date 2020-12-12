from Drawables.Drawable import Drawable

class Polygon(Drawable):
    """Polygon base class."""

    def __init__(self):
        """Initialize base class."""
        super().__init__()
        self.vertices:list
        self.size:int

    def setPolygon(self, vertexList=None, edgeList=None):
        """Set Polygon, provided a list of vertices or edes(lines)."""
        from Drawables.Line import Line
        vertices = list()
        for curPoint in vertexList:
            vertices.append(curPoint)
        self.vertices = vertices
        self.size = len(vertices)

    @classmethod
    def fromPolygon(cls, polygon):
        new = cls()
        new.setPolygon(Polygon.newVertices(polygon.vertices))
        return new

    @staticmethod
    def newVertices(points):
        from Drawables.Point import Point
        new = []
        for i in range(len(points)):
            new.append(Point.fromPoint(points[i]))
        return new

    @classmethod
    def fromPoints(cls, pointList:list):
        new = cls()
        new.setPolygon(pointList)
        return new

    def area(self):
        pass

    def centroid(self):
        pass

    def centroidOfVertices(self):
        try:
            return self._vertexCentroid
        except(Exception):
            from Drawables.Point import Point
            centroid = Point()
            for point in self.vertices:
                centroid += point
            self._vertexCentroid = centroid
            return centroid

    def __str__(self) -> str:
        s = list()
        s.append(f"{self.__name__} has {self.order} sides.\nIt's vertices are:")
        i = 1
        for vertex in self.vertices:
            s.append(f"\n{i}.\t{vertex}")
            i += 1
        return("".join(s))