import sympy as sp

def main():
    global Roots
    Roots = []
    # We need a list to store the roots we've fonud, and it needs to be a global variable.

    # First, use Bisection Method.
    print('Bisection Method:')
    if type(Bisection()) == 'list':
        # Bisection() will return a list when it finds 2 roots.
        print('We find 2 roots.\n')
    else:
        # Bisection() will return a float when it finds only 1 root.
        # We need to run Bisection() agian to find another root.
        Bisection()
        print('We find 2 roots.\n')
    
    # Second, use Newton Method.
    print('Newton Method:')
    Newton(Roots[0])
    Newton(Roots[1])

    # Finally, use Hybrid Method. The function Hybrid() needs 3 parameters, and we set them in advance.
    # The reason why we select these values will be explained in pdf.
    print('Hybrid Method:')
    print('%.14f is a root of the equation.' % Hybrid(0,1,0.5))
    print('%.14f is a root of the equation.' % Hybrid(1,2,1.5))


def f(t):
    function = t**3 - 5*t + 3
    return function
# Define the function which we need to sketch.

def Bisection():
# Bisection Method
    global Roots
    root = 0 

    while True:
        x1 = eval(input('Please input the lower bound x1:'))
        x2 = eval(input('Please input the upper bound x2:'))
        
        if f(x1)*f(x2) > 0:
            # Make sure that the root is in the interval [x1,x2].
            print('Please make sure that f(x1)*f(x2)<0.')
        
        elif f(x1)*f(x2) < 0:
            x3 = (x1+x2) / 2
            while abs(f(x3)) > 1e-4:
            # We take x3 as a root when abs(f(x3)) < 1e-4, so it is determined to 4 decimal places.
                if f(x1)*f(x3) < 0:
                # The root is between [x1,x3].
                    x2 = x3
                    x3 = (x1+x2) / 2
                
                else:
                # The root is between [x3,x2].
                    x1 = x3
                    x3 = (x1+x2) / 2
            
            root = x3
            Roots.append(root)
            print('%.4f is a root of the equation.' % root)
            # Get the root, put it into the list and break the while-loop.
            break

        else:
            if f(x1)==0 and f(x2)==0:
            # Both x1 and x2 are roots, and we put them into the list.
                root = [x1,x2]
                Roots = root[:]
                print('Both %.4f and %.4f are roots of the equation.' % (x1,x2))
            elif f(x1)==0:
            # x1 is a root, and we put it into the list.
                root = x1
                Roots.append(root)
                print('%.4f is a root of the equation.' % root)
            else:
            # x2 is a root, and we put it into the list.
                root = x2
                Roots.append(root)
                print('%.4f is a root of the equation.' % root)
            
            # Get the root and break the while-loop.
            break

    return root


def Newton(t):
# Newton Method
    global Roots

    x = sp.Symbol('x')
    derivative = sp.diff(f(x),x)
    # We get the derivative of the function.

    iteration = 0
    # The times of iteration.

    while True:
        a = f(t)                              # a is the value of the function at t.
        b = derivative.evalf(subs={x:t},n=10) # b is the value of the function's derivative at t.
        print("f(x)=%.14f, f'(x)=%.14f, the times of iteration is %d." % (a,b,iteration))

        if abs(a) > 1e-14:
            # The root is determined to 14 decimal places.
            t = t - (a/b)
            iteration += 1
            # Call next iteration.
        
        else:
            print('%.14f is a root of the equation.\n' % t)
            Roots.append(t)
            return t
            # Get the root, put it into the list and break the while-loop.            


def Hybrid(x1,x2,t):
# Hybrid Method
# x1,x2 is the bound of Bisection Method. t is the original value of Newton Method.

    x = sp.Symbol('x')
    derivative = sp.diff(f(x),x)
    a = f(t)                             # a is the value of the function at t.
    b = derivative.evalf(subs={x:t},n=7) # b is the value of the function's derivative at t.
    x3 = (x1+x2) / 2

    while abs(a) > 1e-14 and abs(f(x3)) > 1e-14:
        if f(x1)*f(x3) < 0:
        # The root is between [x1,x3].
            x2 = x3
            x3 = (x1+x2) / 2

            # Check if the result of Newton Method sits in the interval given by Bisection Method.
            if t - (a/b) > x1 and t - (a/b) < x2:
                t = t - (a/b)
            else:
                t = x3
        
        else:
        # The root is between [x3,x2].
            x1 = x3
            x3 = (x1+x2) / 2

            # Check if the result of Newton Method sits in the interval given by Bisection Method.
            if t - (a/b) > x1 and t - (a/b) < x2:
                t = t - (a/b)
            else:
                t = x3

        # Update the value of a and b.
        a = f(t)
        b = derivative.evalf(subs={x:t},n=7)
    
    return t
    

if __name__ == '__main__':
    main()