import random
import numpy as np
import matplotlib.pyplot as plt

p = 0.5
l = 1  
N = 500  
iteration = 10000
x_stopright = 10  
x_stopleft = -10
lifetime = {}

for j in range(-9 , 10):
    x_result = np.zeros(iteration)  
    n_stop = np.zeros(iteration)  
    for i in range(iteration):
        x = j  
        for step in range(N):
            if random.random() > p:
                x += l
            else:
                x -= l
            if x == x_stopleft or x == x_stopright: 
                n_stop[i] = step + 1  
                break
        x_result[i] = x

    mean_life = np.mean(n_stop)
    #print( mean_life)

    lifetime[j] = float(mean_life)
print(lifetime)


plt.figure(figsize=(12, 6))
plt.plot(lifetime.keys(), lifetime.values(), 'bo-', markersize=8)
plt.xlabel('Starting Position (x)', fontsize=14)
plt.ylabel('Mean Lifetime (steps)', fontsize=14)
plt.title('Effect of Starting Position on Particle Lifetime (Monte Carlo)', fontsize=16)
plt.xticks(range(-9, 10))
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


