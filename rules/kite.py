"""Point Structure."""
from rules.drawable import *
kiteADT = {
    parent:(Quadrilateral,),
    "new":{
        (list, Point,):{
            args:("listOfPoint",),
            trgt:Kite.fromPoints,
        },
        (list, Line,):{
            args:("listOfLine",),
            trgt:Kite.fromLines,
        },
        (Line, float, float):{
            args:("line", "lengthOther", "angle"),
            trgt:Kite.fromMetrics,
        },
        (float, float, float, float,):{
            args:("line", "angleLine" "lengthOther", "angle"),
            trgt:Kite.fromMetrics,
        },
        tuple():{
            args:tuple(),
            trgt:Kite.default
        },
        retVal:Kite
    },
    "copy":{
        tuple():{
            args:tuple(),
            trgt:Kite.fromKite
        },
        retVal:Kite
    }
}