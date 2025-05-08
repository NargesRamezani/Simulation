import numpy as np
import matplotlib.pyplot as plt
import random
import math
from scipy.optimize import curve_fit

kBT = 1.0  
J_values = np.linspace(0.35, 0.55, 20)  
L_values = [ 50]  # 10, 20,
steps_per_L = { 50: 6000000}  #  10: 200000, 20: 500000,
sample_interval = 5000
samples_per_J = 20
l_max = 20

Jc = 0.4407
nu_theory = 1  

def get_neighbors(s, i, j, L):
    return [s[i, (j + 1) % L],
        s[i, (j - 1) % L],
        s[(i + 1) % L, j],
        s[(i - 1) % L, j]]

def deltaE(s, i, j, L, J):
    return 2 * J * s[i, j] * sum(get_neighbors(s, i, j, L))

def correlation(s, L, max_dist):
    c = np.zeros(max_dist)
    m = np.mean(s)
    v = np.var(s)
    if v == 0:
        return c
    
    for l in range(1, max_dist + 1):
        val = 0
        for i in range(L):
            for j in range(L):
                val += s[i, j] * s[i, (j + l) % L]
        c[l - 1] = (val / (L * L) - m * m) / v
    return c

def decay(x, a, xi):
    return a * np.exp(-x / xi)

corr_lengths = {L: [] for L in L_values}


for L in L_values:
    print(f"L = {L}...")
    N = steps_per_L[L]
    
    for J in J_values:
        s = np.random.choice([-1, 1], size=(L, L))
        
        
        for _ in range(N // 2):
            i, j = random.randint(0, L - 1), random.randint(0, L - 1)
            dE = deltaE(s, i, j, L, J)
            if dE <= 0 or random.random() < math.exp(-dE / kBT):
                s[i, j] *= -1
        samples = []
        for _ in range(samples_per_J):
            for __ in range(sample_interval):
                i, j = random.randint(0, L - 1), random.randint(0, L - 1)
                dE = deltaE(s, i, j, L, J)
                if dE <= 0 or random.random() < math.exp(-dE / kBT):
                    s[i, j] *= -1
            samples.append(s.copy())
        
        c_total = np.zeros(l_max)
        for config in samples:
            c_total += correlation(config, L, l_max)
        c_avg = c_total / len(samples)
        l_vals = np.arange(1, l_max + 1)
        try:
            popt, _ = curve_fit(decay, l_vals, c_avg, p0=[1.0, 1.0], maxfev=5000)
            corr_lengths[L].append(popt[1])
        except:
            corr_lengths[L].append(np.nan)
        print(f"J = {J:.3f}, ξ = {corr_lengths[L][-1]:.3f}")

plt.figure(figsize=(12, 7))
for L in L_values:
    plt.plot(J_values, corr_lengths[L], 'o-', label=f"L={L}", markersize=5)
plt.axvline(Jc, color='r', linestyle='--', label=f'  $J_c$ = {Jc}')
plt.xlabel("(J)", fontsize=14)
plt.ylabel("  (ξ)", fontsize=14)
plt.title("  (ξ) vs J  ", fontsize=16)
plt.legend(fontsize=12)
plt.grid(alpha=0.3)
plt.show()


def powerlaw(J, a, nu, Jc):
    return a * np.abs(J - Jc) ** (-nu)

plt.figure(figsize=(12, 7))
for L in L_values:
    xi_vals = np.array(corr_lengths[L])
    mask = np.isfinite(xi_vals)
    J_masked =J_values[mask]
    xi_masked = xi_vals[mask]
    
    for side, color in [('left', 'blue'), ('right', 'green')]:
        if side =='left':
            mask_side = J_masked < Jc
            label= f'L={L}, J<Jc'
        else:
            mask_side = J_masked > Jc
            label = f'L={L}, J>Jc'
        
        if np.sum(mask_side) < 3:
            continue
            
        try:
            popt, pcov = curve_fit(lambda J, a, nu: powerlaw(J, a, nu, Jc),
                                J_masked[mask_side], xi_masked[mask_side],
                                p0=[1.0, 1.0])
            plt.plot(J_masked[mask_side], xi_masked[mask_side], 'o', color=color)
            plt.plot(J_masked[mask_side], powerlaw(J_masked[mask_side], *popt, Jc),
                    '--', color=color, label=f'{label}, ν={popt[1]:.2f}±{np.sqrt(pcov[1,1]):.2f}')
        except Exception as e:
            print(f" error    L={L}, {side}: {str(e)}")

plt.axvline(Jc, color='r', linestyle='--', label=f'$J_c$ = {Jc}')
plt.xlabel("J", fontsize=14)
plt.ylabel("ξ", fontsize=14)
plt.title("nu " , fontsize=16)
plt.legend(fontsize=12)
plt.grid(alpha=0.3)
plt.show()