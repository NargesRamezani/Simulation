import random
import numpy as np
import matplotlib.pyplot as plt

N = 100000
a, b = 0, 2
y_max = -np.sqrt(5/3) * (10/3)
p=0

for i in range(N):
    x = random.uniform (a, b)
    y = random.uniform (0, y_max)
    f_y = x**3 - (5*x)
    if y >= f_y :
        p+=1

I = y_max*(b - a)*(p/N)
print(I)


'''X = np.arange(0 , 2 , 0.01)
y = X**3 - 5 * X

plt.plot(X, y, label='y = x³ - 5x', color='blue')
plt.grid(True) 
plt.legend() 
plt.show()'''