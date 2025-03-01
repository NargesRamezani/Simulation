import matplotlib.pyplot as plt
import random
import numpy as np
import math

w = 200  
n = 40000  
batch_size = 10000
num_batches = math.ceil(n / batch_size)

height = np.zeros(w, dtype=int)
max_height = 250
grid = np.zeros((max_height, w), dtype=int) 
layer_color = np.zeros(w, dtype=int)  

for batch in range(num_batches):
    color = 1 if batch % 2 == 0 else 2  

    particles = batch_size if (batch + 1) * batch_size <= n else (n % batch_size)

    for _ in range(particles):
        x = random.randint(0, w - 1)
        y = height[x]

        grid[y, x] = color  
        height[x] += 1
        layer_color[x] = color  


cmap = plt.matplotlib.colors.ListedColormap(["white", "blue", "red"])

plt.figure(figsize=(10, 6))
plt.pcolormesh(grid, cmap=cmap, edgecolors="none")  
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Ballistic Deposition")
plt.show()
