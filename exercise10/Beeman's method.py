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
a = np.zeros(N)
t = np.linspace(0, T, N)

theta[0] = theta_0
omega[0] = omega_0
a[0] = -(g/L)*np.sin(theta[0])


theta[1] = theta[0] + omega[0] * h + 0.5 * a[0] * h**2
omega[1] = omega[0] + a[0] * h
a[1] = -(g / L) * np.sin(theta[1])


for i in range(1, N):
    theta[i] = theta[i-1] + omega[i-1] * h + (2/3)* a[i-1]* h**2 - (1/6)* a[i-2] * h**2
    a[i] = -(g/L)*np.sin(theta[i])
    omega[i] = omega[i-1] + (1/3)* a[i] *h + (5/6) *a[i-1] *h - (1/6) *a[i-2] *h


kinetic_energy = 0.5*m*L**2*omega**2
potential_energy = m*g*L*(1 - np.cos(theta))
energy = kinetic_energy + potential_energy

plt.figure(figsize=(8,8))

#theta vs time
plt.subplot(1, 3, 1)
plt.plot(t, theta)
plt.xlabel('Time (s)')
plt.ylabel('θ (rad)')
plt.title('Angle vs Time')

#omega vs time
plt.subplot(1, 3, 2)
plt.plot(t, omega)
plt.xlabel('Time (s)')
plt.ylabel('ω (rad/s)')
plt.title('Angular Velocity vs Time')

#phase diagram
plt.subplot(1, 3, 3)
plt.plot(theta, omega)
plt.xlabel('θ (rad)')
plt.ylabel('ω (rad/s)')
plt.title('Phase Space Diagram')
plt.grid(True)

plt.tight_layout()
plt.show()

plt.plot(t, energy)
plt.xlabel('Time (s)')
plt.ylabel('Total Energy (J)')
plt.title('Energy Conservation')
plt.grid(True)
plt.show()
