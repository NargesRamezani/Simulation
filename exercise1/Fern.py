import matplotlib.pyplot as plt
import numpy as np
import random

def f1(a):
    c = np.array([2, 4])  
    theta_deg = -3
    theta = np.radians(theta_deg)
    scale_factor = 7 / 8.4

    point_scaled = (a - c) * scale_factor + c
    point_translated = point_scaled - c

    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]])

    point_rotated = rotation_matrix @ point_translated
    point_final = point_rotated + c
    
    return point_final

def f2(a):
    c = np.array([0.5, 0.2])  
    theta_deg = 60
    theta = np.radians(theta_deg)
    scale_factor = 1.5 / 5

    point_scaled = a * scale_factor
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]])

    point_rotated = rotation_matrix @ point_scaled
    point_final = point_rotated + c
    
    return point_final

def f3(a):
    c = np.array([0.7, 0.3])  
    theta_deg = -60
    theta = np.radians(theta_deg)
    shear_factor = 0.3
    scale_factor = 1.5 / 5

    point_scaled = a * scale_factor
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]])
    shear_matrix = np.array([
        [1, shear_factor],
        [0, 1]])

    point_rotated = rotation_matrix @ point_scaled
    point_sheared = shear_matrix @ point_rotated
    point_final = point_sheared + c
    
    return point_final



def f4(a):
    theta_deg = -2.63
    theta = np.radians(theta_deg)
    
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    
    x_new = 0.69
    y_new =(1.83/10) * a[1]  # مقیاس کردن ارتفاع
    
    new_point = np.array([x_new, y_new])
    rotated_point = rotation_matrix @ new_point  # اعمال چرخش
    
    return rotated_point


functions = [f1, f2, f3, f4]
prob = [0.85, 0.07, 0.07, 0.01]

x, y = random.uniform(0, 2), random.uniform(0, 4)
points = []


for _ in range(10000):
    
    for _ in range(20):
        func = np.random.choice(functions, p=prob)
        x, y = func(np.array([x, y]))
        points.append((x, y))


x_vals, y_vals = zip(*points)


plt.figure(figsize=(8, 8))
plt.scatter(x_vals, y_vals, s=0.1, color='green', alpha=0.6, label="Fern")
plt.xlim(-0.5, 2.5)
plt.ylim(-0.5, 4.5)
plt.gca().set_aspect('equal')
plt.show()
