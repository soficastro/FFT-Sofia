import cmath
from cmath import exp, pi, sin, cos
import numpy as np
import matplotlib.pyplot as plt 
 
def FFT(A):
    N = len(A)
    if N == 1:
      return A
    else:
      Wn = exp(2*pi*1j/N)
      W = 1
      A_even = []
      A_odd = []
      for i in range(0, N):
        if i%2 == 0:
          A_even.append(A[i])
        else:
          A_odd.append(A[i])
      Y_even = FFT(A_even)
      Y_odd = FFT(A_odd)
      Y1 = []
      Y2 = []
      half_N = int(N/2)
      for i in range(half_N):
        Y1.append(Y_even[i] + W*Y_odd[i])
        Y2.append(Y_even[i] - W*Y_odd[i])
        W = W*Wn
    return Y1+Y2


m = 10                  #choose the pow of two!!!s
N = pow(2, m)           #1024 samples
T = 1/100               #sample spacing

time = np.linspace(0.0, N*T, N)
freq = np.linspace(0.0, 1/(2*T), N)

signal = []
for t in time:
  signal.append(2*cos(0.5*pi*t + 1))

fourier_signal = FFT(signal)

plt.figure(1)
plt.plot(time, signal)
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')
plt.title('Signal')
plt.figure(2)
plt.title('Fourier Transform')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.plot(freq, np.abs(fourier_signal))
plt.grid()
plt.show()


    