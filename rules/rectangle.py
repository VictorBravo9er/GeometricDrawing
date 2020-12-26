"""Point Structure."""
from rules.drawable import *
rectangleADT = {
    is_a:(Parallelogram,),
    "new":{
        (list, Point,):{
            args:("listOfPoint",),
            trgt:Rectangle.fromPoints,
        },
        (list, Line,):{
            args:("listOfLine",),
            trgt:Rectangle.fromLines,
        },
        (float, float, float):{
            args:("line", "angleLine", "lengthOther",),
            trgt:Rectangle.fromMetrics,
        },
        (Line, float):{
            args:("line", "lengthOther",),
            trgt:Rectangle.fromMetrics,
        },
        tuple():{
            args:tuple(),
            trgt:Rectangle.default
        },
        retVal:Rectangle
    },
    "copy":{
        tuple():{
            args:tuple(),
            trgt:Rectangle.fromRectangle
        },
        retVal:Rectangle
    }
}