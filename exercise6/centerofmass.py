import random
import numpy as np
import matplotlib.pyplot as plt

R = 2
a, b = -R, R
N = 1000
rho_0 = 5

p = 0
m = 0
for _ in range(N):
    x = random.uniform(a , b)
    y = random.uniform(a, b)
    z = random.uniform(a, b)
    rho = random.uniform(0, rho_0) 
    f_R = np.sqrt(x**2 + y**2 + z**2)
    rho_z = ((rho_0 / (4 * R)) * z + (3/4) * rho_0)*z
    M = (rho_0 / (4 * R)) * z + (3/4) * rho_0
    if f_R <= R and rho <= rho_z :
        p+=1
    if f_R <= R and rho <= M:
        m+=1

I = (b - a)**3 *(p/N)
J = (b - a)**3 *(m/N)
print(I/J)
