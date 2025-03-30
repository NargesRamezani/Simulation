import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm 

result = []
before_four = []
for i in range(500000):
    a = random.randint(0,9)
    result.append(a)

    if result[i]==4:
        if i == 0:
            continue
        else:
            before_four.append(result[i-1])

#print(result)
#print(before_four)
plt.hist(before_four, bins=10, density=True, alpha=0.55, color='purple', edgecolor='black')
plt.show()