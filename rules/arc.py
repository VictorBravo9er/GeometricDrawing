"""Point Structure."""
from rules.drawable import *
arcADT = {
    parent:tuple(),
    "new":{
        (Point, float, float, float,):{
            args:("centre", "radius", "angleStart", "angleEnd"),
            trgt:Arc.formArc,
        },
        (Point, Point, float,):{
            args:("centre", "point", "angle",),
            trgt:Arc.formArc,
        },
        retVal:Arc
    },
    "copy":{
        tuple():{
            args:tuple(),
            trgt:Arc.copy
        },
        retVal:Arc
    }
}