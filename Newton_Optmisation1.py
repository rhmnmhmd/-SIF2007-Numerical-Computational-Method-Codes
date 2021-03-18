import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (np.power(x, 2)/10) - 2*np.sin(x)

def fprime(x):
    return x/5 - 2*np.cos(x)

def fpprime(x):
    return 1/5 + 2*np.sin(x)

x = 0
tol = 10**-3
xvalues = [x, ]

for i in range(1, 1000):
    xnew= x - ( fprime(x)/fpprime(x) )
    dif = np.abs(xnew - x)    
    print(i, xnew)
    xvalues.append(xnew)
    
    if dif < tol:
        print(xnew, " is converged value")
        break
    
    x = xnew

xspace = np.arange(0, 7, 0.01)
plt.plot(xspace, f(xspace), label = "Target Function")

plt.plot(xvalues, f(xvalues), label = "Converged")

plt.title("f(x) vs x")
plt.legend()

plt.xlabel("x")
plt.ylabel("f(x)")

#plt.xlim(0, 2)
#plt.ylim(-2, 0)

plt.style.use("dark_background")

#plt.savefig("x=4", dpi = 1500)

plt.show()





















