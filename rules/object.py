"""Object mapping."""
import __init__
from Drawables.Drawable import Drawable
from Drawables.Point import Point
from Drawables.Line import Line
from Drawables.Polygon import Polygon
from Drawables.Circle import Circle
from Drawables.Triangle import Triangle

args:str = "arguements"
trgt:str = "target"
ret:str = "return"

initOrder = (
    Point, Line, Circle, Polygon, Triangle,
    
    )

objectADT = {
    "int":int,
    "float":float,
    "boolean":bool,
    "drawable":Drawable,
    "point":Point,
    "line":Line,
    "circle":Circle,
    "polygon":Polygon,
    "triangle":Triangle
}

def isfloatOrBool(trgt:str):
    """Don't know what it does yet.""" 
    pass