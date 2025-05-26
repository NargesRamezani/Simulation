import numpy as np
import math
import random
import matplotlib.pyplot as plt

N = 100      
L = 100
v_max = 600
sigma = 1

n_side = int(L/2)  
spacing = L / n_side
r_0 = np.zeros((N, 2))
count = 0
for i in range(n_side+1):
    for j in range(int(n_side/2)+1):
        if count >= N:
            break
        r_0[count, 0] = i * spacing  # x
        r_0[count, 1] = j * spacing  # y
        count += 1
print(r_0)
v_0 = np.zeros((N, 2))

for i in range(N):
    v_0[i, 0] = random.randint(-v_max, v_max)  
    v_0[i, 1] = random.randint(-v_max, v_max)  

class MolecularSystem:
    def __init__(self, positions, velocity, L, sigma):
        self.positions = np.array(positions)
        self.velocity = np.array(velocity)
        self.L = L
        self.sigma = sigma
        self.r_c = 3.5 * sigma
        self.neighbors = self.neighbor_list(self.r_c)

    def remove_com_velocity(self):
        v_com = np.mean(self.velocity, axis=0)
        self.velocity -= v_com

    def neighbor_list(self, r_c=None):
        if r_c is None:
            r_c = self.r_c
        N = len(self.positions)
        neighbor = [[] for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                dr = self.positions[i] - self.positions[j]
                dr -= self.L * np.round(dr / self.L)
                dis = np.linalg.norm(dr)
                if dis < r_c:
                    neighbor[i].append(j)
                    neighbor[j].append(i)
        return neighbor

    def potential_per_particle(self):
        r_c = self.r_c
        u_shift = 4 * ((1 / r_c) ** 12 - (1 / r_c) ** 6)
        N = len(self.positions)
        u_particle = np.zeros(N)

        for i in range(N):
            for j in self.neighbors[i]:
                if j > i:  
                    dr = self.positions[i] - self.positions[j]
                    dr -= self.L * np.round(dr / self.L)
                    r = np.linalg.norm(dr)
                    if r < r_c:
                        r6 = (1 / r) ** 6
                        r12 = r6 ** 2
                        u = 4 * (r12 - r6) - u_shift
                        u_particle[i] += 0.5 * u
                        u_particle[j] += 0.5 * u
        return u_particle






