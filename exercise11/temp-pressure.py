import numpy as np
import pandas as pd

# Parameters
N = 100
k_B = 1.380649e-23  # Boltzmann constant (J/K)
epsilon = 1.65e-21   # LJ potential depth (J)
m = 39.95 * 1.6605e-27  # Mass of Argon (kg)

# Load data
df = pd.read_csv('E:\\Physics\\4S\\cp\\template\\exercise11\\trajectory (4).csv')

# Calculate mean squared velocity
vx = df['vx'].values
vy = df['vy'].values
mean_v_squared = np.mean(vx**2 + vy**2)

# Convert to physical units
v_squared_physical = mean_v_squared * (epsilon / m)

# Compute temperature (2D system)
T = (m * v_squared_physical) / (2 * k_B)

print(f"System Temperature: {T:.2f} K")