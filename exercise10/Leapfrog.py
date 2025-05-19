import numpy as np
import matplotlib.pyplot as plt


theta_0 = np.pi * 6 / 180
omega_0 = 0
L = 1 #m
g = 9.8 #m/s2
T = 5 #s
m = 1 #Kg
N = 10000
h = T/N

theta = np.zeros(N)
omega = np.zeros(N)
t = np.linspace(0, T, N)

theta[0] = theta_0
omega[0] = omega_0

omega_half = omega[0] - 0-5*(g/L)*np.sin(theta[0])*h

for i in range(1, N):
    theta[i] = theta[i-1] + omega_half*h
    omega_full = omega_half- 0.5*(g/L)*np.sin(theta[i])*h
    omega[i] = omega_full
    omega_half = omega_full- 0.5*(g/L)*np.sin(theta[i])*h


kinetic_energy = 0.5*m*L**2*omega**2
potential_energy = m*g*L*(1 - np.cos(theta))
energy = kinetic_energy + potential_energy

plt.figure(figsize=(8,8))

#theta vs time
plt.subplot(2, 2, 1)
plt.plot(t, theta)
plt.xlabel('Time (s)')
plt.ylabel('θ (rad)')
plt.title('Angle vs Time')
plt.grid(True)

#omega vs time
plt.subplot(2, 2, 2)
plt.plot(t, omega)
plt.xlabel('Time (s)')
plt.ylabel('ω (rad/s)')
plt.title('Angular Velocity vs Time')
plt.grid(True)

#phase diagram
plt.subplot(2, 2, 3)
plt.plot(theta, omega)
plt.xlabel('θ (rad)')
plt.ylabel('ω (rad/s)')
plt.title('Phase Space Diagram')
plt.grid(True)

#energy
plt.subplot(2, 2, 4)
plt.plot(t, energy)
plt.xlabel('Time (s)')
plt.ylabel('Total Energy (J)')
plt.title('Energy Conservation')
plt.grid(True)

plt.tight_layout()
plt.show()
