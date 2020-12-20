"""Point Structure."""
from rules.drawable import *
arcADT = {
    is_a:None,
    "new":{
        (Point, float, float, float,):{
            args:("centre", "radius", "startAngle", "endAngle"),
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