import random
import numpy as np
import matplotlib.pyplot as plt

p = 0.5  
l = 1  
N = 100  
iterations = 5000 

r_squared_avg = np.zeros(N)  

for _ in range(iterations):
    x, y = 0, 0  
    
    for step in range(N):
        if random.uniform(0, 1) > p:
            x += l  
        else:
            x -= l  
        
        if random.uniform(0, 1) > p:
            y += l  
        else:
            y -= l  

        r_squared_avg[step] += x**2 + y**2  

r_squared_avg /= iterations


plt.figure(figsize=(8, 6))
plt.plot(range(N), r_squared_avg, label="Simulation ⟨r²⟩")
plt.plot(range(N), 2*np.arange(N), linestyle="--", label="Theory (2t)", color="red")
plt.xlabel("Number of Steps (t)")
plt.ylabel("⟨r²⟩")
plt.legend()
plt.grid(True)
plt.show()