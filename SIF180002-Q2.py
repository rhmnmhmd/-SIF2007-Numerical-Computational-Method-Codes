import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import sympy as sym

m = 60.0
c = 1.3
g = 9.81

def f(t, v):
    return (-c/m)*v + g

def func(t):
    answer = (-g*m/c)*np.exp(-c*t/m) + (g*m/c)
    return answer
    
v = 0.0
t = 0.0
h = 7
tspace = [t, ]
vspace = [v, ]
i = 0

while t < 200.0:
    print(i, t, v)
    v = v + h*f(t, v)
    t = t + h
    i = i + 1
    tspace.append(t)
    vspace.append(v)
        
plt.plot(tspace, vspace, "x", label = "Numerical Solution")

xvalues = np.arange(0.0, 200.0, 0.1)
plt.plot(xvalues, func(xvalues), label = "Analytical Solution")

plt.xlabel("t")
plt.ylabel("v(t)")
plt.title("v(t) vs t")
plt.legend()
plt.style.use("dark_background")

plt.show()




































