from Drawables.Drawable import Drawable

class Polygon(Drawable):

    __name__ = "Polygon"
    def __init__(self):
        super().__init__()
        self.vertices:list
        self.edges:list
        self.order:int


    def setPolygon(self, pointList):
        from Drawables.Line import Line
        vertices = list()
        edges = list()
        prevPoint = pointList[-1]
        for curPoint in pointList:
            vertices.append(curPoint)
            edges.append(Line.fromPoints(prevPoint, curPoint))
            prevPoint = curPoint
        self.vertices = vertices
        self.edges = edges
        self.order = len(vertices)

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