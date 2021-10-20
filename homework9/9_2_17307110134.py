import numpy as np
import matplotlib.pyplot as plt

class Heisenberg(object):

    def __init__(self, size, J):
        self.size = size
        self.J = J
        self.lattice = np.ones([size, size, size, 3])
    
    def initialize_spin(self):
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    self.lattice[i, j, k] = np.array([0.0,0.0,1.0])
        return None

    def random_spin(self):
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    vec = np.random.randn(3)
                    vec = vec / np.linalg.norm(vec)
                    self.lattice[i, j, k] = vec
        return None
    
    def x_before(self, x, y, z):
        if x < 1:
            return [self.size - 1, y, z]
        else:
            return [x - 1, y, z]
    
    def x_after(self, x, y, z):
        if x > self.size - 2:
            return [0, y, z]
        else:
            return [x + 1, y, z]
    
    def y_before(self, x, y, z):
        if y < 1:
            return [x, self.size - 1, z]
        else:
            return [x, y - 1, z]
    
    def y_after(self, x, y, z):
        if y > self.size - 2:
            return [x, 0, z]
        else:
            return [x, y + 1, z]
    
    def z_before(self, x, y, z):
        if z < 1:
            return [x, y, self.size - 1]
        else:
            return [x, y, z - 1]
    
    def z_after(self, x, y, z):
        if z > self.size - 2:
            return [x, y, 0]
        else:
            return [x, y, z + 1]

    # Calculate energies and magnetizations

    def unit_E(self, x, y, z):
        [x1, y1, z1] = self.x_before(x, y, z)
        [x2, y2, z2] = self.x_after(x, y, z)
        [x3, y3, z3] = self.y_before(x, y, z)
        [x4, y4, z4] = self.y_after(x, y, z)
        [x5, y5, z5] = self.z_before(x, y, z)
        [x6, y6, z6] = self.z_after(x, y, z)
        spin = self.lattice[x1, y1, z1] + self.lattice[x2, y2, z2] + self.lattice[x3, y3, z3] \
             + self.lattice[x4, y4, z4] + self.lattice[x5, y5, z5] + self.lattice[x6, y6, z6]
        
        E = -self.J * self.lattice[x, y, z].dot(spin)
        return E
    
    def total_E(self):
        total_energy = 0

        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    total_energy += self.unit_E(x, y, z)
        return total_energy / 2
    
    def total_M(self):
        return np.sum(np.sum(np.sum(self.lattice,axis = 0),axis = 0),axis = 0)
    
    def average_E(self):
        E = self.total_E()
        return E / (self.size ** 3)
    
    def average_M(self):
        M = self.total_M()
        return M / (self.size ** 3)

    # Metropolis method, flip a single spin for one time.
    def Metropolis(self,temperature):

        # Pick a spin to flip randomly.

        x = np.random.randint(0, self.size)
        y = np.random.randint(0, self.size)
        z = np.random.randint(0, self.size)
        original_spin = self.lattice[x, y, z].copy()

        # The original energy.
        E0 = self.unit_E(x, y, z)

        vec = np.random.randn(3)
        vec = vec / np.linalg.norm(vec)
        self.lattice[x, y, z] = vec

        # The energy after flip.
        E1 = self.unit_E(x, y, z)
        delta_E = E1 - E0

        # Calculate the Metropolis acceptance rate.
        if delta_E > 0:
            if np.random.rand() > np.exp(-delta_E / temperature):
                self.lattice[x, y, z] = original_spin
        
        return None
    

size = 32
temperature = 1
J = 1
steps = 10000000

h = Heisenberg(size, J)
h.initialize_spin()
iteration = []
M = []

for i in range(steps):
    h.Metropolis(temperature)

    if (i+1) % 10000 == 0:
        iteration.append(i+1)
        M.append(h.average_M())

    if (i+1) % 100000 == 0:
        print(h.average_M())

plt.plot(iteration, M)
plt.show()
