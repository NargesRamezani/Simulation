import random
import numpy as np
import matplotlib.pyplot as plt

N = [i for i in range(100 , 8000, 50)]



final_difference = []
a, b = 0, 2
y_max = -np.sqrt(5/3) * (10/3)



for i in N:
    result = []
    difference = []
    for _ in range(50):
        p=0
        for j in range(i):
            x = random.uniform (a, b)
            y = random.uniform ( y_max , 0)
            f_y = x**3 - (5*x)
            if y >= f_y :
                p+=1

        I = y_max*(b - a)*(p/i)
        d = np.abs(-6 - I)
        result.append(float(I))
        difference.append(float(d))
    final_difference.append(np.mean(difference))

print(np.mean(result))
plt.plot(N, final_difference)
plt.xlabel("Number of Samples (N)")
plt.ylabel("Error (|I - Exact Value|)")
plt.title("Error vs Number of Samples")
plt.grid(True)
plt.show()


'''
X = np.arange(0 , 2 , 0.01)
y = X**3 - 5 * X

plt.plot(X, y, label='y = x³ - 5x', color='blue')
plt.grid(True) 
plt.legend() 
plt.show()'''
