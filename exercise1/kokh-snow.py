import numpy as np
import matplotlib.pyplot as plt


x , y =0 , 0
x1 , y1 = 3 , 0
n=12

def rot(theta, point, origin=(0, 0)):
    x, y = point
    ox, oy = origin
    x_new = ox + (x - ox) * np.cos(theta) - (y - oy) * np.sin(theta)
    y_new = oy + (x - ox) * np.sin(theta) + (y - oy) * np.cos(theta)
    return (x_new, y_new)

def kokh (x , y , x1 , y1 , n):
    if n==0:
        return[(x,y) , (x1 , y1) ]
    
    dx = (x1 - x) / 3
    dy = (y1 - y) / 3
    
    
    xx = x + dx
    yy = y + dy
    Xx = x1 - dx
    Yy = y1 - dy
    

    theta = np.pi / 3

    x_mid, y_mid = rot(theta, (Xx, Yy), (xx, yy))

    
    points=[]

    #points = [(x , y),(xx , yy) , (x_mid , y_mid), (Xx , Yy), (x1 , y1)]
    points.extend(kokh(x,y , xx , yy , n-1))
    points.extend(kokh(xx,yy , x_mid , y_mid , n-1))
    points.extend(kokh( x_mid , y_mid ,Xx,Yy , n-1))
    points.extend(kokh( Xx,Yy , x1 ,y1, n-1))
    return points

points = kokh(x , y ,x1, y1 , n)
xval , yval = zip(*points)


plt.plot(xval, yval, color="blue", linestyle="-", label="Left Part")

plt.axis('equal')  
plt.title(f"Kokh snowflake (n={n})")
plt.show()
