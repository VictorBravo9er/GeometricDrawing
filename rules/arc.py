"""Point Structure."""
from rules.drawable import *
lineADT = {
    "is_a":None,
    "new":{
        (Point, float, float, float,):{
            args:("centre", "radius", "startAngle", "endAngle"),
            trgt:Arc.formArc,
        },
        (Point, Point, float,):{
            args:("centre", "point", "angle",),
            trgt:Arc.formArc,
        },
        ret:Arc
    },
    "copy":{
        tuple():{
            args:tuple(),
            trgt:Arc.copy
        },
        ret:Arc
    }
}