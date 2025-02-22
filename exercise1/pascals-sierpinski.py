import numpy as np
import matplotlib.pyplot as plt

def generate_pascals_triangle(n):
    triangle = np.zeros((n, 2 * n - 1), dtype=int) 
    for i in range(n):
        for j in range(i + 1):
            col = n - 1 - i + 2 * j
            if j == 0 or j == i:
                triangle[i, col] = 1
            else:
                triangle[i, col] = triangle[i - 1, col - 1] + triangle[i - 1, col + 1]
    return triangle

def display_pascals_triangle(triangle):
    color_matrix = (triangle % 2 == 1).astype(float) 
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal') 
    

    ax.pcolormesh(color_matrix, cmap='Blues', edgecolors='none', shading='auto')
    
    ax.set_xlim(-0.5, color_matrix.shape[1] - 0.5)
    ax.set_ylim(-0.5, color_matrix.shape[0] - 0.5)
    ax.invert_yaxis() 
    ax.axis('off') 

    
    plt.show()


n = 135

triangle = generate_pascals_triangle(n)
display_pascals_triangle(triangle)
