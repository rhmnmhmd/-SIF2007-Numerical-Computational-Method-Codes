import numpy as np
import matplotlib.pyplot as plt
import math

def f(t, N):
    return -34.65*(t**-0.5)*np.exp(-0.693*(t**0.5))

def func(t):
    return 100*np.exp(-t)
    
N0 = 100.0
t0 = 0.001
h = 0.4
tspace = [t0, ]
Nspace = [N0, ]
print(t0, N0)
print("t", "N", "absolute error")

while t0 <= 4.0:
    N0 = N0 + h*f(t0, N0)
    t0 = t0 + h
    tspace.append(t0)
    Nspace.append(N0)
    abserror = np.abs(func(t0) - N0)
    print(t0, N0, abserror)
    
plt.plot(tspace, Nspace, label = "Numerical Solution")

xvalues = np.arange(0, 4.0, 0.01)
plt.plot(xvalues, func(xvalues), label = "Analytical Solution")

plt.xlabel("t")
plt.ylabel("N(t)")
plt.title("N(t) vs t")
plt.legend()

plt.show()
