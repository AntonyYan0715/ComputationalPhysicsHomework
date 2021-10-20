import numpy as np

def hypersphere(n):
    N = 0

    for i in range(1000000):
        r = 0

        for j in range(n):
            x = np.random.rand()
            r += x**2
        
        if r <= 1:
            N += 1
    
    return (N/1000000) * (2**n)

print(hypersphere(2))
print(hypersphere(3)*0.75)
print(hypersphere(4))
print(hypersphere(5))
