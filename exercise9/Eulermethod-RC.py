import numpy as np
import matplotlib.pyplot as plt


q_0 = 0.02 #mC
iteration = 10000
C = 1e-3  # m F
R = 5 #m ohm
h = (3.5*1e-2) / iteration
q = np.zeros(iteration)
t = np.linspace(0 , 3.5*1e-2 ,iteration)
q[0] = q_0


for i in range(1, iteration):
    q[i] = q[i-1] - (q[i-1] * h) / (R * C)

q_e= q_0 / np.e
e_index = np.argmin(np.abs(q - q_e))
t_e = t[e_index]
q_at_e= q[e_index]


q_exact = q_0*np.exp(-t/(R*C))

plt.figure(figsize=(8,8))
plt.scatter(t_e * 1000, q_at_e, color="red", label="q = q₀ / e")
plt.plot(t * 1000, q_exact, label="Analytical Solution", marker='*', color="green")
plt.plot(t*1000, q, color="black", label="Numerical Solution")
plt.xlabel("Time (ms)")
plt.ylabel("Charge (mC)")
plt.title("RC Discharge with Euler's Method")
plt.legend()
plt.grid(True)
plt.show()