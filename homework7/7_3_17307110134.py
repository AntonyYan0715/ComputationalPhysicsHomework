import numpy as np
import matplotlib.pyplot as plt

def derivative(y, V, E):
    # We set dψ/dx = φ, d^2ψ/dx^2 = dφ/dx = (V-E)ψ = (V-x^2)ψ
    # y = [ψ, φ]
    result = np.asarray([y[1], (V - E) * y[0]])
    return result

def RK4(f, psi0, x, V, E):
    # Use RK4 method to calculate ψ in the region
    psi = np.array([psi0] * len(x))

    for i in range(len(x) - 1):
        h = x[i+1] - x[i]
        k1 = f(psi[i], V[i], E)
        k2 = f(psi[i] + (h*k1) / 2, V[i], E)
        k3 = f(psi[i] + (h*k2) / 2, V[i], E)
        k4 = f(psi[i] + (h*k3), V[i], E)
        psi[i+1] = psi[i] + h * (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return psi

def count_zeros(func):
    # Count the number of zero-crossings of the wave function
    n = len(func)
    counter = 0
    for i in range(n - 1):
        if func[i] * func[i+1] < 0:
            counter += 1
    return counter

def shooting(E_min, E_max, zeros, psi0, x, V):
    ''' We use Shooting method to calculate the eigenvalue E
    E_min - the lower bound of E
    E_max - the upper bound of E
    zeros - the number of zero-crossings of the wave function
    x - the array of x points
    V - the array of points of potential V(x)
    '''
    tolerance = 1e-10
    minE = E_min
    maxE = E_max

    while (maxE - minE) > tolerance:
        E = (minE + maxE) / 2.0
        psi = RK4(derivative, psi0, x, V, E)[: , 0]
        num = count_zeros(psi)

        if num > zeros:
            maxE = E
        elif num < zeros:
            minE = E
        elif abs(psi[-1]) > 1e-5:
        
            if (num%2 == 0):
                if psi[-1] > 0:
                    maxE = E
                else:
                    minE = E   
            else:
                if psi[-1] > 0:
                    minE = E
                else:
                    maxE = E
        else:
            return E

    return E

def Harmonic_Oscillator(E_min, E_max, zeros):
    # Initial-value ψ0 = 0.0, and we set φ0 = 1.0
    psi_0 = np.asarray([0.0, 1.0])
    x = np.linspace(-5.0, 5.0, num=1001)
    V = x ** 2
    E = shooting(E_min, E_max, zeros, psi_0, x, V)
    psi = RK4(derivative, psi_0, x, V, E)[: , 0]

    return E, x, psi

def main():
    E1, x1_points, psi1_points = Harmonic_Oscillator(0, 100, 1)
    print('Found Ground State at E = %f' % E1)
    plt.plot(x1_points, psi1_points)
    plt.title('Ground State')
    plt.grid()
    plt.show()

    E2, x2_points, psi2_points = Harmonic_Oscillator(0, 100, 2)
    print('Found First Excited State at E = %f' % E2)
    plt.plot(x2_points, psi2_points)
    plt.title('First Excited State')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
