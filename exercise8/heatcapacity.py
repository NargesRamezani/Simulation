import numpy as np
import matplotlib.pyplot as plt
import random
import math

kBT = 1
J_values = np.linspace(0, 1, 10)
plot_interval = 1000

L_values = [10, 15, 20, 25,50]
steps_per_L = {
    10: 100000,
    15: 400000,
    20: 800000,
    25: 3000000,
    50: 10000000}

def get_neighbors(s, i, j, L):
    return [s[i, (j + 1) % L],
        s[i, (j - 1) % L],
        s[(i + 1) % L, j],
        s[(i - 1) % L, j]]

def calculate_deltaE(s, i, j, L, J):
    neighbors = get_neighbors(s, i, j, L)
    return 2 * J * s[i, j] * sum(neighbors)

def calculate_total_energy(s, L, J):
    energy = 0
    for i in range(L):
        for j in range(L):
            neighbors = get_neighbors(s, i, j, L)
            energy += -J * s[i, j] * sum(neighbors)
    return energy / 2

def calculate_magnetization(s):
    return np.abs(np.mean(s))

def variance(E):
    return np.var(E)

results_m = {}
results_C = {}

for L in L_values:
    N = steps_per_L[L]
    final_magnetizations = []
    heat_capacities = []

    for J in J_values:
        magnet = []
        energy = []

        s = np.random.choice([-1, 1], size=(L, L))
        total_energy = calculate_total_energy(s, L, J)

        for step in range(N):
            i, j = random.randint(0, L - 1), random.randint(0, L - 1)
            deltaE = calculate_deltaE(s, i, j, L, J)

            if deltaE <= 0 or random.random() < math.exp(-deltaE / kBT):
                s[i, j] *= -1
                total_energy += deltaE
                if step >= N / 2:
                    magnet.append(calculate_magnetization(s))
                    energy.append(total_energy)

        final_magnetizations.append(np.mean(magnet))
        heat_capacities.append(variance(energy) / (kBT**2))

    results_m[L] = final_magnetizations
    results_C[L] = heat_capacities


plt.figure(figsize=(8, 5))
for L in L_values:
    plt.plot(J_values, results_m[L], 'o-', label=f"L={L}")
plt.xlabel("Coupling Strength (J)", fontsize=12)
plt.ylabel("Final Magnetization", fontsize=12)
plt.title("Magnetization vs. J", fontsize=14)
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
for L in L_values:
    plt.plot(J_values, results_C[L], 'o-', label=f"L={L}")
plt.xlabel("Coupling Strength (J)", fontsize=12)
plt.ylabel("Heat Capacity", fontsize=12)
plt.title("Heat Capacity vs. J", fontsize=14)
plt.legend()
plt.grid(True)
plt.show()