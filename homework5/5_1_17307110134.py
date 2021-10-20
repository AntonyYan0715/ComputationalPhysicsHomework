import numpy as np

def Richardson(h, n, x):
# Richardson extrapolation to approximate f'(x)
# h: initial stepsize
# n: max iteration value
# x: the value to find derivative at
    mat = np.zeros([n, n])
    
    for i in range(n):
        mat[i,0] = (f(x+h) - f(x-h)) / (2*h)
        h = h/2
    
    for j in range(1,n):
        for k in range(j,n):
            mat[k,j] = mat[k,j-1] + (1 / (4**j - 1)) * (mat[k,j-1] - mat[k-1,j-1])
    
    return mat

def f(x):
    return np.sin(x)

print(Richardson(1, 4, (np.pi/3)))
    
