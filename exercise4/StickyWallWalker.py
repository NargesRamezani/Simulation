import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm 

p = 0.6  
q = 1 - p  
l = 1  
N = 500  
iteration = 50 
x_stopright = 10  
x_stopleft = -10

x_result = np.zeros(iteration)  
n_stop = np.zeros(iteration)  

for i in range(iteration):
    x = 0  
    for step in range(N):
        if random.random() > p:
            x += l
        else:
            x -= l
        if x == x_stopleft or x == x_stopright: 
            n_stop[i] = step + 1  
            break
    x_result[i] = x

print( n_stop)


'''theory_mean = N*l*(q - p)
theory_variance = 4 *(l**2) * N*p*q
mean = np.mean(result)
variance = np.var(result)

print ('theory mean: ' , theory_mean , ' mean: ' , mean)
print ('theory variance: ' , theory_variance , ' variance: ' , variance)
'''