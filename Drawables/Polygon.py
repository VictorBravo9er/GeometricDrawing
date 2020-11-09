from Drawables.Drawable import Drawable

class Polygon(Drawable):

    def __init__(self):
        super().__init__()

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
        copyPoints = list(polygon.vertices)
        new.setPolygon(copyPoints)

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