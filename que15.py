from scipy.optimize import minimize

def func(v):
    x,y = v
    return (x-2)**2 + (y-2)**2

guess = [0.0 , 0.0]

result = minimize(func, guess)

print(f"Minimum value occurs at: x = {result.x[0]:.2f}, y = {result.x[1]:.2f}")
print(f"Minimum function value: {result.fun:.2f}")