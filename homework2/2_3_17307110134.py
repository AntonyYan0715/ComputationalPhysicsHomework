import sympy as sp
import math as ma

def main():
    root1 = Bisection(0,1.57)
    # First, we use Bisection Method to search for a rough solution.
    # The value of theta satisfies 0° < theta < 90°, so the interval is [0,pi/2].

    root2 = Newton(root1)
    # Then we use Newton Method to polish it up.

    theta = (root2/ma.pi) * 180
    print('The system is in equilibrium at %s°.' % theta)


def Bisection(x1,x2):
# Bisection Method
    root = 0

    if f(x1)*f(x2) < 0:
    # The root is between [x1,x2].
        x3 = (x1+x2) / 2

        while abs(f(x3)) > 1e-4:
            if f(x1)*f(x3) < 0:
            # The root is between [x1,x3].
                x2 = x3
                x3 = (x1+x2) / 2
                
            else:
            # The root is between [x3,x2].
                x1 = x3
                x3 = (x1+x2) / 2
            
        root = x3
        print('Roughly, %.4f is a root of the equation.' % root)
    
    elif f(x1)*f(x2) == 0:
        if f(x1) == 0 and f(x2) == 0:
        # Both x1 and x2 are roots.
            root = [x1,x2]
            print('Both %.4f and %.4f are roots of the equation.' % (x1,x2))
        
        elif f(x1) == 0:
        # x1 is a root.
            root = x1
            print('%.4f is a root of the equation.' % root)
        
        else:
        # x2 is a root.
            root = x2
            print('%.4f is a root of the equation.' % root)
            

    else:
        print('Please make sure that f(x1)*f(x2)<0.')

    return root        


def Newton(t):
# Newton Method

    x = sp.Symbol('x')
    derivative = sp.diff(f(x),x)
    # We get the derivative of the function.

    iteration = 0
    # The times of iteration.

    while True:
        a = f(t)                             # a is the value of the function at t.
        b = derivative.evalf(subs={x:t},n=7) # b is the value of the function's derivative at t.
        print("f(x)=%.14f, f'(x)=%.14f, the times of iteration are %d." % (a,b,iteration))

        if abs(a) > 1e-14:
            # The root is polished up to 14 decimal places.
            t = t - (a/b)
            iteration += 1
            # Call next iteration.
        
        else:
            print('%.14f is a root of the equation.' % t)
            return t
            # Get the root and break the while-loop.


def f(t):
    m = 5
    L = 0.3
    k = 1000
    g = 9.8
    
    function = sp.tan(t) - sp.sin(t) - (m*g)/(2*k*L)
    return function
    # Define the equation which we need to solve.


if __name__ == '__main__':
    main()