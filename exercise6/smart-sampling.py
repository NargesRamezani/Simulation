import random
import numpy as np

N = 100000
a, b = 0, 2


p = 0
y_max = 1
for i in range(N):
    x = random.uniform(a, b)
    y = random.uniform(0, y_max)
    f_x = np.exp(-x**2)
    if y <= f_x:
        p += 1

I = y_max * (b - a) * (p / N)
print("simple sampling: ", I)



def exp_restricted():
    while True:
        u = random.uniform(0, 1)
        x = -np.log( u * (1 - np.exp(-2)))  
        if 0 <= x <= 2:
            return x


Z = 1 - np.exp(-2)  

k = 0
for j in range(N):
    x = exp_restricted()
    f_x = np.exp(-x**2)
    g_x = (np.exp(-x))   
    k += f_x / g_x

J = Z*(k / N)
print("smart sampling: ", J)


'''x = np.arange(0, 2, 0.001)
y = np.exp(-x**2)

plt.plot(x, y, color='blue')
plt.grid(True) 
plt.legend() 
plt.show()'''