import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import math
import sympy as sym

a = float(input("Please enter value for a = "))
b = float(input("Please enter value for b = "))
c = float(input("Please enter value for c = "))

discr = pow(b, 2) - 4*a*c

if discr < 0:
    x_1 = str(-b/(2*a) + np.sqrt(abs(discr))/(2*a)
    x_2 = 
elif discr == 0:
    x_1 = x_2 = -b/(2*a)
elif discr > 0:
    x_1 = (-b + np.sqrt(discr)) / (2*a)
    x_2 = (-b - np.sqrt(discr)) / (2*a)
else:
    print("Invalid input")
    
print("x_1 = ", x_1)
print("x_2 = ", x_2)





















