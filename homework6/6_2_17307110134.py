import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack

def load_file(filename):
# Load the data from file
    f = open(filename, 'r')
    lines = f.readlines()
    month = []    # Store the months in list
    sunspot = []  # Store the number of sunspots in list

    for line in lines:
        data = line.split()
        month.append(int(data[0]))
        sunspot.append(float(data[1]))
    
    return month, sunspot

def FFT(x, y):
# Calculate the Fourier transform of the sample
    n = len(x)
    F = fftpack.fft(y)                 # Fourier transform of sample
    f = fftpack.fftfreq(n, 1)          # Fourier transform sample frequencies
    domain = np.where(f > 0)           # We consider about half of the sample because of symmetry 
    x_axis = f[domain]                 # Set frequency as x-axis
    y_axis = (abs(F[domain]) / n) ** 2 # Set magnitude squared as y-axis

    plt.plot(x_axis, y_axis)
    plt.xlim(-0.001, 0.05)
    plt.xlabel('frequency (Hz)')
    plt.ylabel('magnitude squared')
    plt.show()

    max_loc = np.where(y_axis == np.max(y_axis)) # Search for the peak
    return x_axis[max_loc]

def main():
    x, y = load_file('sunspots.txt')
    plt.plot(x, y)   # The original sample
    plt.show()
    
    freq = FFT(x, y) # The Fourier transform of the sample
    T = 1/freq       # Calculate the period
    print('The period of the sunspots is %f months.' % T)

if __name__ == "__main__":
    main()