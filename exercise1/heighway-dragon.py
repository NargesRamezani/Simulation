

import numpy as np
import matplotlib.pyplot as plt

x1, y1 = 0, 0
x2, y2 = 2, 0

def rot(theta, a):
    x_new = a * np.cos(theta)
    y_new = a * np.sin(theta)
    return x_new, y_new

def dragon(x1, y1, x2, y2, n, left=True):
    if n == 0:
        return [(x1, y1), (x2, y2)]

    x_mid = (x1 + x2) / 2
    y_mid = (y1 + y2) / 2
    shift = np.sqrt((x2 - x1)**2 + (y2 - y1)**2) / 2

    theta = np.arctan2((y2 - y1), (x2 - x1))
    sign = 1 if left else -1

    
    x_rot, y_rot = rot(theta + sign * np.pi / 2, shift)
    X = x_mid + x_rot
    Y = y_mid + y_rot

    
    left_part = dragon(x1, y1, X, Y, n - 1, left=True)
    right_part = dragon(X, Y, x2, y2, n - 1, left=False)

    
    return left_part + right_part

n = 20
points = dragon(x1, y1, x2, y2, n, left=True)


mid = len(points) // 2
left_points = points[:mid]
right_points = points[mid - 1:]  


left_x, left_y = zip(*left_points)
right_x, right_y = zip(*right_points)


plt.figure(figsize=(8, 8))
plt.plot(left_x, left_y, color="blue", linestyle="-", label="Left Part")
plt.plot(right_x, right_y, color="red", linestyle="-", label="Right Part")
plt.axis('equal')
plt.title(f"Dragon Curve (n={n})")
plt.legend()
plt.show()