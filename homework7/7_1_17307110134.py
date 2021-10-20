import matplotlib.pyplot as plt
from math import pi

def Euler(T, h):
# We set l/g = 1, ml^2/2 = mgl/2 = 1
# θ = y1, dθ/dt = y2
# dy1/dt = y2, dy2/dt = -y1
    N = int(T / h)
    t_points = []
    y1_points = []
    y2_points = []
    energy = []
    y = [pi/40, 0]

    for i in range(N):
        t_points.append(h * i)
        y1_points.append(y[0])
        y2_points.append(y[1])
        energy.append(y[0]**2 + y[1]**2)
        y = [y[0] + y[1]*h, y[1] - y[0]*h]
    
    t_points.append(h * N)
    y1_points.append(y[0])
    y2_points.append(y[1])
    energy.append(y[0]**2 + y[1]**2)

    plt.plot(t_points, y1_points)
    plt.show()
    plt.plot(t_points, energy)
    plt.show()

    return t_points, y1_points, y2_points

def midpoint(T, h):
    N = int(T / h)
    t_points = []
    y1_points = []
    y2_points = []
    energy = []
    y = [pi/40, 0]

    for i in range(N):
        t_points.append(h * i)
        y1_points.append(y[0])
        y2_points.append(y[1])
        energy.append(y[0]**2 + y[1]**2)
        y_temp = [y[0] + (y[1]*h)/2, y[1] - (y[0]*h)/2]
        y = [y[0] + y_temp[1]*h, y[1] - y_temp[0]*h]
    
    t_points.append(h * N)
    y1_points.append(y[0])
    y2_points.append(y[1])
    energy.append(y[0]**2 + y[1]**2)

    plt.plot(t_points, y1_points)
    plt.show()
    plt.plot(t_points, energy)
    plt.show()

    return t_points, y1_points, y2_points

def RK4(T, h):
    N = int(T / h)
    t_points = []
    y1_points = []
    y2_points = []
    energy = []
    y = [pi/40, 0]

    for i in range(N):
        t_points.append(h * i)
        y1_points.append(y[0])
        y2_points.append(y[1])
        energy.append(y[0]**2 + y[1]**2)

        k1 = [y[1], -y[0]]
        k2 = [y[1] + (h/2)*k1[1], -(y[0] + (h/2)*k1[0])]
        k3 = [y[1] + (h/2)*k2[1], -(y[0] + (h/2)*k2[0])]
        k4 = [y[1] + h*k3[1], -(y[0] + h*k3[0])]

        temp = [(a + 2*b + 2*c + d) / 6 for a, b, c, d in zip(k1, k2, k3, k4)]
        y = [y[0] + temp[0]*h, y[1] + temp[1]*h]
    
    t_points.append(h * N)
    y1_points.append(y[0])
    y2_points.append(y[1])
    energy.append(y[0]**2 + y[1]**2)

    plt.plot(t_points, y1_points)
    plt.show()
    plt.plot(t_points, energy)
    plt.show()

    return t_points, y1_points, y2_points

def Euler_trapezoidal(T, h):
    iteration = 3
    N = int(T / h)
    t_points = []
    y1_points = []
    y2_points = []
    energy = []
    y = [pi/40, 0]

    for i in range(N):
        t_points.append(h * i)
        y1_points.append(y[0])
        y2_points.append(y[1])
        energy.append(y[0]**2 + y[1]**2)

        # Euler method:
        y_derivative = [y[1], -y[0]]
        y_temp = [y[0] + y[1]*h, y[1] - y[0]*h]

        # Trapezoidal rule:
        for j in range(iteration):
            y_derivative = [(y[1] + y_temp[1]) / 2, -(y[0] + y_temp[0]) / 2]
            y_temp = [y[0] + y_derivative[0]*h, y[1] + y_derivative[1]*h]
        y = y_temp
    
    t_points.append(h * N)
    y1_points.append(y[0])
    y2_points.append(y[1])
    energy.append(y[0]**2 + y[1]**2)

    plt.plot(t_points, y1_points)
    plt.show()
    plt.plot(t_points, energy)
    plt.show()

    return t_points, y1_points, y2_points

def main():
    T = 50
    h = 0.001
    Euler(T, h)
    midpoint(T, h)
    RK4(T, h)
    Euler_trapezoidal(T, h)

if __name__ == "__main__":
    main()