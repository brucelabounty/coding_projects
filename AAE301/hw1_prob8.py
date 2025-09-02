# AAE 301 (Signals I)
# Problem 8: Plotting Roots
# Author: Bruce LaBounty

import numpy as np
import matplotlib.pyplot as plt

n = 50 # Number of roots

theta = np.linspace(0, n-1, 100) # Calculating angle
z = np.exp(1j * theta) # Computing roots

plt.plot(np.real(z), np.imag(z), '*')
plt.xlabel("Re")
plt.ylabel("Im")
plt.title("Plot of Roots")
plt.grid(True)
plt.show()