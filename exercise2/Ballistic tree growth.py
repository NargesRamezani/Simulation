import matplotlib.pyplot as plt
import numpy as np
import random
import math


w = 200  
n = 18500
batch_size = 800
num_batches = math.ceil(n / batch_size)

height = np.zeros(w, dtype=int)  
max_height = 250
grid = np.zeros((max_height, w), dtype=int)  


x0 = w // 2  
y0 = 0
grid[y0, x0] = 1  
height[x0] = y0 + 1  


k = x0
active_sites = {k}  
active_sites.add(x0)
log_times = [int(10 * 2**i) for i in range(int(math.log2(n//10)) + 1)]


widths = []
times = []

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

        left_h = height[left_x]
        right_h = height[right_x]
        current_h = height[x]

        if left_h == 0 and right_h == 0 and current_h == 0:
            continue  


        y = max(y , max_height_neighbors -1)
        y = min(y, max_height - 1)

        
        grid[y, x] = color  
        height[x] = y + 1
        active_sites.add(x)
        active_sites.add(left_x)
        active_sites.add(right_x)


    min_x = min(active_sites)
    max_x = max(active_sites)
    center_x = (min_x + max_x) / 2 
    width = (max_x - min_x) 



    widths.append(width)
    times.append((batch + 1) * batch_size)




ln_times = np.log(times)
ln_widths = np.log(widths)


coef = np.polyfit(ln_times, ln_widths, 1)
fit_line = np.poly1d(coef)


plt.figure(figsize=(7, 5))
plt.scatter(ln_times, ln_widths, color='blue', label='Data')
plt.plot(ln_times, fit_line(ln_times), color='red', linestyle='--', label=f'Fit: y = {coef[0]:.4f}x  {coef[1]:.4f}')

plt.xlabel('ln(Time)')
plt.ylabel('ln(Width)')
plt.title('Log-Log Plot of Tree Width vs. Time')
plt.legend()
plt.grid(True)
plt.show()





'''
cmap = plt.matplotlib.colors.ListedColormap(["white", "blue", "red"])

plt.figure(figsize=(7, 7))
plt.pcolormesh(grid, cmap=cmap, edgecolors="none")  
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Tree Growth")
plt.show()'''