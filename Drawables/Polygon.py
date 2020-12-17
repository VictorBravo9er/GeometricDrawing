"""Module for Polygons."""
import numpy as np
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
        raise ValueError(f"Expected 3 or more lines, received {l}")


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
    def area(self, vectotized:bool=True):
        """Area of polygon."""
        if vectotized:
            return abs(self.signedAreaVectorized())
        return abs(self.signedArea())

    def centroid(self, vectorized:bool=True):
        """Calculate centroid."""
        if vectorized:
            return self.centroidVectorized()
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
        (x, y) = (0, 0)
        for point in self.vertices:
            x += point.X
            y += point.Y
        x = x / self.size
        y = y / self.size
        return Point.fromCoOrdinates(x, y)


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

    def signedAreaVectorized(self):
        """Vectorized implementation of signed area(Shoelace formula)."""
        (X, Y, X_, Y_) = self.vectorize(self.vertices, shiftArray=True)
        return float(np.sum(X * Y_ - Y * X_) * 0.5)

    def centroidVectorized(self):
        """Vectorized implementation of centroid(Shoelace formula)."""
        from Drawables.Point import Point
        (X, Y, X_, Y_) = self.vectorize(self.vertices, shiftArray=True)
        R = (X * Y_ - Y * X_)
        A = 1 / float(np.sum(R) * 3)
        X = A * float(np.sum((X + X_) * R))
        Y = A * float(np.sum((Y + Y_) * R))
        return Point.fromCoOrdinates(X, Y)


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
    def vectorize(pointList:list, shiftArray=False):
        """Vectorize the vertex List."""
        X = []
        Y = []
        (X_, Y_) = (..., ...)
        for point in pointList:
            X.append(point.X)
            Y.append(point.Y)
        if shiftArray:
            X_= np.reshape(X[1:] + X[0:1], (1, -1))
            Y_= np.reshape(Y[1:] + Y[0:1], (1, -1))
        X = np.reshape(X, (1, -1))
        Y = np.reshape(Y, (1, -1))
        return (X, Y, X_, Y_)


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

    def _scale(self, sx:float=1, sy:float=1, point=...):
        if sx == 1 and sy == 1:
            return
        transform = self.scaleMatrix(sx, sy, point)
        self._applyTransform(transform)

    def _translate(self, tx:float=0, ty:float=0):
        if tx == 0 and ty == 0:
            return
        transform = self.translateMatrix(tx, ty)
        self._applyTransform(transform)

    def _rotate(self, centre=...,angle:float=0):
        if angle == 0:
            return
        transform = self.rotateMatrix(angle, centre)
        self._applyTransform(transform)

    def _applyTransform(self, transform):
        homoCoord = []
        for point in self.vertices:
            homoCoord.append([point.X, point.Y, 1])
        homoCoord = np.array(homoCoord).T
        homoCoord = np.dot(transform, homoCoord)
        homoCoord = np.reshape(homoCoord, (3, -1)).T
        i = 0
        for point in self.vertices:
            (point.X, point.Y) = [float(x) for x in homoCoord[i][0:2]]
            i += 1


    # Output interface
    def __str__(self) -> str:
        """Strngify object."""
        s = list()
        s.append(f"{type(self).__name__} has {self.size} sides.")
        s.append("It's vertices are:")
        i = 1
        for vertex in self.vertices:
            s.append(f"{i}.\t{vertex}")
            i += 1
        return("\n".join(s))

    def draw(self, axes):
        """Draw Polygon."""
        x = [p.X for p in self.vertices]
        x.append(x[0])
        y = [p.Y for p in self.vertices]
        y.append(y[0])
        axes.plot(x,y)
