"""Point Structure."""
from rules.drawable import *
trapezoidADT = {
    parent:(Quadrilateral,),
    "new":{
        (list, Point,):{
            args:("listOfPoint",),
            trgt:Trapezoid.fromPoints,
        },
        (list, Line,):{
            args:("listOfLine",),
            trgt:Trapezoid.fromLines,
        },
        (Line, float, float, float):{
            args:("line", "angle1", "angle2" "height",),
            trgt:Trapezoid.fromMetrics,
        },
        (float, float, float, float,):{
            args:("line", "angle1", "angle2" "height",),
            trgt:Trapezoid.fromMetrics,
        },
        tuple():{
            args:tuple(),
            trgt:Trapezoid.default
        },
        retVal:Trapezoid
    },
    "copy":{
        tuple():{
            args:tuple(),
            trgt:Trapezoid.fromTrapezoid
        },
        retVal:Trapezoid
    }
}