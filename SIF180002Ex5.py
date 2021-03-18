import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 2*np.pi, 0.1)
y = np.tan(t)

plt.plot(t, y)
plt.ylabel("y")
plt.xlabel("t")   
plt.title("Graph of f(t) = tan(t)")     
plt.ylim(-10, 10)
                     
plt.show()

