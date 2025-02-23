

import numpy as np
import matplotlib.pyplot as plt

def rot(theta, point, origin=(0, 0)):
    
    x, y = point
    ox, oy = origin
    x_new = ox + (x - ox) * np.cos(theta) - (y - oy) * np.sin(theta)
    y_new = oy + (x - ox) * np.sin(theta) + (y - oy) * np.cos(theta)
    return x_new, y_new

def tp(x, y, dx, dy):
    
    return x + dx, y + dy

def koch(x, y, x1, y1, n):
    
    if n == 0:
        return [(x, y), (x1, y1)]

    theta = np.pi / 3
    dx = (x1 - x) / 3
    dy = (y1 - y) / 3


    p1 = (x, y)
    p2 = tp(x, y, dx, dy)
    p3 = tp(*p2, dx, dy)  
    

    px, py = p2
    p4 = rot(theta, (px + dx, py + dy), p2)  
    
    p5 = (x1, y1)

    
    points = koch(*p1, *p2, n - 1)
    points += koch(*p2, *p4, n - 1)[1:]
    points += koch(*p4, *p3, n - 1)[1:]
    points += koch(*p3, *p5, n - 1)[1:]

    return points


x, y = 0, 0
x1, y1 = 3, 0
n = 8


points = koch(x, y, x1, y1, n)
xval, yval = zip(*points)


plt.figure(figsize=(8, 6))
plt.plot(xval, yval, color="blue", linestyle="-", label="Koch Snowflake")
plt.axis('equal')
plt.title(f"Koch Curve (n={n})")
plt.show()
