from math import pi
from Drawables.Drawable import Drawable

class Polygon(Drawable):
    """Polygon base class."""

    def __init__(self):
        """Initialize base class."""
        super().__init__()
        self.vertices:list
        self.size:int
        self.clockwise:bool


    # Constructors
    @classmethod
    def fromPolygon(cls, polygon):
        """Copy a polygon."""
        new = cls()
        new.setPolygon(Polygon.newVertices(polygon.vertices))
        return new

    @classmethod
    def fromPoints(cls, pointList:list):
        """Draw polygon from points."""
        if len(pointList) == 4:
            pass
        if len(pointList) == 3:
            pass
        new = cls()
        new.setPolygon(vertexList=pointList)
        return new

    @classmethod
    def fromLines(cls, lineList:list):
        """Draw polygon from lines."""
        if len(lineList) == 4:
            pass
        if len(lineList) == 3:
            pass
        new = cls()
        new.setPolygon(edgeList=lineList)
        return new


    # Getters and Setters
    def setPolygon(self, vertexList=None, edgeList=None):
        """Set Polygon, provided a list of vertices or edes(lines)."""
        vertices = list()
        if isinstance(edgeList, list):
            vertexList = Polygon.edgeToVertex(edgeList)
        if isinstance(vertexList, list):
            from Drawables.Point import Point
            for curPoint in vertexList:
                if not isinstance(curPoint, Point):
                    raise Exception(
                        f"Invalid arguements. Expected a {Point}, received a {type(curPoint)}"
                        )
                vertices.append(curPoint)
            self.vertices = vertices
            self.size = len(vertices)
            self.circularDirection()
        else:
            raise Exception(
                "Invalid arguements. Expected either a list of edges or vertices"
                )


    # Methods
    def area(self):
        """Area of polygon."""
        return abs(Polygon.signedArea(self.vertices))

    def centroid(self):
        pass

    def internAngle(self, point=None, idx=None):
        pass

    def externAngle(self, point=None, idx=None):
        pass

    def vertexCentroid(self):
        """Return centroid of vertices."""
        from Drawables.Point import Point
        centroid = Point()
        for point in self.vertices:
            centroid += point
        self._vertexCentroid = centroid
        return centroid


    # Helpers
    @staticmethod
    def newVertices(points):
        """Provide new vertices in order to form a new polygon."""
        from Drawables.Point import Point
        new = []
        for i in range(len(points)):
            new.append(Point.fromPoint(points[i]))
        return new

    @staticmethod
    def signedArea(vertexList):
        """Signed area for nonintersecting Polygon using shielace formula."""
        area = 0
        prev = vertexList[-1]
        for cur in vertexList:
            area += (prev.X * cur.Y - cur.X * prev.Y)
        return area * 0.5

    def circularDirection(self):
        """Check for circular direction of vertices."""
        (prevVertex ,curVertex) = self.vertices[-2:]
        from Drawables.Point import Point
        p = 2 * pi
        n = len(self.vertices) * pi
        intAngle = 0.0
        extAngle = 0.0
        for nextVertex in self.vertices:
            tmpAngle = Point.angleFromPoints(curVertex, prevVertex, nextVertex)
            intAngle += tmpAngle
            extAngle += (p - tmpAngle)
            curVertex, prevVertex = nextVertex, curVertex
        (n, p) = (n - p, n + p)
        if abs(intAngle - n) < Polygon.comparisonLimit and abs(extAngle - p) < Polygon.comparisonLimit:
            self.clockwise = True
            return
        elif abs(intAngle - p) < Polygon.comparisonLimit and abs(extAngle - n) < Polygon.comparisonLimit:
            self.clockwise = False
            return
        raise Exception("Irregularity in polygon")


    @staticmethod
    def edgeToVertex(edgeList:list):
        """Convert edge List to vertex List."""
        prevEdge = edgeList[0]
        vertexList = []
        from Drawables.Line import Line
        if not isinstance(prevEdge, Line):
            raise Exception(
                f"Invalid arguements. Expected a {Line}, received a {type(prevEdge)}."
                )
        for curEdge in edgeList:
            if not isinstance(curEdge, Line):
                raise Exception(
                    f"Invalid arguements. Expected a {Line}, received a {type(curEdge)}."
                    )
            vertexList.append(Polygon.compareEdgeEnds(prevEdge, curEdge))
        return vertexList

    @staticmethod
    def compareEdgeEnds(edge1, edge2):
        """Compare endpoints of two edges, else compute intersection."""
        if edge1.start == edge2.start:
            return edge1.start
        if edge1.start == edge2.end:
            return edge1.start
        if edge1.end == edge2.start:
            return edge1.end
        if edge1.end == edge2.end:
            return edge1.end
        from Drawables.Line import Line
        return Line.intersectionWith(edge1, edge2)


    # Output interface
    def __str__(self) -> str:
        """Strngify object."""
        s = list()
        s.append(f"It has {self.size} sides. It's vertices are:")
        i = 1
        for vertex in self.vertices:
            s.append(f"\n{i}.\t{vertex}")
            i += 1
        return("".join(s))

    def draw(self, axes):
        """Draw Polygon."""
        x = [p.X for p in self.vertices]
        x.append(x[0])
        y = [p.Y for p in self.vertices]
        y.append(y[0])
        axes.plot(x,y)