import matplotlib.pyplot as plt
import numpy as np
import random
import math

w = 400  
n = 6000000
batch_size = 10000
num_batches = math.ceil(n / batch_size)

height = np.zeros(w, dtype=int)
max_height = 600000
grid = np.zeros((max_height, w), dtype=int) 
d={}



log_times = [int(10 * 3**i) for i in range(int(math.log2(n//10)) + 1)]


total_particles = 0  


for i in range(10):
    height = np.zeros(w, dtype=int)
    current_index = 0
    roughness = []  
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


            y = max(y, max_height_neighbors-1)


            y = min(y, max_height - 1)

            grid[y, x] = color  
            height[x] = y +1


            grid[y, x] = color
            height[x] = y + 1  

            real_time = batch * batch_size + _ + 1
            if current_index < len(log_times) and real_time == log_times[current_index]:
                mean_height = np.mean(height)
                roughness_value = np.sqrt(np.mean(height**2) - mean_height**2)  
                if roughness_value > 0:  
                    roughness.append(roughness_value)
                    times.append(real_time)
                    key = int(np.log(real_time))
                    if key in d:
                        d[key].append(float(roughness_value))  
                    else:
                        d[key] = [float(roughness_value)]  

                current_index += 1



            


ln_time = sorted(d.keys())
mean_ln_roughness = [float(np.mean(np.log(d[key]))) for key in ln_time]



split_time = 12


ln_time_early = [t for t in ln_time if t <= split_time]
roughness_early = [mean_ln_roughness[i] for i, t in enumerate(ln_time) if t <= split_time]

ln_time_late = [t for t in ln_time if t > split_time]
roughness_late = [mean_ln_roughness[i] for i, t in enumerate(ln_time) if t > split_time]


coef_early = np.polyfit(ln_time_early, roughness_early, 1)
fit_early = np.poly1d(coef_early)

mean_roughness_late = np.mean(roughness_late)


plt.figure(figsize=(8, 6))


plt.scatter(ln_time, mean_ln_roughness, color='blue', label='Data')


plt.plot(ln_time_early, fit_early(ln_time_early), color='red', linestyle='--',
        label=f'Linear Fit: y = {coef_early[0]:.4f}x + {coef_early[1]:.4f}')


plt.axhline(mean_roughness_late, color='green', linestyle='--', 
            label=f'Flat Fit: y = {mean_roughness_late:.4f}')

plt.xlabel('ln(Time)')
plt.ylabel('ln(Roughness)')
plt.title('Log-Log Plot of Surface Roughness vs. Time (Two-Fit Model)')
plt.legend()
plt.grid(True)
plt.show()


'''
cmap = plt.matplotlib.colors.ListedColormap(["white", "blue", "red"])

plt.figure(figsize=(7, 6))
plt.pcolormesh(grid, cmap=cmap, edgecolors="none")  
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
'''