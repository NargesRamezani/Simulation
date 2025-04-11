import random
import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt

N = 1000
M = [i for i in range(100 , 1501 , 100)]
a, b = 0, 2
Z = 1 - np.exp(-2)


simple_means = []
smart_means = []
simple_stds = []
smart_stds = []
simple_times = []
smart_times = []


def exp_restricted():
    while True:
        u = random.uniform(0, 1)
        x = -np.log(u * (1 - np.exp(-2)))
        if 0 <= x <= 2:
            return x

for k in M:
    simple_results = []
    smart_results = []

    start_simple = time.time()
    for _ in range(k):
        p = 0
        y_max = 1
        for i in range(N):
            x = random.uniform(a, b)
            y = random.uniform(0, y_max)
            f_x = np.exp(-x**2)
            if y <= f_x:
                p += 1
        I = y_max * (b - a) * (p / N)
        simple_results.append(I)
    end_simple = time.time()
    simple_time = round((end_simple - start_simple), 4)

    start_smart = time.time()
    for _ in range(k):
        acc = 0
        for j in range(N):
            x = exp_restricted()
            f_x = np.exp(-x**2)
            g_x = np.exp(-x)
            acc += f_x / g_x
        J = Z * (acc / N)
        smart_results.append(J)
    end_smart = time.time()
    smart_time = round((end_smart - start_smart), 4)

    simple_mean = round(np.mean(simple_results), 3)
    simple_means.append(simple_mean)
    simple_std = round(np.std(simple_results) / np.sqrt(k), 6)
    simple_stds.append(simple_std)
    simple_times.append(simple_time)

    smart_mean = round(np.mean(smart_results), 3)
    smart_means.append(smart_mean)
    smart_std = round(np.std(smart_results) / np.sqrt(k), 6)
    smart_stds.append(smart_std)
    smart_times.append(smart_time)

    #print(f"\nSamples: {k}")
    #print(f"Simple Sampling: mean = {simple_mean:.5f}, std = {simple_std:.5f}, time = {simple_time:.4f} sec")
    #print(f"Smart Sampling : mean = {smart_mean:.5f}, std = {smart_std:.5f}, time = {smart_time:.4f} sec")


true_value = 0.88
simple_error = [abs(val - true_value) for val in simple_means]
simple_errors = [round(num, 3) for num in simple_error]
smart_error = [abs(val - true_value) for val in smart_means]
smart_errors =  [round(num, 3) for num in smart_error]


columns = ["Samples", "Simple Mean", "Smart Mean", "Simple Error", "Smart Error", "Simple Std/nN^0.5", "Smart Std/nN^0.5", "Simple Time", "Smart Time"]
data = list(zip(M, simple_means, smart_means, simple_errors, smart_errors, simple_stds,  smart_stds, simple_times, smart_times))
df = pd.DataFrame(data, columns=columns)


fig, ax = plt.subplots(figsize=(14, 3))
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')


table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.5)
plt.show()

plt.plot(smart_stds, smart_times, label="Smart Sampling")
plt.plot(simple_stds, simple_times, label="Simple Sampling")
plt.xlabel("std")
plt.ylabel("time")
plt.grid(True)
plt.legend()
plt.show()
