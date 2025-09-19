# AAE 301 (Signals I)
# Problem 1: Plotting Spectrum of |a_k| (PART B)
# Author: Bruce LaBounty

import numpy as np
import matplotlib.pyplot as plt
import math

# Initialize array for coefficients
k_vals = range(-80, 81) 
a_k = np.zeros(len(k_vals))
a_k_plot = np.zeros(len(k_vals))

for i, k in enumerate(k_vals):
    if k == 0:
        a_k[i] = 0
    elif k % 2 == 0:
        a_k[i] = 8 / k
    else:
        a_k[i] = 0
    a_k_plot[i] = math.sqrt(a_k[i]**2)

plt.figure()
plt.stem(k_vals, a_k_plot, markerfmt = ' ')
plt.title("Spectrum of |a$_k$| vs. k")
plt.ylabel("|a$_k$|")
plt.xlabel("k")
plt.grid(True)
plt.show()