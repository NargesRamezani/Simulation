import numpy as np
import pandas as pd

df = pd.read_csv('E:\\Physics\\4S\\cp\\template\\exercise11\\trajectory (4).csv')
N = 100
steps = sorted(df['step'].unique())

velocity_data = {step: {'vx': [], 'vy': []} for step in steps}

for _, row in df.iterrows():
    step = int(row['step'])
    velocity_data[step]['vx'].append(row['vx'])
    velocity_data[step]['vy'].append(row['vy'])

for step in velocity_data:
    velocity_data[step]['vx'] = np.array(velocity_data[step]['vx'])
    velocity_data[step]['vy'] = np.array(velocity_data[step]['vy'])

def calculate_vac(velocity_data, max_tau=150):
    vx0 = velocity_data[0]['vx']
    vy0 = velocity_data[0]['vy']
    normalization = np.mean(vx0**2 + vy0**2)
    vac = []
    for tau in range(max_tau + 1):
        corr_sum = 0
        count = 0
        
        for t in range(len(steps)-tau):
            vx_t = velocity_data[steps[t]]['vx']
            vy_t = velocity_data[steps[t]]['vy']
            vx_tau = velocity_data[steps[t + tau]]['vx']
            vy_tau = velocity_data[steps[t + tau]]['vy']
            
            corr_sum += np.sum(vx_t * vx_tau + vy_t * vy_tau)
            count += len(vx_t)
        
        vac.append(corr_sum / (count * normalization))
    
    return vac

vac = calculate_vac(velocity_data)
tau = list(range(len(vac)))


import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.plot(tau, vac, 'o-')
plt.xlabel('Time Lag (τ)')
plt.ylabel('Normalized Velocity Autocorrelation')
plt.title('Velocity Autocorrelation')
plt.grid(True)
plt.show()