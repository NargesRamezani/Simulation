import random
import numpy as np
import matplotlib.pyplot as plt
import time

seed = int(time.time())
x = [seed]
before_four = []
result = [seed%10]
a = 1664525
c = 1013904223
m = 2**31 
N = 1000

def LCG(x_n):
    x_nn = ((a*x_n) + c) % m
    return x_nn

def second_last(a):
    return (a // 10) % 10

for i in range(N):
    x_nn = LCG(x[i])
    x_m = second_last(x_nn)
    x.append(x_nn)
    result.append(x_m)

    if result[i]==4:
        if i == 0:
            continue
        else:
            before_four.append(result[i-1])

#print(result)
plt.hist(result, bins=10, density=True, alpha=0.8, color='purple', edgecolor='black')
plt.title(f'N = {N}')
plt.show()
plt.hist(before_four, bins=10, density=True, alpha=0.55, color='purple', edgecolor='black')
plt.title(f'distribution of numbers before 4 for N = {N}')
plt.show()
