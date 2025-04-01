import random
import numpy as np
import matplotlib.pyplot as plt


N = 1000
result = []


for _ in range(10000):
    k=0
    for i in range(N):
        a = random.randint(0,9)
        k += a
    result.append(k)

#print(result)
plt.hist(result, bins=10, density=True, alpha=0.8, color='purple', edgecolor='black')
plt.show()