import numpy as np
import matplotlib.pyplot as plt

c = -0.8 + 0.16j  

width, height = 1000, 1000  
iterations = 300  

x = np.linspace(-2, 2, width)
y = np.linspace(-2, 2, height)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y  

result = np.zeros(Z.shape, dtype=int)  
for i in range(iterations):
    norm = np.abs(Z)  
    mask = (norm < 2)  
    result[mask] = i  
    Z[mask] = Z[mask] ** 2 + c  

plt.figure(figsize=(8, 8))
plt.imshow(result, cmap="inferno", extent=[-2, 2, -2, 2])
plt.axis("off")
plt.title(f" (n={c})")
plt.show()