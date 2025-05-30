import numpy as np
import random
import matplotlib.pyplot as plt

# Simulation parameters
N = 100
L = 20
v_max = 1.4
sigma = 1
m = 1
h = 0.001
r_cut = 3.5 * sigma
r_min = 0.45 * sigma

# Initialize positions on a grid
n_side = int(np.ceil(np.sqrt(N)))
spacing = 10 / n_side
r_0 = np.zeros((N,2))
count = 0
for i in range(n_side):
    for j in range(int(n_side)):
        if count >= N:
            break
        r_0[count, 0] = i* spacing + 0.5* spacing
        r_0[count, 1] = j* spacing + 0.5* spacing
        count += 1

# Initialize velocities
v_0 = np.random.uniform(-v_max, v_max, (N,2))
v_0 -= np.mean(v_0, axis=0)

class MolecularSystem:
    def __init__(self, positions, velocity, L, sigma):
        self.positions = np.array(positions)
        self.velocity = np.array(velocity)
        self.L = L
        self.sigma = sigma
        self.r_c = r_cut
        self.neighbors = self.neighbor_list()
        self.force = np.zeros_like(positions)
        
    def neighbor_list(self):
        N = len(self.positions)
        neighbor = [[] for _ in range(N)]
        for i in range(N):
            for j in range(i+1, N):
                dr = self.positions[i] - self.positions[j]
                dr -= self.L * np.round(dr / self.L)
                dis = np.linalg.norm(dr)
                if dis < self.r_c:
                    neighbor[i].append(j)
                    neighbor[j].append(i)
        return neighbor

    def potential(self):
        r_c = self.r_c
        u_shift = 4 * ((sigma/r_c)**12 - (sigma/r_c)**6)
        N = len(self.positions)
        u_particle = np.zeros(N)
        self.force.fill(0)

        for i in range(N):
            for j in self.neighbors[i]:
                if j > i:
                    dr = self.positions[i] - self.positions[j]
                    dr -= self.L * np.round(dr / self.L)
                    r = np.linalg.norm(dr)
                    
                    if r < r_min:
                        r = r_min
                    
                    if r < r_c:
                        sr = sigma / r
                        sr6 = sr**6
                        sr12 = sr6**2
                        
                        u = 4 * (sr12 - sr6) - u_shift
                        u_particle[i] += 0.5 * u
                        u_particle[j] += 0.5 * u
                        
                        f_mag = 24 * (2*sr12 - sr6) / r
                        f_vec = f_mag * dr / r
                        self.force[i] += f_vec
                        self.force[j] -= f_vec
        return u_particle

# Initialize system
system = MolecularSystem(r_0, v_0, L, sigma)

# Simulation parameters
M = 28000
R = r_0.copy()
v = v_0.copy()
E_p = np.zeros(M)
E_K = np.zeros(M)
E = np.zeros(M)

with open('trajectory.csv','w') as f:
    f.write('step,particle_id,x,y,vx,vy\n')

# Main simulation loop
for i in range(M):
    # Update neighbor list periodically
    if i % 20 == 0:
        system.neighbors = system.neighbor_list()
    
    # Calculate forces and potential
    E_p[i] = np.sum(system.potential())
    a = system.force / m
    
    # Velocity Verlet integration
    v_half = v + 0.5 * a * h
    R += v_half * h
    R %= L
    system.positions = R
    
    # Calculate new forces
    if i % 20 == 0:
        system.neighbors = system.neighbor_list()
    system.potential()
    a_new = system.force / m
    
    v = v_half + 0.5 * a_new * h
    
    # Calculate energies
    E_K[i] = 0.5 * m * np.sum(v**2)
    E[i] = E_K[i] + E_p[i]

    if i%10 == 0:
    
        with open('trajectory.csv', 'ab') as f:
            for j in range(N):  
                line = f"{i},{j},{R[j,0]:.6f},{R[j,1]:.6f},{v[j,0]:.6f},{v[j,1]:.6f}\n"
                f.write(line.encode()) 

    # Print progress
    if i % 500 == 0:
        print(f"Step {i}")
        print(f"Kinetic Energy = {E_K[i]:.6f}")
        print(f"Potential Energy = {E_p[i]:.6f}")
        print(f"Total Energy = {E[i]:.6f}")
        print(f"Energy Drift = {(E[i]-E[0])/E[0]*100:.4f}%")
        print("------------------")

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(E_K, label='Kinetic Energy')
plt.plot(E_p, label='Potential Energy')
plt.plot(E, label='Total Energy')
plt.xlabel('Time step')
plt.ylabel('Energy')
plt.legend()
plt.title('Energy Conservation')
plt.show()