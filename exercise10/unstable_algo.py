import numpy as np
import matplotlib.pyplot as plt


q_0 = 0.02 #mC
iteration = 50
C = 1e-3  # m F
R = 5 #m ohm
h = (3.5*1e-2) / iteration
q = np.zeros(iteration)
t = np.linspace(0 , 3.5*1e-2 ,iteration)
q[0] = q_0
q[1] = q[0] - (q[0] * h) / (R * C)

for i in range(1, iteration):
    q[i] = q[i-2] - (q[i-1] * h) / (R * C)


plt.figure(figsize=(8,8))
plt.plot(t*1000, q, color="black", label="Numerical Solution")
plt.xlabel("Time (ms)")
plt.ylabel("Charge (mC)")
plt.title("RC Discharge with Euler's Method")
plt.legend()
plt.grid(True)
plt.show()