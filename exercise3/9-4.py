import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

L = 10
#P = np.arange(0.5, 0.7, 0.001).tolist()

P=[0.618]

result = {}

for p in P:
    grid = np.zeros((L, L), dtype=int)
    for i in range(L):
        for j in range(L):
            if random.uniform(0, 1) < p:
                grid[i, j] = 1

    new_L = L // 2
    new_grid = np.zeros((new_L, new_L), dtype=int)

    for i in range(0, L, 2):
        for j in range(0, L, 2):
            subgrid = grid[i:i+2, j:j+2]  
            count = np.sum(subgrid)  

            if count == 4:  
                new_grid[i//2, j//2] = 1
            elif count == 3:  
                new_grid[i//2, j//2] = 1
            elif count == 2:
                if np.array_equal(subgrid, [[1, 1], [0, 0]]) or np.array_equal(subgrid, [[0, 0], [1, 1]]):
                    new_grid[i//2, j//2] = 1  


    p_prime = np.sum(new_grid) / (new_L * new_L)
    p_calculated = round((p**4 + (4 * p**3 * (1 - p)) + (2 * p**2 * (1 - p)**2)), 3)
    p = round(p, 3)
    result[p] = (round(p_calculated, 3), round(float(p_prime), 3))

    colors = ['white', 'blue']
    custom_cmap = mcolors.ListedColormap(colors)

    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap=custom_cmap, vmin=0, vmax=1, interpolation='none')
    plt.title(f'Initial Grid (p = {p})')
    plt.show()

    plt.figure(figsize=(6, 6))
    plt.imshow(new_grid, cmap=custom_cmap, vmin=0, vmax=1, interpolation='none')
    plt.title(f'Transformed Grid (p = {p})')
    plt.show()

fixed_point = None
for p, (p_calculated, p_prime) in result.items():
    if abs(p - p_calculated) < 0.000001:  
        fixed_point = p
        break


