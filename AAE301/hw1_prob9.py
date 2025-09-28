# AAE 301 (Signals I)
# Problem 9: Plotting Parametric Curves
# Author: Bruce LaBounty

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 1000) # Calculating angles
eq1 = np.exp(1j * 3 * theta) # Equation 1
eq2 = 1j * np.exp(1j * -2 * theta) # Equation 2

plt.figure(1)
plt.plot(np.real(eq1), np.imag(eq1))
plt.xlabel("Re")
plt.ylabel("Im")
plt.title("Plotting roots of Equation 1")
plt.grid(True)
plt.show()

plt.figure(2)
plt.plot(np.real(eq2), np.imag(eq2))
plt.xlabel("Re")
plt.ylabel("Im")
plt.title("Plotting roots of Equation 2")
plt.grid(True)
plt.show()