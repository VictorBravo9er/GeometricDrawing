"""Point Structure."""
from rules.drawable import *
squareADT = {
    is_a:(Parallelogram,Kite),
    "new":{
        (list, Point,):{
            args:("listOfPoint",),
            trgt:Square.fromPoints,
        },
        (list, Line,):{
            args:("listOfLine",),
            trgt:Square.fromLines,
        },
        (Line,):{
            args:("line",),
            trgt:Square.fromMetrics,
        },
        (float, float):{
            args:("line", "angle",),
            trgt:Square.fromMetrics,
        },
        tuple():{
            args:tuple(),
            trgt:Square.default
        },
        retVal:Square
    },
    "copy":{
        tuple():{
            args:tuple(),
            trgt:Square.fromSquare
        },
        retVal:Square
    }
}