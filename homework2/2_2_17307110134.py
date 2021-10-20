import sympy as sp
from sympy.abc import x,y
from sympy.plotting import plot3d

def main():
    plot(-10,10)
    # First, plot the function in the interval -10<x<10, -10<y<10.
    # From the graph we can tell that g(x,y) is a periodic function.

    result = SD_method(0.01)
    print('when x=%.4f, y=%.4f, the function reaches its minimum.' % (result[0],result[1]))    


def function():
    g = sp.sin(x+y) + sp.cos(x + 2*y)
    g_x = sp.diff(g,x)
    g_y = sp.diff(g,y)
    list1 = [g,g_x,g_y]
    # We construct a list that contains the function and its partial derivatives.

    return list1


def plot(m,n):
    g = sp.sin(x+y) + sp.cos(x + 2*y)
    plot3d(g, (x,m,n), (y,m,n))
    # Plot the function in the interval [m,n].


def SD_method(t):
# Steepest-Descent method
    step = t
    x0 = -1.0       # The original x-coordinate.
    y0 = -1.0       # The original y-coordinate.
    fun = function()
    f = fun[0]      # The given function.
    f_x = fun[1]    # The x partial derivative of function.
    f_y = fun[2]    # The y partial derivative of function.
    iteration = 0

    while True:
        delta_x = -(step * f_x.evalf(subs={x:x0,y:y0},n=10))
        delta_y = -(step * f_y.evalf(subs={x:x0,y:y0},n=10))
        x1 = x0 + delta_x
        y1 = y0 + delta_y

        if abs(f.evalf(subs={x:x1,y:y1},n=10) - f.evalf(subs={x:x0,y:y0},n=10)) >= 1e-20:
        # When |f(x,y)-f(x+Δx,y+Δy)| < 1e-20, we take f(x,y) as a minimum of the function.
            print('f(x)=%.8f, the times of iteration are %d.' % (f.evalf(subs={x:x0,y:y0},n=10),iteration))
            x0 = x1
            y0 = y1
            iteration += 1
        
        else:
            minimum = f.evalf(subs={x:x0,y:y0},n=10)
            print('f(x)=%.8f is the minimum of the function, the times of iteration are %d.' % (minimum, iteration))
            return [x0,y0,minimum]


if __name__ == '__main__':
    main()