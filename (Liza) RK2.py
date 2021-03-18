import numpy as np
import matplotlib.pyplot as plt
import math

def f(x, y):
    return 1.0 - y

def func(x):
    return -np.exp(-x) + 1

x0 = 0
y0 = 0
n = 20
h = 1/n

xi = x0
yi = y0

xspace = [xi, ]
yspace = [yi, ]

for i in range (0, n):
    print(i, xi, yi)
    K1 = f(xi, yi)
    K2 = f(xi + h, yi + h*f(xi, yi))
    yi = yi + (h/2)*(K1 + K2)
    xi = xi + h
    xspace.append(xi)
    yspace.append(yi)

plt.plot(xspace, yspace, "ko", label = "RK2")

xvalues = np.arange(0, 1.0, 0.01)
plt.plot(xvalues, func(xvalues), label = "Analytical Solution")

plt.legend()



plt.show()

































