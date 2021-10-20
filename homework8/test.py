import scipy as sp
from scipy.sparse import spdiags, linalg
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rdm

def Crank_Nicolson(alpha, psi):
    # psi - The wave function ψ_n
    # alpha - Δt/Δx^2
    # Return the wave function ψ_n+1
    n = len(psi)
    diags = np.array([0, -1, 1])
    vec1 = np.array([alpha for i in range(n)])
    vec2 = np.array([(2 - 2*alpha) for i in range(n)])
    vec3 = np.array([-alpha for i in range(n)])
    vec4 = np.array([(2 + 2*alpha) for i in range(n)])

    data1 = np.array([vec2, vec1, vec1])
    U1 = spdiags(data1, diags, n, n)

    data2 = np.array([vec4, vec3, vec3])
    U2 = spdiags(data2, diags, n, n)

    inv_U2 = np.linalg.inv(U2.toarray())
    U = np.dot(inv_U2, U1.toarray())
    next_psi = np.dot(U, psi)

    return next_psi


plt.axis([0, 100, 0, 1])
plt.ion()

xs = [0, 0]
ys = [1, 1]

for i in range(100):
    y = rdm.random()
    xs[0] = xs[1]
    ys[0] = ys[1]
    xs[1] = i
    ys[1] = y
    plt.plot(xs, ys)
    plt.pause(0.1)
