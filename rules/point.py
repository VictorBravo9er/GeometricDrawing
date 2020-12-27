"""Point Structure."""
from rules.drawable import *
pointADT = {
    parent:tuple(),
    "new":{
        tuple():{
            args:tuple(),
            trgt:Point.default
        },
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
        retVal:Point
    },
    "copy":{
        tuple():{
            args:tuple(),
            trgt:Point.fromPoint
        },
        retVal:Point
    },
    "slope":{
        (Point,):{
            args:("point",),
            trgt:Point.slopeTo
        },
        retVal:float
    },
    "angle":{
        (Point,):{
            args:("point",),
            trgt:Point.angleTo
        },
        (Point, Point,):{
            args:("point1", "point2",),
            trgt:Point.angleFromPoints
        },
        (Line,):{
            args:("line",),
            trgt:Point.angleFromLine
        },
        retVal:float
    },
    "distance":{
        (Point,):{
            args:("point",),
            trgt:Point.distanceTo,
        },
        (Line,):{
            args:("line",),
            trgt:Point.distanceTo
        },
        retVal:float
    },
    "midpoint":{
        (Point,):{
            args:("point",),
            trgt:Point.middlePoint
        },
        retVal:Point
    },
    "projection":{
        (Line,):{
            args:("line",),
            trgt:Point.projectionOn
        },
        retVal:Point
    },
    "bisector":{
        (Point,):{
            args:("point",),
            trgt:Point.bisect
        },
        retVal:Line
    },
    "angle_bisector":{
        (Line,):{
            args:("line",),
            trgt:Point.bisectAngleLine
        },
        (Point, Point,):{
            args:("point1", "point2",),
            trgt:Point.bisectAnglePoints
        },
        retVal:Line
    },
    "line":{
        (Point,):{
            args:("point",),
            trgt:Point.lineToPoint
        },
        (float, float,):{
            args:("angle", "distance",),
            trgt:Point.lineTo
        },
        retVal:Line
    },
    "triangle":{
        (Line,):{
            args:("line",),
            trgt:Point.triangleTo
        },
        retVal:Triangle
    },
    "circle":{
        (float,):{
            args:("radius",),
            trgt:Point.circle
        },
        retVal:Circle
    },
    "tangent_circle":{
        (Line,):{
            args:("tangent",),
            trgt:Point.circleFrom
        },
        retVal:Circle
    },
    "chord_circle":{
        (Line,):{
            args:("chord",),
            trgt:Point.circleFrom
        },
        retVal:Circle
    }
}