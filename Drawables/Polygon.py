"""Module for Polygons."""
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
        new.setPolygon(cls.newVertices(polygon.vertices))
        return new

    @classmethod
    def fromPoints(cls, pointList:list):
        """Draw polygon from points."""
        l = len(pointList)
        if l == 4:
            pass
        if l == 3:
            from Drawables.Triangle import Triangle
            return Triangle.fromPoints(pointList)
        if l > 4:
            new = cls()
            new.setPolygon(vertexList=pointList)
            return new
        raise ValueError(f"Expected 3 or more points, received {l}")

    @classmethod
    def fromLines(cls, lineList:list):
        """Draw polygon from lines."""
        l = len(lineList)
        if l == 4:
            pass
        if l == 3:
            from Drawables.Triangle import Triangle
            return Triangle.fromLines(lineList)
        if l > 4:
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
        return abs(self.signedArea())

    def centroid(self):
        """Calculate centroid."""
        from Drawables.Point import Point
        A = 0.0
        (x, y) = (0.0, 0.0)
        prev = self.vertices[-1]
        for cur in self.vertices:
            det = (prev.X * cur.Y - cur.X * prev.Y)
            x += ((prev.X + cur.X) * det)
            y += ((prev.Y + cur.Y) * det)
            A += det
            prev = cur
        A = 1 / (6 * A * 0.5)
        (x, y) = (A * x, A * y)
        return Point.fromCoOrdinates(x, y)

    def internAngle(self, point=..., idx:int=...):
        """Calculate Internal angle at a vertex."""
        from Drawables.Point import Point
        (point, idx) = self.resolvePoint(point=point, idx=idx)
        angle = Point.angleFromPoints(
            point, self.vertices[idx - 1],
            self.vertices[(idx + 1) % len(self.vertices)]
            )
        if self.clockwise:
            return angle
        return (2 * pi) - angle

    def angleBisector(self, point=..., idx:int=...):
        """Angle bisector."""
        from Drawables.Point import Point
        (point, idx) = self.resolvePoint(point=point, idx=idx)
        return Point.bisectAnglePoints(
            self=point, point1=self.vertices[idx - 1],
            point2=self.vertices[(idx + 1) % len(self.vertices)]
            )

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
        if isinstance(points, list):
            from Drawables.Point import Point
            new:list = []
            for point in points:
                new.append(Point.fromPoint(point))
            return new
        raise TypeError(f"Expected list of points, received {type(points).__name__}.")

    def signedArea(self):
        """Signed area for nonintersecting Polygon using shielace formula."""
        area = 0
        prev = self.vertices[-1]
        for cur in self.vertices:
            area += (prev.X * cur.Y - cur.X * prev.Y)
            prev = cur
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

    def resolvePoint(self, point=..., idx:int=...):
        """Resolve availability of vertex in Polygon or its indexed."""
        from Drawables.Point import Point
        if isinstance(idx, int):
            l = len(self.vertices)
            if idx >= l or idx < 0:
                raise ValueError(f"Point index out of range. Must've be in range: 0 - {l}")
            p:Point = self.vertices[idx]
            return (p, idx)
        if isinstance(point, Point):
            try:
                idx = self.vertices.index(point)
            except:
                raise ValueError("Point not in Triangle.")
            return (point, idx)
        raise TypeError("Unsupported Type. Expected: int or Point")


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
