import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 2*np.pi, 0.1)
y = np.sin(t)
z = np.exp(t)

plt.subplot(131)
plt.plot(t, y)
plt.ylabel("y")
plt.xlabel("t")  
plt.title("Graph of f(t) = sin(t) and z(t) = e^t")   
plt.style.use("dark_background")

plt.subplot(133)
plt.plot(t, z)
plt.ylabel("y")
plt.xlabel("t")   
plt.title("Graph of f(t) = sin(t) and z(t) = e^t")     
plt.style.use("dark_background")
                    
plt.show()































