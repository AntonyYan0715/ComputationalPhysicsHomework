import numpy as np
import sympy as sp
from sympy.abc import t

def Simpson(x1, x2, n):
# Simpson's rule to calculate integration of f(x)
# x1: lower bound of integration
# x2: upper bound of integration
# n: number of intervals, which must be even
    interval = np.linspace(x1, x2, num=n+1)
    step = (x2-x1) / n
    integrate = 0

    for i in range(0,n-1,2):
        result = (step/3) * (f(interval[i]) + 4*f(interval[i+1]) + f(interval[i+2]))
        integrate += result
    
    return integrate

def f(x):
# Define the function which needs to be integrated.
    global Φ
    temp1 = (sp.sin(x)) ** 2
    temp2 = (sp.sin(Φ/2)) ** 2
    result = 1 / sp.sqrt(1 - temp1*temp2)
    return result

def T(x):
# Calculate the oscillation period T of a pendulum
# Initial amplitude is x, and initial angular velocity is 0.
    global Φ
    Φ = x
    result = 4 * Simpson(0, np.pi/2, 100)
    return result

print('The period T is: %f*sqrt(l/g)' % T(np.pi/3))