# AAE 301: Signals
# Homework 4 Problem 4
# Author: Bruce LaBounty

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 6*np.pi, 1000)   # 3 periods
t_wrapped = np.mod(t, 2*np.pi)      # wrap into [0, 2π]

# periodic original
f_t = t_wrapped * np.sin(t_wrapped)

Re_t = np.zeros_like(t)
Im_t = np.zeros_like(t)
N = 10

# Use t_wrapped in Fourier terms so both functions are on same periodic domain
for k in range(2, N+1):
    Re_t = Re_t + (-2 / (1 - k**2)) * np.cos(k * t_wrapped)

p_t = -1 + Re_t + Im_t + np.pi * np.sin(t_wrapped) - (1/2) * np.cos(t_wrapped)

plt.figure(1)
plt.plot(t, f_t, label="Original (3 periods)")
plt.plot(t, p_t, label="Fourier Approximation")
plt.grid(True)
plt.xlabel("Time (t)")
plt.ylabel("f(t) and p(t)")
plt.title("Fourier Series Approximation (N = %i, 3 periods)" % N)
plt.legend()
plt.show()

# RMS error per period
error_fun = (f_t - p_t)**2
mean_square = (1/(2*np.pi)) * np.trapezoid(error_fun, t)  # normalize by 2π
rms_error = np.sqrt(mean_square)

print(f"The per-period RMS error for N = 10 is: {rms_error:.6e}")