import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.optimize import curve_fit

L = 10
P = [0.5, 0.55, 0.59]
max_cells = 400
stop_position = (L - 1, L - 1)

def compute_radius_of_gyration(cluster_points):
    if len(cluster_points) == 0:
        return 0
    cluster_points = np.array(cluster_points)
    center_of_mass_x = np.mean(cluster_points[:, 0])
    center_of_mass_y = np.mean(cluster_points[:, 1])
    squared_distances = []
    for point in cluster_points:
        dx = point[0] - center_of_mass_x
        dy = point[1] - center_of_mass_y
        squared_distances.append(dx**2 + dy**2)
    return np.sqrt(np.mean(squared_distances))

result = {}

for p in P:
    min_S = []
    min_radius = []
    for _ in range(150):
        grid = np.zeros((L, L), dtype=int)
        grid[L//2, L//2] = 1
        where = [(L//2, L//2)]
        
        while where:
            new_cells = []
            for i in where:
                neighbors = [(i[0] - 1, i[1]), (i[0], i[1] - 1),
                            (i[0] + 1, i[1]), (i[0], i[1] + 1)]
                for j in neighbors:
                    if 0 <= j[0] < L and 0 <= j[1] < L:
                        if grid[j] == 0 and random.uniform(0, 1) < p:
                            grid[j] = 1
                            new_cells.append(j)
                            if j == stop_position:
                                where = []
                                break
                        elif grid[j] == 0:
                            grid[j] = -1
            where = new_cells
            if not where:
                break

        cluster_points = np.argwhere(grid == 1)
        radius_of_gyration = float(compute_radius_of_gyration(cluster_points))
        cluster_area = np.count_nonzero(grid == 1)

        min_S.append(cluster_area)
        min_radius.append(radius_of_gyration)

    result[p] = [np.average(min_S), np.average(min_radius)]

print(result)

S_values = np.array([result[p][0] for p in result])
Rg_values = np.array([result[p][1] for p in result])

log_S = np.log(S_values)
log_Rg = np.log(Rg_values)

def linear_model(x, a, b):
    return a * x + b

params, covariance = curve_fit(linear_model, log_Rg, log_S)
a_fit, b_fit = params

log_Rg_fit = np.linspace(min(log_Rg), max(log_Rg), 100)
log_S_fit = linear_model(log_Rg_fit, a_fit, b_fit)


plt.scatter(log_Rg, log_S, color='red', label="Data Points")
plt.plot(log_Rg_fit, log_S_fit, color='blue', linestyle='--', label=f"Fit: y = {a_fit:.2f}x + {b_fit:.2f}")
plt.xlabel("log(Rg)")
plt.ylabel("log(S)")
plt.title("Log-Log Plot of Cluster Area vs Radius of Gyration")
plt.legend()
plt.grid(True)
plt.show()

'''cmap = ListedColormap(["white", "pink"])  
plt.imshow(final_grid, cmap=cmap, origin="upper")
plt.grid(False)
plt.show()'''

'''cmap = ListedColormap(["white", "pink"])  
plt.imshow(final_grid, cmap=cmap, origin="upper")
plt.grid(False)
plt.show()'''
