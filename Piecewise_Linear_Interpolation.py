import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.rcParams['text.usetex'] = False

#Actual function
def f(x):
    return (25*(x**2)+1)**-1


#Piecewise parts
def q_0(x):
    return 0.1116*x + 0.1501

def q_1(x):
    return 0.286*x + 0.2809

def q_2(x):
    return 1.7242*x + 1.0

def q_3(x):
    return -1.7242*x + 1.0

def q_4(x):
    return -0.286*x + 0.2809

def q_5(x):
    return -0.1116*x + 0.1501


#independent variable space
xspace = np.arange(-1, 1, 0.001)
x_0 = np.arange(-1, -0.75, 0.001)
x_1 = np.arange(-0.75, -0.5, 0.001)
x_2 = np.arange(-0.5, 0, 0.001)
x_3 = np.arange(0, 0.5, 0.001)
x_4 = np.arange(0.5, 0.75, 0.001)
x_5 = np.arange(0.75, 1, 0.001)

#Plotting
plt.plot(xspace, f(xspace), label = "f(x)")
plt.plot(x_0, q_0(x_0), label = "q_0(x)")
plt.plot(x_1, q_1(x_1), label = "q_1(x)")
plt.plot(x_2, q_2(x_2), label = "q_2(x)")
plt.plot(x_3, q_3(x_3), label = "q_3(x)")
plt.plot(x_4, q_4(x_4), label = "q_4(x)")
plt.plot(x_5, q_5(x_5), label = "q_5(x)")

#Labelling
plt.title("Graph of f(x) = 1/(25x^2 + 1)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()


plt.style.use("dark_background")
#plt.savefig("Mine.png", dpi = 1200)



plt.show(True)
