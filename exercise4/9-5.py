import numpy as np
import matplotlib.pyplot as plt

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def count_self_avoiding_walks(N, x=0, y=0, visited=None):
    if visited is None:
        visited = set()
    
    if N == 0:
        return 1
    
    visited.add((x, y))
    count = 0
    
    for dx, dy in DIRECTIONS:
        new_x, new_y = x + dx, y + dy
        if (new_x, new_y) not in visited:  
            count += count_self_avoiding_walks(N - 1, new_x, new_y, visited.copy()) 
    
    return count


max_N = 15 
saw = [count_self_avoiding_walks(N) for N in range(1, max_N + 1)]

free_walk = [4**N for N in range(1, max_N + 1)]

ratios = [saw[i] / free_walk[i] for i in range(len(saw))]

plt.figure(figsize=(10, 5))
plt.plot(range(1, max_N + 1), saw , marker='o', label="Self-Avoiding Walks")
plt.plot(range(1, max_N + 1), free_walk, marker='s', linestyle="dashed", label="Free Walks (4^N)")
plt.xlabel("Step Length (N)")
plt.ylabel("Number of Walks")
plt.title("Number of Self-Avoiding Walks vs. Free Walks")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(range(1, max_N + 1), ratios, marker='o', color='red')
plt.xlabel("Step Length (N)")
plt.ylabel("SAW / Free Walk")
plt.title("Ratio of Self-Avoiding Walks to Free Walks")
plt.grid()
plt.show()
