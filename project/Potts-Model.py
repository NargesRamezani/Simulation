import numpy as np
import matplotlib.pyplot as plt
import random

L = 25
N = 120000
dish = np.zeros([L, L], dtype=str)

v0_A = 0
v0_B = 0
v0_M =0
Lambda = 0.5
k_BT = 1
AB_length = 0
BA_length = 0


list = ['M', 'A', 'B']
weight = [0.15, 0.425, 0.425]
for i in range(L):
    for j in range(L):
        dish[i, j] = random.choices(list, weights=weight)[0]
        if dish[i, j] == 'A':
            v0_A += 1
        elif dish[i, j] == 'B':
            v0_B +=1
        else:
            v0_M +=1

for i in range(L):
    for j in range(L):
        cell = dish[i, j]
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            ni = i + di
            nj = j + dj
            ni %= L
            nj %= L
            if cell == 'A':
                if dish[ni, nj] == 'B':
                    AB_length+=1

def delta_AB_length(old_dish, new_dish, i, j):
    old_length = 0
    new_length = 0
    for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
        ni = i + di
        nj = j + dj
        ni %= L
        nj %= L
        if old_dish[i, j] =='A':
            if old_dish[ni, nj] =='B':
                old_length +=1
        if old_dish[i, j] =='B':
            if old_dish[ni, nj] =='A':
                old_length +=1
        if new_dish[i, j] =='A':
            if new_dish[ni, nj] =='B':
                new_length +=1
        if new_dish[i, j] =='B':
            if new_dish[ni, nj] =='A':
                new_length +=1
    return new_length - old_length





'''
dish = np.zeros([L, L], dtype=str)
list = ['A', 'B']
weight = [0.2, 0.8]
for i in range(L-2):
    for j in range(L-2):
        dish[i+1, j+1] = random.choices(list, weights=weight)[0]
        if dish[i, j] == 'A':
            v0_A += 1
        elif dish[i, j] == 'B':
            v0_B +=1

v0_M = 2*L + 2*(L-2)
dish[0, :] = 'M'
dish[L-1, :] = 'M'
dish[:, 0] = 'M'
dish[:, L-1] = 'M'

'''


first = dish.copy()     


J = {('A', 'A'): -1.5, ('B', 'B'): -1.5, ('A', 'B'): 3, ('B', 'A'): 2, ('A', 'M'): 2, ('B', 'M'): 1, ('M', 'A'): 2, ('M', 'B'): 1, ('M', 'M'): 0.0}

def delta_energy(dish, i, j, new_type, J, L):
    delta_H = 0
    old_type = dish[i,j]
    
    for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
        ni, nj = (i+di)%L, (j+dj)%L  
        neighbor = dish[ni,nj]

        if (old_type, neighbor) in J:
            delta_H -= J[(old_type, neighbor)]

        if (new_type, neighbor) in J:
            delta_H += J[(new_type, neighbor)]
    
    return delta_H
H0 = 0
VA = 0
VB = 0

for i in range(L):
    for j in range(L):

        cell = dish[i, j]
        if cell == 'M':
            continue
        for di , dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = di + i, dj+ j
            ni %= L
            nj %= L

        neighbor = dish[ni, nj]
        if (cell, neighbor) in J:  
                H0 += J[(cell, neighbor)]




H = H0
current_VA = v0_A
current_VB = v0_B
frames = []  
hamiltonian = []
step = []
ABlength = []

for k in range(N):
    i, j = np.random.randint(0, L), np.random.randint(0, L)
    hamiltonian.append(H)
    step.append(k)
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    random.shuffle(directions)
    for di,dj in directions:
        ni, nj = (i+di)%L, (j+dj)%L
        if dish[ni,nj] != 'M':
            break
    else:
        continue
    old_dish = dish.copy()
    new_list = ['A', 'B']
    new = random.choice(new_list)

    old = dish[ni, nj]
    temp_VA = current_VA
    temp_VB = current_VB

    if old == 'A':
        temp_VA -= 1
    elif old == 'B':
        temp_VB -= 1

    if new == 'A':
        temp_VA += 1
    elif new == 'B':
        temp_VB += 1

    
    delta_H = delta_energy(dish, ni, nj, new, J, L) + Lambda * ((temp_VA - v0_A)**2 + (temp_VB - v0_B)**2 - (current_VA - v0_A)**2 - (current_VB - v0_B)**2)

    if delta_H < 0 or random.random() < np.exp(-delta_H/k_BT):
        dish[ni,nj] = new 
        current_VA, current_VB = temp_VA, temp_VB
        H += delta_H
    else:
        ABlength.append(AB_length)
        continue
    delta_length = delta_AB_length(old_dish, dish, i, j)
    AB_length += delta_length
    ABlength.append(AB_length)




    if k % 1000 == 0:
        frame = np.zeros((L, L))
        for i in range(L):
            for j in range(L):
                if dish[i, j] == 'A':
                    frame[i, j] = 1
                elif dish[i, j] == 'B':
                    frame[i, j] = 2
                else:
                    frame[i, j] = 0
        frames.append(frame)



final = np.zeros([L, L])
firstt = np.zeros([L, L])
for i in range(L):
    for j in range(L):
        if first[i, j] == 'A':
            firstt[i, j] = 1
        elif first[i, j] == 'B':
            firstt[i, j] = 2
        else:
            firstt[i, j] = 0
for i in range(L):
    for j in range(L):
        if dish[i, j] == 'A':
            final[i, j] = 1
        elif dish[i, j] == 'B':
            final[i, j] = 2
        else:
            final[i, j] = 0


plt.figure(figsize=(12, 6))
plt.plot(step, hamiltonian)
plt.title('Hamiltonian vs. Monte Carlo Steps')
plt.show()

plt.plot(step, ABlength)
plt.title('Boundary Length Between Cell Types A and B vs. Monte Carlo Steps')
plt.show()

plt.subplot(1, 2, 1)
plt.imshow(firstt, cmap='viridis')
plt.title('Initial State')
plt.colorbar(ticks=[0, 1, 2], label='M=0, A=1, B=2')

plt.subplot(1, 2, 2)
plt.imshow(final, cmap='viridis')
plt.title('Final State')
plt.colorbar(ticks=[0, 1, 2], label='M=0, A=1, B=2')

plt.tight_layout()



import matplotlib.animation as animation

fig, ax = plt.subplots()
img = ax.imshow(frames[0], cmap='viridis', vmin=0, vmax=2)
plt.title('Cell Sorting Process')
cbar = plt.colorbar(img, ticks=[0, 1, 2], label='M=0, A=1, B=2')

def update(frame):
    img.set_data(frame)
    return [img]

ani = animation.FuncAnimation(fig, update, frames=frames, interval=300, blit=True)

plt.show()


