import numpy as np
import matplotlib.pyplot as plt

#defining function
def f(theta, a):
    return a*np.sin(theta)

#x-axis space
theta = np.arange(0, 2*np.pi, 0.01)

#Plotting
plt.subplot(221)
plt.plot(theta, f(theta, 1), label = "a =1", color = "r")
plt.ylim(-5, 5)
plt.legend()

plt.subplot(222)
plt.plot(theta, f(theta, 2), label = "a = 2", color = "g")
plt.ylim(-5, 5)
plt.legend()

plt.subplot(223)
plt.plot(theta, f(theta, 3), label = "a = 3", color = "b")
plt.ylim(-5, 5)
plt.legend()

plt.subplot(224)
plt.plot(theta, f(theta, 4), label = "a = 4", color = "m")
plt.ylim(-5, 5)
plt.legend()


plt.suptitle("Graph of a*sin($\phi$) vs $\phi$")
plt.style.use("dark_background")
plt.show()








































