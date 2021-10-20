import numpy as np
import sympy as sp
from sympy.abc import t
from sympy.plotting import plot

def Newton_formula(x, y):
# Newton divided difference formula to calculate the coefficients of polynomial.
    n = len(x)
    mat1 = np.zeros([n, n+1])
    # Construct a matrix and load x,y in first and second columns.
    for i in range(n):
        mat1[i][0] = x[i]
        mat1[i][1] = y[i]
    
    # Fill in the divided differences.
    for j in range(2, n+1):
        for k in range(j-1, n):
            mat1[k][j] = (mat1[k][j-1]-mat1[k-1][j-1]) / (mat1[k][0]-mat1[k-j+1][0])
    
    # The diagonal elements are the coefficients we need.
    result = np.zeros(n)
    for l in range(n):
        result[l] = mat1[l][l+1]
    
    return result

def polynomial(x, b):
# Evaluate the polynomial f(t) with coefficients b and given x.
# f(t) = b0 + b1(t-x0) + b2(t-x0)(t-x1) + ...
    n = len(b)
    result = b[0]

    for i in range(1,n):
        temp = 1
        for j in range(i):
            temp = temp * (t-x[j])
        result += b[i]*temp
    
    return result

def spline(x, y):
# Cubic spline interpolation of (x0,y0),(x1,y1)...
# fi(x) = ai*x^3 + bi*x^2 + ci*x + di, i from 0 to (n-2)
# We need to construct a [4(n-1) * 4(n-1)] matrix
    n = len(x)
    mat1 = np.zeros([4*(n-1), 4*(n-1)])
    mat2 = np.zeros(4*(n-1))

    for i in range(n-1):
        mat1[2*i][4*i] = x[i]**3
        mat1[2*i][4*i + 1] = x[i]**2
        mat1[2*i][4*i + 2] = x[i]
        mat1[2*i][4*i + 3] = 1
        mat2[2*i] = y[i]

        mat1[2*i + 1][4*i] = x[i+1]**3
        mat1[2*i + 1][4*i + 1] = x[i+1]**2
        mat1[2*i + 1][4*i + 2] = x[i+1]
        mat1[2*i + 1][4*i + 3] = 1
        mat2[2*i + 1] = y[i+1]
    
    for j in range(n-2):
        mat1[2*n - 2 + j][4*j] = 3 * (x[j+1]**2)
        mat1[2*n - 2 + j][4*j + 1] = 2 * x[j+1]
        mat1[2*n - 2 + j][4*j + 2] = 1

        mat1[2*n - 2 + j][4*j + 4] = -3 * (x[j+1]**2)
        mat1[2*n - 2 + j][4*j + 5] = -2 * x[j+1]
        mat1[2*n - 2 + j][4*j + 6] = -1
    
    for k in range(n-2):
        mat1[3*n - 4 + k][4*k] = 6 * x[k+1]
        mat1[3*n - 4 + k][4*k + 1] = 2

        mat1[3*n - 4 + k][4*k + 4] = -6 * x[k+1]
        mat1[3*n - 4 + k][4*k + 5] = -2
    
    mat1[4*n - 6][0] = 6 * x[0]
    mat1[4*n - 6][1] = 2
    mat1[4*n - 5][4*n -8] = 6 * x[n-1]
    mat1[4*n - 5][4*n -7] = 2

    solution = np.linalg.solve(mat1, mat2)
    return solution

def equation(x):
# Generate all (n-1) cubic equations, i-th equation is: 
# fi(t) = ai*t^3 + bi*t^2 + ci*t + di, i from 0 to (n-2)
    n = int(len(x) / 4)
    result = []

    for i in range(n):
        ai = x[4*i]
        bi = x[4*i + 1]
        ci = x[4*i + 2]
        di = x[4*i + 3]
        fi = (ai * (t**3)) + (bi * (t**2)) + (ci * t) + di
        result.append(fi)
    
    return result

def test1():
# Compare with 10 points of cos(x) within [0, Pi]
    x = np.linspace(0.0, np.pi, num=10)
    y = [np.cos(i) for i in x]
    f1 = polynomial(x, Newton_formula(x,y)) # Newton interpolation
    plot(f1,(t, 0.0, np.pi))                # The graph of Newton interpolation

    f2 = equation(spline(x, y))             # Cubic spline interpolation
    result = []
    # We have 9 equations and 9 ranges, so we use a list to store the information

    for i in range(9):
        temp = (f2[i],(t,x[i],x[i+1]))
        result.append(temp)

    # The graph of cubic spline interpolation
    plot(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8])

def test2():
# Compare with 10 points of 1/(1+25x^2)  within [-1, 1]
    x = np.linspace(-1.0, 1.0, num=10)
    y = [(1 / (1 + 25*(i**2))) for i in x]
    f1 = polynomial(x, Newton_formula(x,y)) # Newton interpolation
    plot(f1,(t, -1.0, 1.0))                 # The graph of Newton interpolation

    f2 = equation(spline(x, y))             # Cubic spline interpolation
    result = []

    for i in range(9):
        temp = (f2[i],(t,x[i],x[i+1]))
        result.append(temp)
    
    # The graph of cubic spline interpolation
    plot(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8])

def main():
    test1()
    test2()

if __name__ == "__main__":
    main()