import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return x - np.tan(x)

def fprime(x):
    return 1.0 - (np.cos(x))**-2

x = 0.0
tol = 10**-5
xvalues = [x, ]

for i in range(1, 1000):
    xnew= x - (f(x)/fprime(x))
    dif = np.abs(xnew - x)    
    print(i, xnew)
    xvalues.append(xnew)
    
    if dif <= tol:
        print(xnew, " is converged value")
        break
    
    x = xnew
    
    
    
xspace = np.arange(-2, 2, 0.1)

plt.plot(xspace, f(xspace), label = "Actual function")
#plt.plot(xvalues, f(xvalues), label = "Path of root finding")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("f(x) vs x")
plt.xlim(-1, 1)

plt.legend()
plt.show()























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    