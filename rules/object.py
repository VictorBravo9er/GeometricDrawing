"""Object mapping."""
import __init__
from Drawables.Drawable import Drawable
from Drawables.Point import Point
from Drawables.Line import Line
from Drawables.Polygon import Polygon
from Drawables.Circle import Circle
from Drawables.Triangle import Triangle
from typing import List, Tuple
objectADT = {
    int:"integer number",
    float:"floating point number",
    bool:"boolean value",
    Drawable:"drawable",
    Point:"point",
    Line:"line",
    Circle:"circle",
    Polygon:"polygon",
    Triangle:"triangle"
}

def isfloatOrBool(target:str):
