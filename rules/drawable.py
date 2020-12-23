"""Object mapping."""
import __init__
from Drawables.Drawable import Drawable
from Drawables.Point import Point
from Drawables.Line import Line
from Drawables.Polygon import Polygon
from Drawables.Circle import Circle
from Drawables.Triangle import Triangle
from Drawables.Arc import Arc
from Drawables.Quad import Quadrilateral
from Drawables.Parallelogram import Parallelogram
from Drawables.Trapezoid import Trapezoid
from Drawables.Kite import Kite

is_a:str = "is_a"
args:str = "arguements"
trgt:str = "target"
retVal:str = "return"

initOrder = (
    Point, Line, Arc, Circle, Polygon, Triangle,
    Quadrilateral, Parallelogram, Trapezoid, Kite,

    )

objectADT = {
    "int":int,
    "float":float,
    "boolean":bool,
    "str":str,
    "drawable":Drawable,
    "point":Point,
    "line":Line,
    "arc":Arc,
    "circle":Circle,
    "polygon":Polygon,
    "triangle":Triangle,
    "quad":Quadrilateral,
    "parallelogram":Parallelogram,
    "trapezoid":Trapezoid,
    "kite":Kite,
    
}
