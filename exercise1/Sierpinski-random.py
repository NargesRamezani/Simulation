import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

def f1 (x,y):
    x=x/2
    y=y/2
    return(x,y)

def f2(x,y):
    x=x/2 + 0.5
    y=y/2+1
    return (x ,y)

def f3 (x ,y):
    x=x/2 +1 
    y= y/2
    return(x,y)

functions=[f1 , f2 , f3]
points=[]



for _ in range(10000):
    x= random.uniform(0, 2)
    y=random.uniform(0, 2)
    
    for _ in range(20):
        func=random.choice(functions)
        x , y = func(x , y)
    points.append((x,y))

x_value , y_value =zip(*points)

plt.scatter(x_value, y_value, s=0.1, color='purple')
plt.xlim(0, 2)
plt.ylim(0, 2)
plt.gca().set_aspect('equal')
plt.show()
