import matplotlib.animation as animation
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


L = 20
N = 100
sigma = 1.0
h = 0.0001
steps_per_frame = 10

df = pd.read_csv('E:\\Physics\\4S\\cp\\template\\exercise11\\trajectory (4).csv')


particles = {i: {'x': [], 'y': []} for i in range(N)}
for _, row in df.iterrows():
    pid = int(row['particle_id'])
    particles[pid]['x'].append(row['x'])
    particles[pid]['y'].append(row['y'])

for i in range(N):
    particles[i]['x'] = np.array(particles[i]['x'])
    particles[i]['y'] = np.array(particles[i]['y'])

fig, ax = plt.subplots(figsize=(10, 10))
scat = ax.scatter([], [], s=500, colorizer='pink')  
ax.set_xlim(0, L)
ax.set_ylim(0, L)
ax.set_title('Molecular Dynamics Simulation')

def update(frame):

    x = [particles[i]['x'][frame] for i in range(N)]
    y = [particles[i]['y'][frame] for i in range(N)]
    
    scat.set_offsets(np.column_stack((x,y)))
    scat.set_color("#00F48AFF")
    return scat,
frame_time_ms = h* steps_per_frame*1000
num_frames = len(particles[0]['x'])

ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=frame_time_ms, blit=True)

plt.show()

