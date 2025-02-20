import matplotlib.pyplot as plt
import matplotlib.patches as patches


x1 , y1 = 0 ,0
x2 , y2 = 2 , 0
x3 , y3 = 1 , 2
n=6

def ser (x1 , y1 , x2 , y2 ,x3 , y3 , n):
    if n==0: 
        return [(x1 , y1) , (x2 , y2) , (x3, y3)]
    
    xx1=(x1+x2)/2
    yy1=(y1+y2)/2

    xx2=(x2+x3)/2
    yy2=(y2+y3)/2

    xx3=(x1+x3)/2
    yy3=(y1+y3)/2
    
    
    points = []
    points.extend(ser(x1, y1, xx1, yy1, xx3, yy3, n - 1))
    points.extend(ser(xx1, yy1, x2, y2, xx2, yy2, n - 1))
    points.extend(ser(xx3, yy3, xx2, yy2, x3, y3, n - 1))

    return points

points = ser(x1 , y1 , x2 , y2 ,x3 , y3 , n)


fig, ax = plt.subplots()

x_vals, y_vals = zip(*points)



triangle = patches.Polygon([[x1, y1], [x2, y2], [x3, y3]], closed=True, color=(100/255, 224/255, 250/255))
ax.add_patch(triangle)

for i in range(0,len(points),3):
    triangle = patches.Polygon(points[i:i+3], closed=True, color=(0/255, 0/255, 0/255))
    ax.add_patch(triangle)

plt.xlim(-1, 3)
plt.ylim(-1, 3)
ax.set_aspect('equal')
plt.title(f"Sierpinski (n={n})")
plt.show()