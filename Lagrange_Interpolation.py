import math
import numpy as np
import matplotlib.pyplot as plt

#Defining the fucntion and polynomials
def f(x):
    return np.sin(np.pi*x/2)

def p_2(x):
    return -0.8282*x**2 + 1.8284*x

def p_4(x):
    return 0.1728*x**4 - 0.7851*x**3 + 0.0468*x**2 + 1.5655*x


#independent variable
xspace = np.arange(0, 2*np.pi, 0.05)
x_2 = np.arange(0, 1, 0.05)
x_4 = np.arange(0, 1, 0.05)


#Plotting
plt.plot(xspace, f(xspace), color = "r", label = "f(x)")
plt.plot(x_2, p_2(x_2), label = "p_2(x)")
plt.plot(x_4, p_4(x_4), label = "p_4(x)")


#x and y limit
plt.xlim(0, 1.1)
plt.ylim(0, 1.2)


#Labelling
plt.legend()
plt.title("Plot of f(x) = sin($\pi$x/2) and its Lagrange Interpolation ")
plt.ylabel("f(x)")
plt.xlabel("x")


#Styling
plt.style.use("dark_background")


#Save figure
plt.savefig("Lagrange_Interpoaltion_Plots", dpi = 1200)





plt.show()









































