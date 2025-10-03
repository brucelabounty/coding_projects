# AAE 301: Signals
# Homework 4 Problem 4
# Author: Bruce LaBounty

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)
Re_t = np.zeros_like(t)
Im_t = np.zeros_like(t)
N = 2 # Number of k values

for k in range (2, N+1):
    Re_t = Re_t - (-2 / (1 - k**2)) * np.cos(k * t)

p_t = -1 + Re_t

f_t = np.zeros_like(t)
f_t = t * np.sin(t)

plt.figure(1)
plt.plot(t, f_t)
plt.plot(t, p_t)
plt.show()