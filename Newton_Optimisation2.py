import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.power(x, 2) - 2*x + 2

xspace = np.arange(-2, 2, 0.01)

plt.plot(xspace, f(xspace))

plt.hlines(y = 0)
plt.vlines(x = 0, ymin = 0, ymax = 10, color = "r")



























