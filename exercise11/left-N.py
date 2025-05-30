import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('E:\\Physics\\4S\\cp\\template\\exercise11\\trajectory (4).csv')
N = 100


Nl = {int(ti):0 for ti in df['step']}
t = len(Nl)

for _, row in df.iterrows():
    step = row['step']
    if row['x'] < 11 and step in Nl:
        Nl[step] += 1

#print(Nl)
steps = []
counts = []
for keys, value in Nl.items():
    steps.append(keys)
    counts.append(value)

plt.figure(figsize=(10, 5))
plt.plot(steps, counts, )
plt.xlabel('Time Step')
plt.ylabel('Number of Particles (x < 10)')
plt.title('Left Side Particle Count')
plt.grid(True)
plt.show()


