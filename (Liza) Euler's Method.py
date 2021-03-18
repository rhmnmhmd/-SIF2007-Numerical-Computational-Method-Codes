import numpy as np
import matplotlib.pyplot as plt
import math

def f(x, y):
    return 1.0 - y

def func(x):
    return -np.exp(-x) + 1
    
y0 = 0.0
x0 = 0.0
n = 5
h = 1/n
xspace = [x0, ]
yspace = [y0, ]

for i in range(0, n):
    print(x0, y0)
    yi = y0 + h*f(x0, y0)
    x0 = x0 + h
    xspace.append(x0)
    yspace.append(yi)
    y0 = yi
    
plt.plot(xspace, yspace, label = "Numerical Solution")

xvalues = np.arange(0, 1.0, 0.01)
plt.plot(xvalues, func(xvalues), label = "Analytical Solution")

plt.xlabel("x")
plt.ylabel("y")
plt.title("y(x) vs x")
plt.legend()

plt.show()






























