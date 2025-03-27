import random
import numpy as np
import matplotlib.pyplot as plt

p = 0.5
q = 1 - p  
l = 1  
N = 100   
iteration = 1  

position = np.zeros((N, 2), dtype=int)
side_memory = []  

def random_walk(x, y):
    direction = random.choice(["x", "y"])
    if direction == "x":
        if random.uniform(0, 1) > p:
            x += l
        else:
            x -= l
    else:
        if random.uniform(0, 1) > p:
            y += l
        else:
            y -= l

    return [x, y]

x, y = 0, 0  
for step in range(N):
    
    neighbors = [[x + l, y], [x - l, y], [x, y + l], [x, y - l]]
    if all(neighbor in side_memory for neighbor in neighbors):  
        print(f"Stopped at step {step} due to dead end.")  
        break  

    new_position = random_walk(x, y)  
    while new_position in side_memory:  
        new_position = random_walk(x, y)  
    
    position[step] = new_position
    side_memory.append(new_position) 
    x, y = new_position  


valid_steps = len(side_memory)
position = np.array(side_memory)[:valid_steps]  


plt.plot(position[:, 0], position[:, 1], marker="o", linestyle="-")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Self-Avoiding Random Walk with Dead End Check")
plt.grid()
plt.show()
