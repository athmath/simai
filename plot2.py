import matplotlib.pyplot as plt
import numpy as np

th=np.arange(1000)*2*np.pi/1000

def r(theta):
    return(1/(1+max(abs(np.cos(theta)), abs(np.sin(theta)))))

x = [r(theta)*np.cos(theta) for theta in th]
y = [r(theta)*np.sin(theta) for theta in th]

plt.plot(x, y)
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.axis('equal')
plt.show()