import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm 

result = []
for _ in range(100000):

    a = random.randint(0,9)
    result.append(a)

#print(result)
plt.hist(result, bins=10, density=True, alpha=0.8, color='purple', edgecolor='black')
plt.show()