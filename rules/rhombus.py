"""Point Structure."""
from rules.drawable import *
rhombusADT = {
    parent:(Parallelogram,Kite),
    "new":{
        (list, Point,):{
            args:("listOfPoint",),
            trgt:Rhombus.fromPoints,
        },
        (list, Line,):{
            args:("listOfLine",),
            trgt:Rhombus.fromLines,
        },
        (Line, float):{
            args:("line", "angleInternal",),
            trgt:Rhombus.fromMetrics,
        },
        (float, float, float):{
            args:("line", "angleLine","angleInternal",),
            trgt:Rhombus.fromMetrics,
        },
        tuple():{
            args:tuple(),
            trgt:Rhombus.default
        },
        retVal:Rhombus
    },
    "copy":{
        tuple():{
            args:tuple(),
            trgt:Rhombus.fromRhombus
        },
        retVal:Rhombus
    }
}