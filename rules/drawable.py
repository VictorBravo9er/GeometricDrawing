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
from Drawables.Rectangle import Rectangle
from Drawables.Rhombus import Rhombus
from Drawables.Square import Square

parent:str = "parent"
args:str = "arguements"
trgt:str = "target"
retVal:str = "return"

initOrder = (
    Point, Line, Arc, Circle, Polygon, Triangle,
    Quadrilateral, Parallelogram, Trapezoid, Kite,
    Rectangle, Rhombus, Square
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
    "trapezoid":Trapezoid,
    "kite":Kite,
    "parallelogram":Parallelogram,
    "rectangle":Rectangle,
    "rhombus":Rhombus,
    "square":Square,
}
