import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap



'''اینجا ران نگییییییر! ممنون'''
p = 0.5
l = 1
grid_size = 150
num_particles = 70000

grid = np.zeros((grid_size, grid_size), dtype=int)
grid[1, :] = 1  

for i in range(num_particles):
    x, y = random.randint(0, grid_size-1), grid_size-2  
    
    while True:
        x = np.clip(x, 0, grid_size-1)
        y = np.clip(y, 0, grid_size-1)
        
        
        if (y > 0 and grid[y-1, x] == 1) or \
        (x > 0 and grid[y, x-1] == 1) or \
        (x < grid_size-1 and grid[y, x+1] == 1) or \
        (y < grid_size-1 and grid[y+1, x] == 1):
            grid[y, x] = 1  
            break
            
        
        direction = random.choice(["x", "y"])
        if direction == "x":
            x += l if random.random() > p else -l
        else:
            y += l if random.random() > p else -l
        
        
        if y < -100 or y >= (grid_size+200) or x < -100 or x >= (grid_size+200):
            break

colors = ['white'] + [plt.cm.rainbow(i) for i in np.linspace(0, 1, 255)]
cmap_custom = ListedColormap(colors)


plt.figure(figsize=(10, 10))
plt.imshow(grid, cmap=cmap_custom, origin='lower', vmin=0, vmax=1)
plt.colorbar(label='attachment')
plt.show()