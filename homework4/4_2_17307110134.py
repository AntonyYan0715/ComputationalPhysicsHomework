from scipy.optimize import leastsq
import numpy as np

def func(p, x):
# The function that needs to be fitted
    a, b = p
    fx = (8.314 * 303 * ((1/x) + (a/(x**2) + (b/(x**3)))))
    return fx

def error(p, x, y):
# The residual error of the fitting
    return func(p,x) - y

def SVD(x, y):
# Solving least-squares system with SVD
    m = len(x)
    A = np.zeros([m,2])
    b = np.zeros(m)
    mat = np.zeros([2,m])

    for i in range(m):
        A[i][0] = (8.314*303) / (x[i]**2)
        A[i][1] = (8.314*303) / (x[i]**3)
        b[i] = y[i] - (8.314*303) / x[i]
    
    U, sigma, V = np.linalg.svd(A)
    mat[0][0] = 1 / sigma[0]
    mat[1][1] = 1 / sigma[1]
    solution = np.dot(np.dot(np.dot(V.T,mat),U.T),b)

    return solution

    

def main():
    V1 = 0.001 * np.asarray([25000, 22200, 18000, 15000])
    P1 = 1.013e05 * np.asarray([0.985, 1.108, 1.363, 1.631])
    V2 = np.asarray([25000, 22200, 18000, 15000])
    P2 = np.asarray([0.985, 1.108, 1.363, 1.631])
    p0 = [1,-1]
    para1 = leastsq(error, p0, args=(V1,P1))
    para2 = leastsq(error, p0, args=(V2,P2))
    print('国际单位制下：a=%f, b=%f' % (para1[0][0], para1[0][1]))
    print('国际单位制下，奇异值分解得到： a=%f, b=%f' % (SVD(V1,P1)[0], SVD(V1,P1)[1]))
    print('未转换单位时：a=%f, b=%f' % (para2[0][0], para2[0][1]))
    print('未转换单位时，奇异值分解得到： a=%f, b=%f' % (SVD(V2,P2)[0], SVD(V2,P2)[1]))


if __name__ == "__main__":
    main()
