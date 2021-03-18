import numpy as np
import matplotlib.pyplot as plt

#defining function
def f(phi, a, w):
    return -a*pow(w, 2)*np.sin(phi)

#x-axis space
phi = np.arange(0, 2*np.pi, 0.01)

#Plotting
plt.subplot(221)
plt.plot(phi, f(phi, 1, 1), label = "a =1", color = "r")
plt.ylim(-5, 5)
plt.legend()

plt.subplot(222)
plt.plot(phi, f(phi, 2, 1), label = "a = 2", color = "g")
plt.ylim(-5, 5)
plt.legend()

plt.subplot(223)
plt.plot(phi, f(phi, 3, 1), label = "a = 3", color = "b")
plt.ylim(-5, 5)
plt.legend()

plt.subplot(224)
plt.plot(phi, f(phi, 4, 1), label = "a = 4", color = "m")
plt.ylim(-5, 5)
plt.legend()


plt.style.use("dark_background")
plt.suptitle("Graph of -a$\omega^2$sin($\phi$) vs $\phi$")
plt.show()


