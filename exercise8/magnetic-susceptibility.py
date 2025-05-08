import numpy as np
import matplotlib.pyplot as plt
import random
import math
from scipy.optimize import curve_fit

kBT = 1
J_values = np.linspace(0, 0.9, 12)
plot_interval = 1000

L_values = [10, 15, 20, 25, 50]
steps_per_L = {
    10: 100000,
    15: 400000,
    20: 900000,
    25: 8000000,}

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
results_ms = {}

for L in L_values:
    N = steps_per_L[L]
    final_magnetizations = []
    magnetic_susceptibility = []

    for J in J_values:
        magnet = []
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
                    

        magnetic_susceptibility.append((L**2 *variance(magnet)) / (kBT))

    results_ms[L] = magnetic_susceptibility


J_c = 0.5 * np.log(1 + np.sqrt(2))
L_vals = []
chi_peaks = []

for L in results_ms:
    chi = results_ms[L]
    max_chi = max(chi)
    L_vals.append(L)
    chi_peaks.append(max_chi)

L_vals = np.array(L_vals)
chi_peaks = np.array(chi_peaks)


def scaling_law(L, gamma_over_nu):
    return L**(gamma_over_nu)

popt, pcov = curve_fit(scaling_law, L_vals, chi_peaks)
gamma_over_nu = popt[0]
gamma = gamma_over_nu  
plt.figure(figsize=(6, 4))
plt.loglog(L_vals, chi_peaks, 'o', label='χ_max (data)')
plt.loglog(L_vals, scaling_law(L_vals, *popt), '--', label=f'Fit: γ ≈ {gamma:.2f}')
plt.xlabel("L (log)")
plt.ylabel("χ_max (log)")
plt.title("Scaling of χ_max ~ L^γ")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



plt.figure(figsize=(8, 5))
for L in L_values:
    plt.plot(J_values, results_ms[L], 'o-', label=f"L={L}")
plt.xlabel("Coupling Strength (J)", fontsize=12)
plt.ylabel("magnetic susceptibility", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()