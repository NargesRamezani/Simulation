import numpy as np
import matplotlib.pyplot as plt

x_0 = 0.5
R = np.linspace(0, 1, 500)
N= 10000
x = np.zeros(N)
result = {}

for r in R:
    x[0] = x_0
    for i in range(1, N):
        x[i] = 4*r* x[i-1]*(1 - x[i-1])

        if 1000 <= i <=1100:
            if r not in result:
                result[r] = []
            result[r].append(x[i])

bifurcation_points = []
prev_branches = 1  
for r in sorted(result.keys()):
    unique_x = np.unique(np.round(result[r], 8))
    current_branches = len(unique_x)
    
    if current_branches > prev_branches:
        bifurcation_points.append((r, current_branches))
        prev_branches = current_branches
        

for i, (r, branches) in enumerate(bifurcation_points[:20]):  
    print(f"{i+1}. r = {r:.6f} - {branches} ")

r_values = []
x_values = []
for r in sorted(result.keys()):
    for x_val in result[r]:
        r_values.append(r)
        x_values.append(x_val)
        


plt.figure(figsize=(12, 6))
plt.plot(r_values, x_values, 'k.', markersize=2, alpha=0.6)
plt.xlabel('r', fontsize=14)
plt.ylabel('x (iterations 1000-1100)', fontsize=14)
plt.title('Logistic Map Bifurcation Diagram (r = 0 to 1)', fontsize=16)
plt.grid(True, alpha=0.3)
plt.show()

'''
def chaotic_r(r, x_01=0.5, x_02 = 0.5001, N=500 , threshold=0.01):

    chaotic_R = []

    for R in r:
        x1, x2 = x_01, x_02
        diff = 0
        for j in range(N):
            x1 = 4 * R * x1 * (1 - x1)
            x2 = 4 * R * x2 * (1 - x2)
            current_diff = abs(x1 - x2)
            if current_diff > diff:
                diff = current_diff
        if diff > threshold:
            chaotic_R.append(float(R))
    
    return chaotic_R

r = np.linspace(0.7, 1.0, 300)  

chaotic_r_values = chaotic_r(r)

print("r: ")
print(chaotic_r_values[0], "...")  
'''