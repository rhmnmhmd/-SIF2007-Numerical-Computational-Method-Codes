import numpy as np
import matplotlib.pyplot as plt
import math

def f(t, v):
    m = 60
    c = 1.3
    g = 9.8
    return (-c/m)*v + g

#def func(t):
    return -np.exp(-t) + 1
    
v0 = 0.0
t0 = 0.0
n = 10
h = 1/n
tspace = [t0, ]
vspace = [v0, ]

for i in range(0, n):
    print(t0, v0)
    vi = v0 + h*f(t0, v0)
    t0 = t0 + h
    tspace.append(t0)
    vspace.append(vi)
    v0 = vi
    
plt.plot(xspace, yspace, label = "Numerical Solution")

#xvalues = np.arange(0, 1.0, 0.01)
#plt.plot(xvalues, func(xvalues), label = "Analytical Solution")

plt.xlabel("t")
plt.ylabel("v(t)")
plt.title("v(t) vs t")
plt.legend()
plt.style.use("dark_background")

plt.show()

