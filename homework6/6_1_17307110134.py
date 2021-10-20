import sympy as sp
from sympy.abc import t, k
from sympy.plotting import plot

def Fourier(x):
# x terms of Fourier series
    N = int(x / 2)
    result = 0
    func = abs(t) * sp.exp(1j * k * t)
    # Fourier coefficient g_k
    g_k = (1 / (2*sp.pi)) * sp.integrate(func, (t, -sp.pi, sp.pi))

    for i in range(-N, N+1):
        temp = g_k.evalf(subs={k:i}, n=10) * sp.exp(-1j * i * t)
        result += temp
    
    return result

def main():
    plot(abs(t), (t, -sp.pi, sp.pi), axis_center=[0,0])

    for i in range(2, 11, 2):
        func = Fourier(i)
        plot(func, (t, -sp.pi, sp.pi), axis_center=[0,0])

if __name__ == "__main__":
    main()