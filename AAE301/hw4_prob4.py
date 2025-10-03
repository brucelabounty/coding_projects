# AAE 301: Signals
# Homework 4 Problem 4
# Author: Bruce LaBounty

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)
Re_t = np.zeros_like(t)
Im_t = np.zeros_like(t)
N = 20 # Number of k values

for k in range (2, N+1):
    Re_t = Re_t + (1 / ((1+k) * (1-k))) * np.cos(k * t)
    Im_t = Im_t + (k / ((1-k)**2 * (1+k)**2)) * np.sin(k * t)

p_t = -1 + 4*Re_t - 8*Im_t

f_t = np.zeros_like(t)
f_t = t * np.sin(t)

plt.figure(1)
plt.plot(t, f_t)
plt.plot(t, p_t)