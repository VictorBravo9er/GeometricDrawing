"""Different marks."""
from Drawables.Point import Point

def markings():
    """Return marked positions of figures."""
    top, bottom, left, right, mid = 1.0, 0.0, 0.0, 0.3, 0.7

    top_right = (right, top)
    right = (right, mid)
    mid = (left, mid)
    top = (left, top)
    bottom = (left, bottom)

    return {
        "vertical":     (bottom, top),
        "shortvertical":(right, top_right),
        "tophorizontal":(top, top_right),
        "midhorizontal":(mid, right),
        "diagonaldown":(top, right),
        "diagonalup":(mid, top_right),
        "horizon":((0,0.5), (1,0.5))
    }
