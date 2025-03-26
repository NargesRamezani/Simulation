import random
import numpy as np
import matplotlib.pyplot as plt


p = 0.5 
q = 1 - p  
l = 1  
N = 10  
iteration = 1  


x_positions = np.zeros(N)
y_positions = np.zeros(N)


x, y = 0, 0  
for step in range(N):
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
    x_positions[step] = x
    y_positions[step] = y


print(x_positions)
print(y_positions)

plt.figure(figsize=(8, 8))
plt.plot(x_positions, y_positions, marker="o", markersize=2, linestyle="-", alpha=0.7)


plt.scatter(0, 0, color="red", label="Start", zorder=3, s=100, edgecolors="black") 
plt.scatter(x_positions[-1], y_positions[-1], color="blue", label="End", zorder=3, s=100, edgecolors="black")  
plt.gca().set_aspect('equal', adjustable='datalim') 
plt.xlim(min(x_positions) - 5, max(x_positions) + 5)
plt.ylim(min(y_positions) - 5, max(y_positions) + 5)


plt.grid(True, linestyle="--", alpha=0.6)
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("2D Random Walk")
plt.legend()
plt.show()