#Importing modules etc
import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import sympy as sym

#Defining the best fit curve function. f(t)
def f(t):
    return 1545.39 * np.e**(-0.0154*t)

#Reading Excel data into Spyder
data = pd.read_excel("Data.xlsx")

#Given data
t = data.t
R = data.R

#input space for f(t)
x = np.arange(60, 140, 0.1)

#Plotting
plt.plot(t, R, label = "Given data")
plt.plot(x, f(x), label = "Best fit curve, R = 1545.39e^(-0.0154t)")

#Labels
plt.title("Plot of Rate of decay, R (decay/min) vs time, t (min)")
plt.ylabel("R")
plt.xlabel("t")
plt.legend()

#Styling
plt.style.use("dark_background")

#Saving figure
plt.savefig("Linear Regression Plots", dpi = 1200)



plt.show()







































