import numpy as np
import matplotlib.pyplot as plt

v = 3
x0, y0 = 2, 2.5
x1 = 20
y1=5
tlower=(x1-x0)/v
tupper=np.sqrt(1+(y1-y0)**2/(x1-x0)**2)*(x1-x0)/v
t = np.linspace(tlower, tupper, 500)

x = (1/(2*np.pi)) * ((y1-y0)/np.sqrt((y1-y0)**2+(x1-x0)**2) * v*t +x0*np.arctan((y1-y0)/(x1-x0)))
y = (1/(2*np.pi)) * (1-(x1-x0)/np.sqrt((y1-y0)**2+(x1-x0)**2) * v*t +y0*np.arctan((y1-y0)/(x1-x0)))


plt.plot(x, y)
plt.xlabel("x [m]")
plt.ylabel("y [m]")
#plt.axis("equal")
plt.grid()
plt.show()