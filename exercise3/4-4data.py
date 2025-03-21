import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file_paths = [
    "E:\\Physics\\4S\\cp\\template\\data\\exercise3\\l10.csv",
    "E:\\Physics\\4S\\cp\\template\\data\\exercise3\\l20.csv",
    "E:\\Physics\\4S\\cp\\template\\data\\exercise3\\l40.csv",
    "E:\\Physics\\4S\\cp\\template\\data\\exercise3\\l80.csv",
    "E:\\Physics\\4S\\cp\\template\\data\\exercise3\\l160.csv"]


Lv = [10, 20, 40, 80, 160]


p_values = np.linspace(0, 1, 21)  


results = {L: {p: [] for p in p_values} for L in Lv}

for file, L in zip(file_paths, Lv):
    data = pd.read_csv(file).iloc[:, 2]
    
    num_blocks = len(data) // 100
    for i in range(num_blocks):
        p = p_values[i % len(p_values)]  
        block = data.iloc[i*100 : (i+1)*100]  
        mean = block.mean()  
        results[L][p].append(mean)  
for L in Lv:
    for p in p_values:
        if results[L][p]:  
            results[L][p] = np.mean(results[L][p])  
        else:
            results[L][p] = None  


colors = ['b', 'g', 'r', 'c', 'm']


plt.figure(figsize=(10, 6))
for i, L in enumerate(Lv):
    x = p_values
    y = [results[L][p] for p in p_values]
    
    plt.plot(x, y, marker='o', color=colors[i], label=f'L = {L}')


plt.xlabel('p', fontsize=14)
plt.ylabel('Q', fontsize=14)
plt.grid(True)
plt.legend()
plt.show()