import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from collections import Counter


N = 100
result = []
for _ in range(N):
    a = random.randint(0,9)
    result.append(a)


#print(result)
plt.hist(result, bins=10, density=True, alpha=0.8, color='purple', edgecolor='black')
plt.title(f'N = {N}', fontsize=14)
plt.show()


''' 
N_values = list(range(1, 101)) + list(range(10, 50001, 500)) + [100000]
sigma_over_N= []
theoretical_values = []

for N in N_values:
    numbers = []
    for _ in range(N):
        a = random.randint(0,9)
        numbers.append(a)

    
    freq = []
    for i in range(10):
        count = numbers.count(i)
        freq.append(count / N)
    freq = np.array(freq)

    sigma = np.std(freq)
    sigma_over_N.append(sigma)
    
    
    theoretical_values.append(np.sqrt(0.09/N))


plt.figure(figsize=(12, 6))
plt.plot(N_values, sigma_over_N, 'bo-', label='σ/N')
plt.plot(N_values, theoretical_values, 'r--', label='1/N^0.5')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N (log scale)')
plt.ylabel('σ (log scale)')
plt.title('Convergence of Standard Deviation (σ) for Uniform Distribution')
plt.legend()
plt.grid(True)
plt.show()'''