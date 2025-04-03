import numpy as np
import matplotlib.pyplot as plt


N = 100000  
sigma = 0.2
m = 0  

U1 = np.random.rand(N)
U2 = np.random.rand(N)

R = np.sqrt(-2 *(sigma**2)* np.log(U1))
theta = 2 * np.pi * U2

x = R* np.cos(theta) + m
y = R* np.sin(theta) + m

plt.hist(x, bins=50, density=True, alpha=0.7, color='b', label="x'")
plt.hist(y, bins=50, density=True, alpha=0.7, color='r', label="y'")
plt.legend()
plt.title(f"Histogram of Generated Gaussian Numbers for N = {N}  (σ = {sigma}) ")
plt.show()
