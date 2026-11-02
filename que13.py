
import numpy as np
from scipy.integrate import quad
from scipy.optimize import approx_fprime

def f(x):
    return 2*x**2-5*x+8

integral,_ = quad(f,0,3)
print(f"Integration result: {integral:.2f}")

derivative = approx_fprime(3.0,f,1e-6)
print(f"Derivative at x=3: {derivative[0]:.2f}")
