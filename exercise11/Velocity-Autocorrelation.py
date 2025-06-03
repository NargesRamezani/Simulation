import numpy as np
import pandas as pd
from scipy.integrate import cumulative_trapezoid
import matplotlib.pyplot as plt


df = pd.read_csv('E:\\Physics\\4S\\cp\\template\\exercise11\\trajectory (4).csv')
N = 100
d = 2  
dt = 0.001
steps = sorted(df['step'].unique())

sigma = 3.4e-10  # m
epsilon = 1.65e-21  # J
m = 39.95 * 1.6605e-27  # kg
tau_LJ = sigma * np.sqrt(m / epsilon)
velocity_data = {step: {'vx': [], 'vy': []} for step in steps}

for _, row in df.iterrows():
    step = int(row['step'])
    velocity_data[step]['vx'].append(row['vx'])
    velocity_data[step]['vy'].append(row['vy'])

for step in velocity_data:
    velocity_data[step]['vx'] = np.array(velocity_data[step]['vx'])
    velocity_data[step]['vy'] = np.array(velocity_data[step]['vy'])

def calculate_vac(velocity_data, max_tau=300):
    vx0 = velocity_data[steps[0]]['vx']
    vy0 = velocity_data[steps[0]]['vy']
    normalization = np.mean(vx0**2+vy0**2)
    vac = []
    
    for tau in range(max_tau + 1):
        corr_sum = 0
        count = 0
        
        for t in range(len(steps)-tau):
            vx_t = velocity_data[steps[t]]['vx']
            vy_t = velocity_data[steps[t]]['vy']
            vx_tau = velocity_data[steps[t+tau]]['vx']
            vy_tau = velocity_data[steps[t+tau]]['vy']
            
            corr_sum += np.sum(vx_t * vx_tau +vy_t * vy_tau)
            count += len(vx_t)
        
        vac.append(corr_sum / (count*normalization))
    
    return vac

vac = calculate_vac(velocity_data)
tau = np.arange(len(vac)) * dt

integral = cumulative_trapezoid(vac, x=tau, initial=0)
D = integral[-1] / d
D_real = D * (sigma**2 / tau_LJ)  

print(f"D(m²/s): {D_real:.2e}")

'''plt.figure(figsize=(10, 6))
plt.plot(tau, vac, 'b-', linewidth=1.5)
plt.xlabel('Time Lag (τ) [ps]', fontsize=12)
plt.ylabel('Normalized VACF', fontsize=12)
plt.title('Velocity Autocorrelation Function', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()'''