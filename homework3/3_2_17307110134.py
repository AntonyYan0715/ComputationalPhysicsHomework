import numpy as np

def main():
    matrix = get_parameter()        # Firstly, we use a function to get the input.
    equation = Gauss(matrix,3)      # The function Gauss() can Gaussian eliminate the matrix.
    solution = Back_sub(equation,3) # The function Back_sub() finishes the backward substitutions.
    resistance = 5.0/solution[0]    # Solution is a matrix which stores the values of the current i1, i2 and i3.
    print('The effective resistance of the circuit is %s' % resistance)

def Gauss(x,n):
# The Gaussian elimination function needs 2 parameters, x is the matrix that we need to solve, n is the order of the matrix.
    equation = np.asarray(x,dtype=float)

    for i in range(n):
        if equation[i][i] == 0.0:
        # We need to make sure that the diagonal elements are not 0, or we need to change the row.
            for j in range(i+1,n):
                if equation[j][i] != 0.0:
                    equation[i],equation[j] = equation[j],equation[i]
                    break
        
        for k in range(i+1,n):
            ratio = -(equation[k][i] / equation[i][i])
            # Ratio is the number we need to multiply before we add the elements of 2 rows together.
            for l in range(n+1):
                equation[k][l] = equation[k][l] + ratio*equation[i][l]
    
    # After these operations, we turn the coefficient matrix into an upper-triangular matrix.
    return equation

def Back_sub(x,n):
# Backward substitutions
    solution = np.zeros(n)  # We initialize a matrix to store the values of i1, i2 and i3 we've solved from the equations.
    matrix = x.copy()

    for i in range(n-1,-1,-1):
    # We start the backward substitution from the last row, so the index starts from n-1 to 0.
        solution[i] = matrix[i][n]

        for j in range(i+1,n):
            solution[i] = solution[i] - matrix[i][j]*solution[j]
            # We subtract the element in this row one by one.
        
        solution[i] = solution[i] / matrix[i][i]
    
    return solution

def get_parameter():
# We use this function to get the input of the resistance.
    r_s = float(input('Please input the value of resistor r_s:'))
    r_x = float(input('Please input the value of resistor r_x:'))
    r_a = float(input('Please input the value of resistor r_a:'))
    r_1 = float(input('Please input the value of resistor r_1:'))
    r_2 = float(input('Please input the value of resistor r_2:'))
    r_3 = float(input('Please input the value of resistor r_3:'))
    v_0 = 5.0
    # Here we set the voltage of the power v_0 = 5.0V.
    # It doesn't matter because we will divide it anyway when we calculate the resistance.
    matrix = np.empty([3,4],dtype=float)
    matrix[0][0] = r_s
    matrix[0][1] = r_1
    matrix[0][2] = r_2
    matrix[0][3] = v_0
    matrix[1][0] = -r_x
    matrix[1][1] = r_1 + r_x + r_a
    matrix[1][2] = -r_a
    matrix[1][3] = 0.0
    matrix[2][0] = -r_3
    matrix[2][1] = -r_a
    matrix[2][2] = r_2 + r_3 + r_a
    matrix[2][3] = 0.0
    return matrix

if __name__ == '__main__':
    main()






