import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.power(x, 3) - 6*np.power(x, 2) - 11*x - 6.1

xspace = np.arange(-20, 20, 0.01)

plt.plot(xspace, f(xspace))

plt.ylim(-90, 20)
plt.xlim(-10, 15)

plt.vlines(x = 0, ymin = -100, ymax = 20, color = "k")
plt.hlines(y = 0, xmin = -10, xmax = 15, color = "k")


plt.title("Plot of f(x) = x^3 - 6x^2 - 11x - 6.1")
plt.ylabel("f(x)")
plt.xlabel("x")








plt.show()






































