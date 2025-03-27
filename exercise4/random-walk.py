import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm 

p = 0.6
q = 1 - p
l = 1
N=10000
iteration = 500
result = np.zeros(iteration)

for i in range(iteration):
    x = 0
    for _ in range(N):
        if random.uniform(0 , 1) > p:
            x+=l
        else:
            x-=1
    result[i] = x

theory_mean = N*l*(q - p)
theory_variance = 4 *(l**2) * N*p*q
mean = np.mean(result)
variance = np.var(result)

print ('theory mean: ' , theory_mean , ' mean: ' , mean)
print ('theory variance: ' , theory_variance , ' variance: ' , variance)
#print(result)

plt.hist(result, bins=30, density=True, alpha=0.6, color='b', edgecolor='black')
y = np.linspace(min(result), max(result), 100)  
pdf = norm.pdf(y, mean, np.sqrt(variance))
plt.plot(y, pdf, 'g-', linewidth=1.2, label='Fitted Gaussian')


plt.title('Histogram of Final Positions with Fitted Gaussian')
plt.xlabel('Final Position')
plt.ylabel('Probability Density')
plt.legend()
plt.show()