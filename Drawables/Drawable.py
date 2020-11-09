import numpy as np
from math import sin, cos, inf, atan

class Drawable(object):
    """description of class"""

    res = {}

    def __init__(self):
        object.__init__(self)
        # super().__init__()

    def rotateMatrix(self, rotation:float=0):
        s = sin(rotation)
        c = cos(rotation)
        id = self.getIdentityMatrix()
        id[0][0] = c
        id[0][1] = -s
        id[1][0] = s
        id[1][1] = c
        return id

    def translateMatrix(self, tx:float=0, ty:float=0):
        id = self.getIdentityMatrix()
        id[0][2] = tx
        id[1][2] = ty
        return id

    def scaleMatrix(self, sx:float=1, sy:float=1):
        id = self.getIdentityMatrix()
        id[0][0] = sx
        id[1][1] = sy
        return id

    def shearMatrix(self, shx:float=0,shy:float=0):
        id = self.getIdentityMatrix()
        id[0][1] = shx
        id[1][0] = shy
        return id

    def reftectionMatrix(self, slope:float=0, intercept:float=0):
        refMat = self.getIdentityMatrix()
        if slope == inf:
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
            refMat = np.dot(refMat, self.translateMatrix(0, -intercept))
        return refMat

    def getIdentityMatrix(self):
        return np.identity(3, dtype="float")

    def __str__(self):
        return super().__str__()
"""


def main():
    with open("Drawables/res.json") as res:
        Drawable.res = readRes(res.read())
"""
