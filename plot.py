import matplotlib.pyplot as plt
import numpy as np

n=20000
x=np.random.uniform(-1,1,n)
y=np.random.uniform(-1,1,n)

def f(x,y):
    r=np.sqrt(x**2+y**2)
    d=min(1-np.abs(x), 1-abs(y))
    if r<=d:
        return 0 
    else:
        return 1

values = np.array([f(xi,yi) for xi, yi in zip(x,y)])
colors = np.where(values>0, 'red', 'blue')

p=sum(values)/n
print(p)

plt.scatter(x, y, c=colors, s=3)
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.axis('equal')
plt.show()

