from Drawables.Drawable import Drawable
from math import inf, pi
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1)
a = Drawable()

r = a.reftectionMatrix(inf, 2)

print(r)

arr = np.reshape((1,2,1), (3,1))
print(arr)

x = np.dot(r,arr)

print(x)

