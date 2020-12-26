"""Base class."""
import numpy as np
from math import pi, sin, cos, inf, atan
import matplotlib.pyplot as plt

class Drawable(object):
    """Description of class."""

    _maxX, _minX, _maxY, _minY = (10.0,-10.0,10.0,-10.0)
    _comparisonLimit = 0.00000001

    def __init__(self):
        """Build Base constructor."""
        object.__init__(self)
        # super().__init__()

    @staticmethod
    def printLimits():
        """Test function to print current limits."""
        print("MinX:",Drawable._minX)
        print("MaxX:",Drawable._maxX)
        print("MinY:",Drawable._minY)
        print("MaxY:",Drawable._maxY)

    @staticmethod
    def rotateMatrix(rotation:float=0, centre=...):
        """Rotate Matrix."""
        from Drawables.Point import Point
        s = sin(rotation)
        c = cos(rotation)
        rotMat = Drawable.getIdentityMatrix()
        rotMat[0][0] = c
        rotMat[0][1] = -s
        rotMat[1][0] = s
        rotMat[1][1] = c
        if isinstance(centre, Point):
            (x, y) = (centre.X, centre.Y)
            rotMat = np.dot(Drawable.translateMatrix(x, y), rotMat)
            rotMat = np.dot(rotMat, Drawable.translateMatrix(-x, -y))  
        return rotMat

    @staticmethod
    def translateMatrix(tx:float=0, ty:float=0):
        """Translate Matrix."""
        trMat = Drawable.getIdentityMatrix()
        trMat[0][2] = tx
        trMat[1][2] = ty
        return trMat

    @staticmethod
    def scaleMatrix(sx:float=1, sy:float=1, point=...):
        """Scale Matrix."""
        scMat = Drawable.getIdentityMatrix()
        scMat[0][0] = sx
        scMat[1][1] = sy
        from Drawables.Point import Point
        if isinstance(point, Point):
            (x, y) = (point.X, point.Y)
            scMat = np.dot(Drawable.translateMatrix(x, y), scMat)
            scMat = np.dot(scMat, Drawable.translateMatrix(-x, -y))  
        return scMat

    @staticmethod
    def shearMatrix(shx:float=0,shy:float=0, point=..., xSlope=0):
        """Shear Matrix."""
        shMat = Drawable.getIdentityMatrix()
        shMat[0][1] = shx
        shMat[1][0] = shy
        from Drawables.Point import Point
        if isinstance(xSlope,(float, int)):
            pass
            xSlope = atan(xSlope)
            shMat = np.dot(Drawable.rotateMatrix(xSlope), shMat)
            shMat = np.dot(shMat, Drawable.rotateMatrix(-xSlope))
        if isinstance(point, Point):
            (x, y) = (point.X, point.Y)
            shMat = np.dot(Drawable.translateMatrix(x, y), shMat)
            shMat = np.dot(shMat, Drawable.translateMatrix(-x, -y))
        return shMat

    @staticmethod
    def reflectionPointmatrix(point=...):
        """Reflect matrix(Point)."""
        return Drawable.scaleMatrix(sx=-1, sy=-1, point=point)

    @staticmethod
    def reftectionLineMatrix(slope:float=0, intercept:float=0):
        """Reflect Matrix(Line). Takes in slope and intercept."""
        trans, trans_ = None, None
        if slope == inf:
            trans = (-intercept, 0)
            trans_ = (intercept, 0)
        else:
            trans = (0, -intercept)
            trans_ = (0, intercept)
        slope = atan(slope)
        refMat = Drawable.translateMatrix(*trans)
        refMat = np.dot(Drawable.rotateMatrix(-slope), refMat)
        refMat = np.dot(Drawable.scaleMatrix(1, -1), refMat)
        refMat = np.dot(Drawable.rotateMatrix(slope), refMat)
        refMat = np.dot(Drawable.translateMatrix(*trans_), refMat)
        return refMat

    @staticmethod
    def getIdentityMatrix():
        """Identity Matrix."""
        return np.identity(3, dtype="float")

    @staticmethod
    def orientation(pointA, pointB, target):
        """Orientation test. 0 - coliniar for it, 1 - left, -1 - right."""
        if target in (pointA, pointB):
            return -1
        buf = np.array([1, pointA.X, pointA.Y, 1, pointB.X, pointB.Y, 1, target.X, target.Y]).reshape(3,-1)
        buf = np.linalg.det(buf)
        if abs(buf) < Drawable._comparisonLimit:
            return 0
        if buf < 0:
            return -1
        return 1

    @staticmethod
    def processPrintableData(data:tuple):
        """To process printable data, like area, etc."""
        try:
            msg, value = data
        except Exception as e:
            raise Exception(f"Expected 2 items, got {len(data)} items")
        print(f"{msg}\n\tValue: {value}")

    @staticmethod
    def draw(
        drawables:list, _show:bool=True, _store:bool=False,
        _storageName:str="./data/store", _print:bool=False
    ):
        """Draw call."""
        fig, ax = plt.subplots(1)
        ax.set_aspect(1)
        from Parser.collect import initOrder as acceptable
        for drawable in drawables:
            if isinstance(drawable, acceptable):
                drawable.draw(ax)
            elif isinstance(drawable, tuple):
                # process values other than drawable figures
                try:
                    if _print:
                        Drawable.processPrintableData(drawable)
                except Exception as e:
                    print(e.args[0])
            else:
                print("Error with object:",drawable)
        if _store:
            plt.savefig(
                f"{_storageName}.jpg", dpi=320,
                pil_kwargs={'quality':90, 'optimize':True}
            )
        if _show:
            plt.show()
        return fig

    def __str__(self):
        """Text maker."""
        return super().__str__()
