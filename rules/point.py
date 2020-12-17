"""Point Structure."""
from rules.drawable import *
pointADT = {
    is_a:None,
    "new":{
        (float, float,):{
            args:("x", "y",),
            trgt:Point.fromCoOrdinates
        },
        (Point, Point, float, float,):{
            args:("point1", "point2", "m", "n",),
            trgt:Point.fromSection
        },
        (float, float, Point,):{
            args:("angle", "distance", "point",),
            trgt:Point.fromMetrics
        },
        ret:Point
    },
    "copy":{
        tuple():{
            args:tuple(),
            trgt:Point.fromPoint
        },
        ret:Point
    },
    "slopeTo":{
        (Point,):{
            args:("point",),
            trgt:Point.slopeTo
        },
        ret:float
    },
    "angleTo":{
        (Point,):{
            args:("point",),
            trgt:Point.angleTo
        },
        ret:float
    },
    "angleFrom":{
        (Point, Point,):{
            args:("point1", "point2",),
            trgt:Point.angleFromPoints
        },
        (Line,):{
            args:("line",),
            trgt:Point.angleFromLine
        },
        ret:float
    },
    "distanceTo":{
        (Point,):{
            args:("point",),
            trgt:Point.distanceTo,
        },
        (Line,):{
            args:("line",),
            trgt:Point.distanceTo
        },
        ret:float
    },
    "midPoint":{
        (Point,):{
            args:("point",),
            trgt:Point.middlePoint
        },
        ret:Point
    },
    "projection":{
        (Line,):{
            args:("line",),
            trgt:Point.projectionOn
        },
        ret:Point
    },
    "bisector":{
        (Point,):{
            args:("point",),
            trgt:Point.bisect
        },
        ret:Line
    },
    "angleBisector":{
        (Line,):{
            args:("line",),
            trgt:Point.bisectAngleLine
        },
        (Point, Point,):{
            args:("point1", "point2",),
            trgt:Point.bisectAnglePoints
        },
        ret:Line
    },
    "lineTo":{
        (Point,):{
            args:("point",),
            trgt:Point.lineToPoint
        },
        (float, float,):{
            args:("angle", "distance",),
            trgt:Point.lineTo
        },
        ret:Line
    },
    "triangle":{
        (Line,):{
            args:("line",),
            trgt:Point.triangleTo
        },
        ret:Triangle
    },
    "circle":{
        (float,):{
            args:("radius",),
            trgt:Point.circle
        },
        ret:Circle
    },
    "tangentCircle":{
        (Line,):{
            args:("tangent",),
            trgt:Point.circleFrom
        },
        ret:Circle
    },
    "chordCircle":{
        (Line,):{
            args:("chord",),
            trgt:Point.circleFrom
        },
        ret:Circle
    }
}