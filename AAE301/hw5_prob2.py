# AAE 301: Signals
# Homework 5 Problem 1 (a)
# Author: Bruce LaBounty

# PART A
import numpy as np
import matplotlib.pyplot as plt

nu = 2**19
t = np.linspace(0, 2*np.pi, nu)

f = np.sin(30 * t) * np.exp(2 * np.cos(5 * t))

c = np.fft.fft(f) / nu
c_shifted = np.fft.fftshift(c)
k = np.fft.fftshift(np.fft.fftfreq(nu, d=2*np.pi/nu))

# Correct zoom indexing
idx_zoom = np.where((k >= -100) & (k <= 100))[0]
c_plot = np.abs(c_shifted[idx_zoom])**2

# Plot with correctly matched x/y
plt.plot(k[idx_zoom], c_plot)
plt.xlabel('k')
plt.ylabel('|c_k|^2')
plt.title('Power Spectrum')
plt.grid(True)
plt.show()