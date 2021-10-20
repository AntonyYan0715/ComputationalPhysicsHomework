import numpy as np
import copy as cp
from scipy.linalg import sqrtm

def dot(x1,x2):
#定义函数求向量点积
    result = 0
    for i in range(len(x1)):
        result += (x1[i] * x2[i])
    return result

def norm(x):
#定义函数求向量的模
    result = dot(x,x)
    return np.sqrt(result)

def Schmidt(x):
#定义Schmidt正交化函数
    x_T = x.T
    #将矩阵转置后运算更方便

    row = len(x_T)
    col = len(x_T[0])

    init = np.zeros([row,col])
    #初始化一个[row,col]维矩阵
    for i in range(0,row):

        for j in range(0,col):
            temp = x_T[i][j]

            for k in range(0,i):
                ratio = -(dot(x_T[i],init[k]) / dot(init[k],init[k]))
                temp += ratio * init[k][j]
            
            init[i][j] = temp
    
    for i in range(0,row):
        n = norm(init[i])

        for j in range(0,col):
            init[i][j] = init[i][j] / n

    result = init.T
    return result

def QR(x):
#定义函数对矩阵进行QR分解
    Q = Schmidt(x)
    R = np.matmul(Q.T,x)
    return [Q,R]

def eigenvalue(x):
#利用QR分解，迭代求本征值
    time = 30

    for i in range(0,time):
        result = QR(x)
        x = np.matmul(result[1],result[0])

    return x

def eigenvector(x):
#进一步求解本征向量
    value_mat = eigenvalue(x)
    vector_mat = np.linalg.inv((x - value_mat))
    return vector_mat

def get_eigenvalue(x):
#取对角矩阵的每一个对角元，即本征值，并存入列表中
    n = len(x)
    solution = []
    
    for i in range(n):
        solution.append(x[i][i])
    
    return solution

def calculate_H(x,y):
#计算H矩阵的矩阵元
    temp1 = -np.exp(-(x-y)**2)
    temp2 = 16 * (2*((x-y)**2)-1)
    temp3 = 2 * ((x+y)**2)
    temp4 = 8 * np.sqrt(np.pi)
    result = (temp1*temp2 + 1 + temp3) / temp4
    return result

def calculate_S(x,y):
#计算S矩阵的矩阵元
    temp1 = np.exp(-(x-y)**2)
    temp2 = np.sqrt(np.pi)
    result = temp1 / temp2
    return result

def new_H(x,y):
#计算H'矩阵的矩阵元
    temp_mat = np.linalg.inv(sqrtm(y))
    new_mat = np.matmul(np.matmul(temp_mat,x),temp_mat)
    return new_mat

def list_s(x):
#定义函数为s赋值
    step = x
    temp_list = []
    
    for i in range(100):
        temp_list.append(i*step)
    
    return temp_list

def generator(x,n):
#定义矩阵生成器函数，生成H,S,H'矩阵
    list_i = list_s(x)
    mat_H = np.zeros([n,n])
    mat_S = np.zeros([n,n])

    for i in range(n):
        for j in range(n):
            mat_H[i][j] = calculate_H(list_i[i],list_i[j])
            mat_S[i][j] = calculate_S(list_i[i],list_i[j])
    
    matrix = new_H(mat_H,mat_S)
    return matrix


def main():
    matrix1 = generator(0.004,100)
    #如果用自己写的函数求本征值就用get_eigenvalue(eigenvalue(matrix))
    #但是得知可以用库了，就用numpy求本征值吧
    result = np.linalg.eig(matrix1)
    eigenvalue1 = result[0]       #所有本征值构成的列表
    eigenvector1 = result[1][99]  #本征值1对应的本征向量

    print('The eigenvalues are:')
    print(eigenvalue1)
    print('The eigenvector is:')   
    print(eigenvector1)  

    #求S矩阵及S^(-1/2)矩阵
    list1 = list_s(0.004)
    mat_S = np.zeros([100,100])
    for i in range(100):
        for j in range(100):
            mat_S[i][j] = calculate_S(list1[i],list1[j])
    
    temp_mat = np.linalg.inv(sqrtm(mat_S))
    new_eigenvector = np.matmul(temp_mat,eigenvector1)

    print('The original eigenvector is:')
    print(new_eigenvector)


if __name__ == "__main__":
    main()