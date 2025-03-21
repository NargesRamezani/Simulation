import numpy as np
import matplotlib.pyplot as plt

Lv = [10, 20, 40 , 80 , 160] 
num_trials = 100  
p_values = np.linspace(0, 1, 20)  

Q_infinity_results = []
results = {L: {} for L in Lv}



for L in Lv:

    Q_infinity_results = []
    for p in p_values:
        success_count = 0
        
        for _ in range(num_trials):
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


            
            first_column = labels[:, 0]
            last_column = labels[:, -1]
            
            infinite_cluster_labels = set(first_column) & set(last_column)
            
            rand_i = np.random.randint(0, L)
            rand_j = np.random.randint(0, L - 1)
            if labels[rand_i, rand_j] in infinite_cluster_labels:
                success_count += 1
        
        Q_infinity = success_count / num_trials
        Q_infinity_results.append(Q_infinity)
        results[L][p] = Q_infinity


colors = ['b', 'g', 'r', 'c', 'm']  
for i, L in enumerate(Lv):
    plt.plot(p_values, [results[L][p] for p in p_values], marker='o', color=colors[i], label=f'L = {L}')

plt.plot(p_values, Q_infinity_results, marker='o')
plt.xlabel('p')
plt.ylabel('Q∞')
plt.legend()
plt.grid(True)
plt.show()
