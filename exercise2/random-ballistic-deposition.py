import matplotlib.pyplot as plt
import random
import numpy as np
import math

w = 200  
n = 800000 
batch_size = 2000
num_batches = math.ceil(n / batch_size)
max_height = 5000
grid = np.zeros((max_height, w), dtype=int) 
layer_color = np.zeros(w, dtype=int)  
log_times = [int(10 * 2**i) for i in range(int(math.log2(n//10)) + 1)]
d={}
h=[]

for i in range(1):
    height = np.zeros(w, dtype=int)
    index = 0
    roughness = []  
    times = []  



    for batch in range(num_batches):
        color = 1 if batch % 2 == 0 else 2  

        particles = batch_size if (batch + 1) * batch_size <= n else (n % batch_size)

        for _ in range(particles):
            x = random.randint(0, w - 1)
            y = height[x]

            grid[y, x] = color  
            height[x] += 1
            layer_color[x] = color
            


            real_time = batch * batch_size + _ + 1
            if index < len(log_times) and real_time == log_times[index]:
                mean_height = np.mean(height)
                roughness_value = np.sqrt(np.mean(height**2) - mean_height**2)  
                h.append([real_time,float(mean_height) , float(roughness_value)])
                if roughness_value > 0:  
                    roughness.append(roughness_value)
                    times.append(real_time)
                

                    key = int(np.log(real_time))
                    if key in d:
                        d[key].append(float(roughness_value))  
                    else:
                        d[key] = [float(roughness_value)]  

                index += 1



            
print(h)

ln_time = sorted(d.keys())
mean_ln_roughness = [float(np.mean(np.log(d[key]))) for key in ln_time]

time = np.exp(ln_time)  
mean_roughness = [float(np.mean(d[key])) for key in ln_time]



#plt.scatter(time, mean_roughness, color='blue', label='')
#plt.plot(time, fit_line(time), color='red', label=f'Fit: y = {coef[0]:.4f}x  {coef[1]:.4f}')

coef = np.polyfit(ln_time, mean_ln_roughness, 1) 
fit_line = np.poly1d(coef) 


plt.scatter(ln_time, mean_ln_roughness, color='blue', label='Data')
plt.plot(ln_time, fit_line(ln_time), color='red', label=f'Fit: y = {coef[0]:.4f}x  {coef[1]:.4f}')

plt.xlabel('ln(Time)')
plt.ylabel('ln(Roughness)')
plt.title('log-log Plot of Surface Roughness vs. Time')
plt.legend()
plt.grid(True)
plt.show()

#If you want to see the dynamics of the model, run this part.
'''cmap = plt.matplotlib.colors.ListedColormap(["white", "blue", "red"])

plt.figure(figsize=(10, 6))
plt.pcolormesh(grid, cmap=cmap, edgecolors="none")  
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Ballistic Deposition")
plt.show()'''
