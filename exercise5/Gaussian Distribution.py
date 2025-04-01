import numpy as np
import matplotlib.pyplot as plt


N = 10000  
sigma = 1  
m = 0  

U1 = np.random.rand(N)
U2 = np.random.rand(N)

R = np.sqrt(-2 *(sigma**2)* np.log(U1))
theta = 2 * np.pi * U2

Z1 = R* np.cos(theta) + m
Z2 = R* np.sin(theta) + m

plt.hist(Z1, bins=50, density=True, alpha=0.6, color='b', label='Z1')
plt.hist(Z2, bins=50, density=True, alpha=0.6, color='r', label='Z2')
plt.legend()
plt.title("Histogram of Generated Gaussian Numbers")
plt.show()
