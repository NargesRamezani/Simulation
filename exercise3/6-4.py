import numpy as np
import random
import matplotlib.pyplot as plt

sizes = [10, 20, 40 , 80 , 160]
n = 100
probabilities = np.linspace(0, 1, 20)

def find(x, equivalences):
    if equivalences.get(x, x) != x:
        equivalences[x] = find(equivalences[x], equivalences)
    return equivalences.get(x, x)

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

plt.figure(figsize=(8, 6))

for L in sizes:
    correlation_lengths = []
    for p in probabilities:
        radii_values = []
        for _ in range(n):
            radii_of_gyration = []
            whole = np.zeros((L, L+1), dtype=int)
            whole[:, 0] = 1
            equivalences = {}
            index = 2
            
            for x in range(L):
                for y in range(L):
                    l = random.choices([0, 1], weights=[1-p, p], k=1)[0]
                    if l == 1:
                        neighbors = []
                        if y > 0 and whole[y-1, x+1] > 0:
                            neighbors.append(find(whole[y-1, x+1], equivalences))
                        if x > 0 and whole[y, x] > 0:
                            neighbors.append(find(whole[y, x], equivalences))
                        
                        if not neighbors:
                            whole[y, x+1] = index
                            equivalences[index] = index
                            index += 1
                        else:
                            min_index = min(neighbors)
                            whole[y, x+1] = min_index
                            for neighbor in neighbors:
                                equivalences[find(neighbor, equivalences)] = min_index
            
            for x in range(L):
                for y in range(L):
                    if whole[y, x+1] > 0:
                        whole[y, x+1] = find(whole[y, x+1], equivalences)
            
            whole = whole[:, 1:]
            first_column = whole[:, 0]
            last_column = whole[:, -1]
            percolates = any(fc == lc and fc > 0 for fc in first_column for lc in last_column)
            
            cluster_points = {}
            for y in range(L):
                for x in range(L):
                    label = whole[y, x]
                    if label > 0:
                        if label not in cluster_points:
                            cluster_points[label] = []
                        cluster_points[label].append((x, y))
            
            if percolates:
                infinite_cluster = set(first_column) & set(last_column)
            else:
                infinite_cluster = set()
            
            for label, points in cluster_points.items():
                if label not in infinite_cluster:
                    radii_of_gyration.append(compute_radius_of_gyration(points))
        
            if radii_of_gyration:
                radii_values.append(np.mean(radii_of_gyration))
            else:
                radii_values.append(0)  
        
        correlation_lengths.append(np.mean(radii_values))  
    plt.plot(probabilities, correlation_lengths, marker='o', linestyle='-', label=f'L={L}')

plt.xlabel('p')
plt.ylabel('Correlation Length')
plt.title('Percolation Correlation Length vs p')
plt.legend()
plt.grid()
plt.show()