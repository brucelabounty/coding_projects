# AAE 301 (Signals I)
# Problem 1: Plotting Approximation to Fourier Sine Series Expansion (PART A)
# Author: Bruce LaBounty

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000) # Generates 1000 points on t from 0 to 2pi
# Note: t is defined from 0 to 2pi
p_t = np.zeros_like(t)

# Solving for P(t) for n = 80
for k in range(1, 81, 2):
    p_t += np.sin(k * t) / k

p_t = 8 * p_t
f_t = np.where(t <= np.pi, 2*np.pi, -2*np.pi) # Showing the function that the Fourier expansions was applied to

plt.plot(t, f_t)
plt.plot(t, p_t)
plt.grid(True)
plt.xlabel("time [t]")
plt.ylabel("p(t) and f(t)")
plt.title("Fourier Sine Series Expansion Approximation")
plt.show()