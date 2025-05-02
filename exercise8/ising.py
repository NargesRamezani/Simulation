import random
import numpy as np
import matplotlib.pyplot as plt


import numpy as np
import matplotlib.pyplot as plt
import random
import math


L = 50
kBT = 1
J_values = np.linspace(0, 2.0, 20)
N = 50000
plot_interval = 1000

def get_neighbors(s, i, j, L):
    return [
        s[i, (j + 1) % L],  
        s[i, (j - 1) % L],  
        s[(i + 1) % L, j],  
        s[(i - 1) % L, j]]

def calculate_deltaE(s, i, j, L, J):
    neighbors = get_neighbors(s, i, j, L)
    return -2 * J * s[i, j] * sum(neighbors)

def calculate_total_energy(s, L, J):

    energy = 0
    for i in range(L):
        for j in range(L):
            neighbors = get_neighbors(s, i, j, L)
            energy += -J * s[i, j] * sum(neighbors)
    return energy / 2

def calculate_magnetization(s):
    return np.abs(np.mean(s))

final_magnetizations = []
magnet=[]
for J in J_values:

    s = np.random.choice([-1, 1], size=(L, L))
    total_energy = calculate_total_energy(s, L, J)
    magnetization = calculate_magnetization(s)

    data = {'steps': [], 'magnetizations': [], 'energies': []}

    for step in range(N):

        i, j = random.randint(0, L-1), random.randint(0, L-1)


        deltaE = calculate_deltaE(s, i, j, L, J)


        if deltaE <= 0 or random.random() < math.exp(-deltaE / kBT):
            s[i, j] *= -1
            total_energy += deltaE
            magnet.append(calculate_magnetization(s))

    
    
    final_magnetizations.append(calculate_magnetization(magnet))

    
    '''data['steps'].append(step)
    data['magnetizations'].append(calculate_magnetization(s))
    data['energies'].append(total_energy)


    plt.imshow(s, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title(f"J={J:.2f}, Step={step}, M={data['magnetizations'][-1]:.2f}")
    plt.colorbar()
    plt.show()'''

plt.figure(figsize=(8, 5))
plt.plot(J_values, final_magnetizations, 'o-', markersize=8, linewidth=2)
plt.xlabel("Coupling Strength (J)", fontsize=12)
plt.ylabel("Final Magnetization", fontsize=12)
plt.title("Magnetization vs. J (kBT=1)", fontsize=14)
plt.grid(True)
plt.show()