import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def Gauss_Seidel(L_x, L_y, h, err, iter):
# x belongs to [0, L_x]
# y belongs to [0, L_y]
# h = Δx = Δy
# err - maximum error
# iter - maximum iteration times
    n_x = int((L_x / h) + 1)
    n_y = int((L_y / h) + 1)
    x = np.linspace(0, L_x, n_x)
    y = np.linspace(0, L_y, n_y)
    X, Y = np.meshgrid(x, y)

    f = np.zeros([n_y, n_x]) # Source term f(x, y) = 0
  # f = -np.ones([n_y, n_x]) 
    u = np.ones([n_y, n_x])  # Initial guess
    u[0,:] = 0.0             # Boundary conditions
    u[-1,:] = 0.0
    u[:,0] = 0.0
    u[:,-1] = 1.0
  # u[:,-1] = 0.0
    error = 1.0              # Set an arbitrary initial error
    iteration = 0            # Iteration times

    while error > err and iteration < iter:
        u_temp = u.copy()

        for i in range(1, n_y - 1):
            for j in range(1, n_x - 1):
                u[i, j] =  (u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1] - f[i, j]*h*h) / 4
        
        error = (abs(u - u_temp)).max()
        iteration += 1
    
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(X, Y, u, cmap='rainbow')
    plt.show()

Gauss_Seidel(1.0, 1.5, 0.01, 0.01, 1000)
# Gauss_Seidel(1.0, 1.0, 0.01, 0.01, 1000)

