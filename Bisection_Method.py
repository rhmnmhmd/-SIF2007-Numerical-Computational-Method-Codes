import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x - np.cos(x)

a = 0.0
b = 1.0
tol = 10**-6

if f(a)*f(b) < 0:
    
    for i in range(1000):
        c = (a + b)/2
        
        if f(a)*f(c) < 0:
            b = c
        
        elif f(c)*f(b) < 0:
            a = c
    
        dif = np.abs(b - a)
        
        if dif < tol:
            root = (a + b)/2
            print("The root is ", root )
            break
        
else:
    print("The root is on interval's end or there is no root in the interval")








































