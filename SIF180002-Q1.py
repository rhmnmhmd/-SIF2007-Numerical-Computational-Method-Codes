import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import sympy as sym

def f(t):
    answer = 2.6293*t - 2.2822
    return answer
    
data = pd.read_excel("linearregression.xlsx")

x = data.x
F = data.F

tspace = np.arange(1.0, 13.0, 0.01)

plt.plot(tspace, f(tspace), label = "Linear Regression")
plt.scatter(x, F, label = "Actual Data Points", color = "red")

plt.title("Plot of F (N) vs x (cm)")
plt.xlabel("Elongation, x (cm)")
plt.ylabel("Force, F (N)")
plt.legend()

plt.show()



































