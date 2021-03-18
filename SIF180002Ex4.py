import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 2*np.pi, 0.1)
y = np.cos(t)

plt.plot(t, y)
plt.ylabel("y")
plt.xlabel("t")   
plt.title("Graph of f(t) = cos(t)")     
         
               
plt.show()

