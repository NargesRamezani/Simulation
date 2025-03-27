import numpy as np
import matplotlib.pyplot as plt


p = 0.5  
q = 1 - p  
x_left = -10  
x_right = 10 
x_range = np.arange(x_left, x_right + 1)
N = 1000  
start_positions = np.arange(-9, 10)

results =[]

for start in start_positions:
    prob = np.zeros(len(x_range))
    initial = np.where(x_range == start)[0][0]
    prob[initial] = 1.0
    survival_prob = [1.0]  
    left_trap_prob = []
    right_trap_prob = []

    for t in range(1, N + 1):
        new_prob = np.zeros_like(prob)
        
        
        for i in range(1, len(x_range) - 1):
            new_prob[i] = p * prob[i - 1] + q * prob[i + 1]
        
        
        left_absorb = q * prob[1]
        right_absorb = p * prob[-2]
        
        left_trap_prob.append(left_absorb)
        right_trap_prob.append(right_absorb)
        
        
        total = left_absorb + right_absorb
        survival_prob.append(survival_prob[-1] - total)
        
        prob = new_prob.copy()
        
        if survival_prob[-1] < 10**(-6):
            break

    mean_lifetime = np.sum(survival_prob)
    results.append((start, mean_lifetime))

    print(f"Start position: {start}, Mean lifetime: {mean_lifetime:.2f}")


positions = [r[0] for r in results]
lifetimes = [r[1] for r in results]


plt.figure(figsize=(12, 6))
plt.plot(positions, lifetimes, 'bo-')
plt.xlabel('Starting Position')
plt.ylabel('Mean Lifetime (time steps)')
plt.title('Effect of Starting Position on Particle Lifetime')
plt.xticks(positions)
plt.grid(True)
plt.show()
