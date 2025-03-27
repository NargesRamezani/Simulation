import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

#for circular random boundary condition run first part and for square condition run second part
p = 0.5
l = 1
grid_size = 100
num_particles = 700


x_min, x_max = -200, grid_size + 500
y_min, y_max = -200, grid_size + 500

grid = np.zeros((grid_size, grid_size), dtype=int)
grid[grid_size//2, grid_size//2] = 1  

for i in range(1, num_particles + 1):

    r = grid_size
    theta = random.uniform(0 , 2*np.pi)
    x , y = int(r*np.cos(theta)) , int(r*np.sin(theta))


    
    '''random_direction= random.choice(["0", "1" , "2" , "3"])
    if random_direction == "0":
        x, y = 0 , random.randint(0, grid_size-1)
    if random_direction == "1":
        x, y = random.randint(0, grid_size-1), 0
    if random_direction == "2" :
        x, y = grid_size-2 , random.randint(0, grid_size-1)
    if random_direction == "3":
        x, y = random.randint(0, grid_size-1), grid_size-2'''  

    
    while True:
        
        if x < x_min or x >= x_max or y < y_min or y >= y_max:
            break  
        
        if 0 <= x < grid_size and 0 <= y < grid_size:
            if (y > 0 and grid[y-1, x] > 0) or \
            (x > 0 and grid[y, x-1] > 0) or \
            (x < grid_size-1 and grid[y, x+1] > 0) or \
            (y < grid_size-1 and grid[y+1, x] > 0):
                grid[y, x] = i  
                break
        
        
        direction = random.choice(["x", "y"])
        if direction == "x":
            x += l if random.random() > p else -l
        else:
            y += l if random.random() > p else -l

colors = ['white'] + [plt.cm.rainbow(k) for k in np.linspace(0, 1, 255)]
cmap_custom = ListedColormap(colors)


plt.figure(figsize=(10, 10))
plt.imshow(grid, cmap=cmap_custom, origin='lower', vmin=0, vmax=num_particles)
plt.show()

