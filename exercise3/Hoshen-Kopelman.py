import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

L = 5
o = [0 , 1]
p = [0.59 , 0.41]

whole = np.zeros((L , L+1), dtype=int)
whole[:,0]=1
M = []
equivalences = {}  



for x in range(L):
    for y in range(L):
        l = random.choices(o, weights=p, k=1)[0] 
        if l==1:
            whole[y,x+1]=1
        
print(whole)

def find(x):
    while equivalences.get(x, x) != x:  
        x = equivalences.get(x, x)
    return x


index = 2
for x in range(L):
    for y in range(L):
        
        if whole[y, x+1] >0:
            neighbors = []
            
            if 0 <= y <= L +1 and whole[y-1, x+1] >0 :
                neighbors.append(whole[y-1, x+1])
            if 0 <= x <= L + 1 and whole[y, x] >0 :
                neighbors.append(whole[y, x])

            if not neighbors:
                
                equivalences[index] = index
                whole[y, x+1] = index
                index += 1
            

            elif len(neighbors) == 1:
                old_index = find(neighbors[0])
                whole[y, x+1] = old_index
            else:
                old_index1 = find(neighbors[0])
                old_index2 = find(neighbors[1])
                min_index = max(old_index1, old_index2)
                whole[y, x+1] = min_index
                equivalences[old_index1] = min_index
                equivalences[old_index2] = min_index

                """current_y, current_x = y, x+1
                while True:
                    # بررسی خانه بالا
                    if current_y > 0 and whole[current_y-1, current_x] > 0:
                        whole[current_y-1, current_x] = min_index
                        current_y -= 1
                    # بررسی خانه چپ
                    elif current_x > 0 and whole[current_y, current_x-1] > 0:
                        whole[current_y, current_x-1] = min_index
                        current_x -= 1
                    else:
                        break"""
                
            




print(equivalences)
print(whole)
