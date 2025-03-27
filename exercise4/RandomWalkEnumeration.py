import numpy as np
import matplotlib.pyplot as plt


p = 0.6  
q = 1 - p  
x_left = -10
x_right = 10
x_range = np.arange(x_left, x_right + 1)  

T_max = 100  
prob = np.zeros(len(x_range))  
prob[len(x_range) // 2] = 1  
trap_left_prob = 0
trap_right_prob = 0

survival_prob = []

for t in range(T_max):
    new_prob = np.zeros_like(prob)  
    for i in range(1, len(x_range) - 1):
        new_prob[i] = p * prob[i - 1] + q * prob[i + 1]
    
    
    trap_left_prob += prob[0]  
    trap_right_prob += prob[-1]  
    new_prob[0] = 0
    new_prob[-1] = 0

    survival_prob.append(np.sum(new_prob))

    prob = new_prob.copy()


mean_lifetime = np.sum(survival_prob)

