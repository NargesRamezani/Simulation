import matplotlib.pyplot as plt
import numpy as np
import random


max_height = 200
w = 300
n = 50000

grid = np.zeros((max_height, w), dtype=int) 
height = np.zeros(w, dtype=int)  
time_snapshots = [1000, 5000, 10000, 20000, 50000]  # زمان‌هایی که می‌خواهیم ذخیره کنیم
height_snapshots = {}

for _ in range(n):
    x = random.randint(0, w - 1)  
    y = max_height  
    #print (x  , y)

    if x == 0:
        left_x = w - 1 
    else:
        left_x = x - 1

    while y >= 0 and (y  > height[left_x]):  
        if x == 0:
            left_x = w - 1 
        else:
            left_x = x - 1  
        x=left_x  
        y -= 1  
        

    if 0 <= y < max_height:  
        grid[y, x] = 1
        height[x] = max(height[x], y+1)
        
    #print(f"Particle landed at: x={x}, y={y}")  



    

'''
plt.figure(figsize=(6, 6))
plt.imshow(grid, cmap="Blues", origin="lower")  
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Competitive growth (Periodic Boundaries)")
plt.show()
'''
