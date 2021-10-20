import matplotlib.pyplot as plt

def Euler_trapezoidal(T, h):
    iteration = 3
    N = int(T / h)
    t_points = []
    y1_points = []
    y2_points = []
    y3_points = []
    y = [0, 1, 0]

    for i in range(N):
        t_points.append(h * i)
        y1_points.append(y[0])
        y2_points.append(y[1])
        y3_points.append(y[2])

        # Euler method:
        y_derivative = [10 * (y[1] - y[0]), 28 * y[0] - y[1] - y[0] * y[2], y[0] * y[1] - (8/3) * y[2]]
        y_temp = [y[0] + y_derivative[0]*h, y[1] + y_derivative[1]*h, y[2] + y_derivative[2]*h]

        # Trapezoidal rule:
        for j in range(iteration):
            y_derivative[0] = 10 * (y_temp[1] - y_temp[0])
            y_derivative[1] = 28 * y_temp[0] - y_temp[1] - y_temp[0] * y_temp[2]
            y_derivative[2] = y_temp[0] * y_temp[1] - (8/3) * y_temp[2]
            y_temp = [y[0] + y_derivative[0]*h, y[1] + y_derivative[1]*h, y[2] + y_derivative[2]*h]
        y = y_temp

    t_points.append(h * N)
    y1_points.append(y[0])
    y2_points.append(y[1])
    y3_points.append(y[2])

    plt.plot(t_points, y2_points)
    plt.show()
    plt.plot(y1_points, y3_points)
    plt.show()

def main():
    Euler_trapezoidal(50, 0.001)

if __name__ == "__main__":
    main()

