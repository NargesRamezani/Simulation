import matplotlib.pyplot as plt
import random
import numpy as np
import math


L =int(input ( 'please enter L ' ))
grid = np.zeros( (L , L) , dtype=int)

o = [0 , 1]
p = [0.4 , 0.6]


whole=np.zeros((L , L+1) , dtype=int)
whole[:, 0]=1
check=np.zeros((L , L+1) , dtype=int)
check[:, 0]=1

for y in range(L):
    for x in range(L):
        l = random.choices(o, weights=p, k=1)[0] 
        grid[y, x] = l
        if grid[y,x]==1:
            whole[y,x+1]=1
        
        
for i in range(L):
    for j in range(L):

        if whole[j, i + 1] == 1:  
            neighbors = [
                (j - 1, i + 1),  
                (j + 1, i + 1),  
                (j, i),
                (j, i + 2) ]
            for ny, nx in neighbors:
                if 0 <= ny < L and 0 <= nx < L + 1: 
                        if check[ny, nx] == 1: 
                            check[j, i + 1] = 1  
                            break


print(whole)
print(check)

if np.any(check[:, -1] == 1):
    print(1)

else:
    print(0)



cmap = plt.matplotlib.colors.ListedColormap(["white", "red"])
plt.figure(figsize=(6, 6))
plt.pcolormesh(grid, cmap=cmap, edgecolors="none")
plt.show()

