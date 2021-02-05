"""Different marks."""
from Drawables.Point import Point

def marks():
    """Return marked positions of figures."""
    top, bottom, left, right, mid = 1.0, 0.0, 0.0, 0.5, 0.6

    top_right = Point.fromCoOrdinates(right, top)
    right = Point.fromCoOrdinates(right, mid)
    mid = Point.fromCoOrdinates(left, mid)
    top = Point.fromCoOrdinates(left, top)
    bottom = Point.fromCoOrdinates(left, bottom)

    return {
        "vertical":     (bottom, top),
        "shortvertical":(right, top_right),
        "tophorizontal":(top, top_right),
        "midhorizontal":(mid, right),
        "diagonaldown":(top, right),
        "diagonalup":(mid, top_right)
    }