from Drawables.Drawable import Drawable
from math import inf, pi
import numpy as np

a = Drawable()

r = a.reftectionMatrix(inf, 2)

print(r)

arr = np.reshape((1,2,1), (3,1))
print(arr)

x = np.dot(r,arr)

print(x)