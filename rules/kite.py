"""Point Structure."""
from rules.drawable import *
kiteADT = {
    is_a:None,
    "new":{
        (list, Point,):{
            args:("listOfPoint",),
            trgt:Kite.fromPoints,
        },
        (list, Line,):{
            args:("listOfLine",),
            trgt:Kite.fromLines,
        },
        (Line, float, float, float):{
            args:("line", "angle", "angleCommon" "lengthOther",),
            trgt:Kite.fromMetrics,
        },
        (float, float, float, float,):{
            args:("line", "angle", "angleCommon" "lengthOther",),
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