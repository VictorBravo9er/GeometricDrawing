"""Base class."""
import numpy as np
from math import sin, cos, inf, atan

class Drawable(object):
    """Description of class."""

    res = {}

    def __init__(self):
        """Build Base constructor."""
        object.__init__(self)
        # super().__init__()

    def rotateMatrix(self, rotation:float=0):
        """Rotate Matrix."""
        s = sin(rotation)
        c = cos(rotation)
        rotMat = self.getIdentityMatrix()
        rotMat[0][0] = c
        rotMat[0][1] = -s
        rotMat[1][0] = s
        rotMat[1][1] = c
        return rotMat

    def translateMatrix(self, tx:float=0, ty:float=0):
        """Translate Matrix."""
        trMat = self.getIdentityMatrix()
        trMat[0][2] = tx
        trMat[1][2] = ty
        return trMat

    def scaleMatrix(self, sx:float=1, sy:float=1):
        """Scale Matrix."""
        scMat = self.getIdentityMatrix()
        scMat[0][0] = sx
        scMat[1][1] = sy
        return scMat

    def shearMatrix(self, shx:float=0,shy:float=0):
        """Shear Matrix."""
        shMat = self.getIdentityMatrix()
        shMat[0][1] = shx
        shMat[1][0] = shy
        return shMat

    def reftectionMatrix(self, slope:float=0, intercept:float=0):
        """Reflect Matrix. Takes in slope and intercept."""
        trans, trans_ = None, None
        if slope == inf:
            trans = (-intercept, 0)
            trans_ = (intercept, 0)
        else:
            trans = (0, -intercept)
            trans_ = (0, intercept)
        refMat = self.translateMatrix(*trans)
        slope = atan(slope)
        refMat = np.dot(self.rotateMatrix(-slope), refMat)
        refMat = np.dot(self.scaleMatrix(1, -1), refMat)
        refMat = np.dot(self.rotateMatrix(slope), refMat)
        refMat = np.dot(self.translateMatrix(*trans_), refMat)
        """if slope == inf:
            refMat[0][0] = -1
        else:
            refMat[1][1] = -1
            if slope != 0:
                refMat[1][1] = -1
                theta = atan(slope)
                refMat = np.dot(self.rotateMatrix(theta), refMat)
                refMat = np.dot(refMat, self.rotateMatrix(-theta))
        if intercept == 0:
            return refMat
        elif slope ==inf:
            refMat = np.dot(self.translateMatrix(intercept), refMat)
            refMat = np.dot(refMat, self.translateMatrix(-intercept))
        else:
            refMat = np.dot(self.translateMatrix(0, intercept), refMat)
            refMat = np.dot(refMat, self.translateMatrix(0, -intercept))"""
        
        return refMat

    def getIdentityMatrix(self):
        """Identity Matrix."""
        return np.identity(3, dtype="float")

    def __str__(self):
        """Text maker."""
        return super().__str__()
