import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


L =int(input ( 'please enter L ' ))
o = [0 , 1]
p = [0.6 , 0.4]

whole = np.zeros((L , L+1), dtype=int)
whole[:,0]=1
M = []
equivalences = {}

index = 2  

def find(x):
    if equivalences.get(x, x) != x:
        equivalences[x] = find(equivalences[x])  
    return equivalences.get(x, x)

for x in range(L):
    for y in range(L):
        l = random.choices(o, weights=p, k=1)[0] 
        if l == 1:
            neighbors = []
            if y > 0 and whole[y-1, x+1] > 0:
                neighbors.append(find(whole[y-1, x+1]))
            if x > 0 and whole[y, x] > 0:
                neighbors.append(find(whole[y, x]))
            
            if not neighbors:
                whole[y, x+1] = index  
                equivalences[index] = index  
                index += 1
            else:
                min_index = min(neighbors)
                whole[y, x+1] = min_index
                for neighbor in neighbors:
                    equivalences[find(neighbor)] = min_index  


for x in range(L):
    for y in range(L):
        if whole[y, x+1] > 0:
            whole[y, x+1] = find(whole[y, x+1])

print(whole)
first_column = whole[: , 1]
last_column = whole[:,-1]
print(first_column)
result = 0 
for i in range(L):
    for j in range(L):
        if first_column[i] == last_column[j] and first_column[i]!=0:
            result = 1  
            break
    if result == 1:
            break

if result == 1:
    print(1)
else:
    print(0)


color_matrix_without_first_column = whole[:, 1:]

colors = ['white'] + [plt.cm.viridis(i) for i in np.linspace(0, 1, 256)] 
custom_cmap = mcolors.ListedColormap(colors)

plt.figure(figsize=(6, 6))
plt.imshow(color_matrix_without_first_column, cmap=custom_cmap, vmin=0, vmax=np.max(color_matrix_without_first_column), interpolation='none')
plt.show()