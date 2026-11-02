import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def poly2(x,a,b,c):
    return a*x**2 + b*x + c

x = np.array([1,2,3,4,5,6])
y = np.array([16,17,34,57,86,121])

popt,_ = curve_fit(poly2,x,y)
a,b,c = popt
print(f"Estimated co-efficients: a={a:.0f} ,b={b:.0f} ,c={c:.0f}")

plt.scatter(x,y,color='red',label='Original Data')
plt.plot(x,poly2(x,a,b,c),label='fitted curve',color='blue')
plt.title("Polynomial Curve Fitting")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()