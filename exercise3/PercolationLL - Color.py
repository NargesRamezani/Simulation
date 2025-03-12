import matplotlib.pyplot as plt
import random
import numpy as np
import math
import matplotlib.colors as mcolors


L= 100
#L =int(input ( 'please enter L ' ))
grid = np.zeros( (L , L) , dtype=int)

o = [0 , 1]
p = [0.59 , 0.41]
color = 2

whole = np.zeros((L , L+2) , dtype=int)
whole[:, 0] = 1
whole[:,-1] = 0

color_matrix = np.zeros((L , L+1) , dtype=int)
color_matrix[:, 0] = 1




for y in range(L):
    for x in range(L):
        l = random.choices(o, weights=p, k=1)[0] 
        if l==1:
            whole[y,x+1]=1
        


        
for i in range(L):
    for j in range(L):

        if whole[i, j+ 1] == 1:
            rndm = list(range(2 , 200)) 
            a = random.choice(rndm)
            color_matrix[i, j+1] = a
            rndm.remove(a)

#print(color_matrix)


for i in range(L):
    for j in range(L):
        if whole[j, i + 1] == 1:  
            neighbors = [
                (j - 1, i + 1),  
                (j + 1, i + 1),  
                (j, i),
                (j, i + 2) 
            ]
            neighbor_colors = []

            for ny, nx in neighbors:
                if 0 <= ny < L and 0 <= nx < L + 1 and whole[ny, nx] > 0: 
                    neighbor_colors.append(color_matrix[ny, nx])


            if neighbor_colors:  
                if len(neighbor_colors) == 1:
                    color_matrix[j, i + 1] = neighbor_colors[0]  
                else:
                    min_color = min(neighbor_colors)

                    if color_matrix[j, i + 1] != min_color:
                            old_color = color_matrix[j, i + 1]
                            color_matrix[j, i + 1] = min_color
                            

                            stack = [(j, i+1)]
                            while stack:
                                y, x = stack.pop()
                                for ny, nx in [
                                    (y-1, x), (y+1, x), (y, x-1), (y, x+1)
                                ]:
                                    if 0 <= ny < L and 0 <= nx < L + 1 and whole[ny, nx] > 0:
                                        if color_matrix[ny, nx] != min_color:
                                            color_matrix[ny, nx] = min_color
                                            stack.append((ny, nx)) 




#print(whole)
#print(check)
#print(color_matrix)



if np.any(color_matrix[:, -1] == 1):
    print(1)
else:
    print(0)



color_matrix_without_first_column = color_matrix[:, 1:]

colors = ['white'] + [plt.cm.viridis(i) for i in np.linspace(0, 1, 256)] 
custom_cmap = mcolors.ListedColormap(colors)


plt.figure(figsize=(6, 6))
plt.imshow(color_matrix_without_first_column, cmap=custom_cmap, vmin=0, vmax=np.max(color_matrix_without_first_column), interpolation='none')


plt.title('Color Matrix Visualization (Zero as White)')
plt.show()

