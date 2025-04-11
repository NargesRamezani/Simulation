import random
import numpy as np

R = 10
a, b = -R, R
N = 1000000
rho_0 = 1
rho_max = rho_0

mass = 0
moment_z = 0

for _ in range(N):
    x = random.uniform(a, b)
    y = random.uniform(a, b)
    z = random.uniform(a, b)
    if x**2 + y**2 + z**2 > R**2:
        continue

    rho_rand = random.uniform(0, rho_max)
    rho_z = (rho_0 / (4 * R)) * z + (3 / 4) * rho_0

    if rho_rand <= rho_z:
        mass += rho_z
        moment_z += rho_z * z

volume = (b - a)**3
estimated_mass = (volume / N) * mass
estimated_moment_z = (volume / N) * moment_z

z_cm = (estimated_moment_z / estimated_mass)/R

print(f"Center of mass (z): {z_cm:.4f} R")
