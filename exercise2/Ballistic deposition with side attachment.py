import matplotlib.pyplot as plt
import numpy as np
import random
import math

w = 100  
n = 800  
batch_size = 500
num_batches = math.ceil(n / batch_size)

height = np.zeros(w, dtype=int)
max_height = 200
grid = np.zeros((max_height, w), dtype=int) 

for batch in range(num_batches):
    color = 1 if batch % 2 == 0 else 2  

    particles = batch_size if (batch + 1) * batch_size <= n else (n % batch_size)

    for _ in range(particles):
        x = random.randint(0, w - 1)
        y = height[x]


        if x == 0:
            left_x = w - 1 
        else:
            left_x = x - 1  
        if x == w - 1:
            right_x = 0  
        else:
            right_x = x + 1 

        

        max_height_neighbors = max(height[left_x], height[right_x])


        y = max(y, max_height_neighbors-1)


        y = min(y, max_height - 1)

        grid[y, x] = color  
        height[x] = y +1

cmap = plt.matplotlib.colors.ListedColormap(["white", "blue", "red"])

plt.figure(figsize=(10, 6))
plt.pcolormesh(grid, cmap=cmap, edgecolors="none")  
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Ballistic Deposition (Periodic Boundaries)")
plt.show()
