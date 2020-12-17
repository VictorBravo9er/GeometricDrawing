"""Object mapping."""
import __init__
from Drawables.Drawable import Drawable
from Drawables.Point import Point
from Drawables.Line import Line
from Drawables.Polygon import Polygon
from Drawables.Circle import Circle
from Drawables.Triangle import Triangle
from Drawables.Arc import Arc

args:str = "arguements"
trgt:str = "target"
ret:str = "return"

initOrder = (
    Point, Line, Arc, Circle, Polygon, Triangle,
    
    )

objectADT = {
    "int":int,
    "float":float,
    "boolean":bool,
    "drawable":Drawable,
    "arc":Arc,
    "point":Point,
    "line":Line,
    "circle":Circle,
    "polygon":Polygon,
    "triangle":Triangle
}
