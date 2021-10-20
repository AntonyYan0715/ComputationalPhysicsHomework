import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.sparse import spdiags

def Crank_Nicolson(alpha, psi):
    # psi - The wave function ψ_n
    # alpha - Δt/Δx^2
    # Return the wave function ψ_n+1
    n = len(psi)
    diags = np.array([0, -1, 1])
    vec1 = np.array([alpha*1j for i in range(n)])
    vec2 = np.array([(1 - 2*alpha*1j) for i in range(n)])
    vec3 = np.array([-alpha*1j for i in range(n)])
    vec4 = np.array([(1 + 2*alpha*1j) for i in range(n)])

    data1 = np.array([vec2, vec1, vec1])
    U1 = spdiags(data1, diags, n, n).toarray()

    data2 = np.array([vec4, vec3, vec3])
    U2 = spdiags(data2, diags, n, n).toarray()

    inv_U2 = np.linalg.inv(U2)
    U = np.dot(inv_U2, U1)
    next_psi = np.dot(U, psi)
    next_psi[0] = next_psi[-1] = 0.0+0.0j

    return next_psi

def Initial_State(x):
    # Calculate the Gaussian initial state ψ(x,0)
    psi = np.sqrt(1 / np.pi) * np.exp(1j * x - x**2 / 2)
    return psi

def wave_function():
    plt.ion()
    x = np.linspace(-10, 10, 2001)
    y = Initial_State(x)
    y[0] = y[-1] = 0.0+0.0j
    
    for i in range(30):
        plt.clf()
        plt.axis([-10, 10, -0.1, 0.6])
        plt.plot(x,abs(y))
        y = Crank_Nicolson(500, y)
        plt.pause(0.05)

    return x, y

wave_function()

