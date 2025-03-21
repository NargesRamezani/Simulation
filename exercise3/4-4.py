import numpy as np
import matplotlib.pyplot as plt
import csv


L = 10
p = 0.5




V = np.random.rand(L, L-1) > p  
H = np.random.rand(L-1, L) > p  
labels = np.zeros((L, L), dtype=int)
index = 1

for i in range(L):
    for j in range(L):
        left = labels[i, j-1] if j > 0 and not V[i, j-1] else 0  
        top = labels[i-1, j] if i > 0 and not H[i-1, j] else 0  

        if left and top:  
                        labels[i, j] = min(left, top)
                        labels[labels == max(left, top)] = min(left, top)  
        elif left:  
                        labels[i, j] = left
        elif top:  
                        labels[i, j] = top
        else:  
                        labels[i, j] = index
                        index += 1


            #plt.figure(figsize=(5, 5))

for i in range(L):
    for j in range(L):
            if j < L-1 and V[i, j]:  
                        plt.vlines(j + 1, L - i - 1, L - i, colors='b', linewidth=2)
            if i < L-1 and H[i, j]:  
                        plt.hlines(L - i - 1, j, j + 1, colors='r', linewidth=2)
                    

            plt.text(j + 0.5, L - i - 0.5, str(labels[i, j]), 
                            ha='center', va='center', fontsize=12, color='black')


            #print(labels)


first_column = labels[: , 0]
last_column = labels[:,-1]

result = 0 
for i in range(L):
    for j in range(L):
        if first_column[i] == last_column[j]:
            result = 1  
            break
    if result == 1:
            break
            



plt.xlim(0, L)
plt.ylim(0, L)
plt.gca().set_xticks(np.arange(L + 1))
plt.gca().set_yticks(np.arange(L + 1))
plt.grid(True)
plt.show()

