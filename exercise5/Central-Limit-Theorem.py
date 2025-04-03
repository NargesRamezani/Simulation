import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

N_values = [5]
colors = ['pink']

plt.figure(figsize=(10, 6))

for N, color in zip(N_values, colors):
    result = []
    for _ in range(100000):
        k = 0
        for i in range(N):
            a = random.randint(0, 9)
            k += a
        result.append(k)

    plt.hist(result, bins=20, density=True, alpha=0.8, color=color, edgecolor='black')

    mu, std = norm.fit(result)

    x = np.linspace(min(result), max(result), 100)
    pdf = norm.pdf(x, mu, std)
    plt.plot(x, pdf, 'b-', linewidth=2)

    plt.legend([f'N = {N}',
                f'Gaussian Fit: μ={mu:.1f}, σ={std:.1f}',
                f'Theoretical: μ={N*4.5}, σ={np.sqrt(N*8.25):.1f}'])

plt.title(f'Distribution of Sums for N={N}')
plt.xlabel('Sum Value')
plt.ylabel('Density')
plt.grid(True)
plt.show()
