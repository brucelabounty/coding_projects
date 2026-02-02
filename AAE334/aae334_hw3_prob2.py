# AAE 334 Homework 3 (Using Python)
# Author: Bruce LaBounty

import numpy as np
import matplotlib.pyplot as plt

# Initializing constants (from part a)
a1 = 0.4189
a2 = 0.5585

x = np.linspace(0,1,500)

# Equations for Camber Line equation
eq1 = a1 * (x - x**2)
eq2 = a2 * (x - x**2) * (1 - 2*x)

camb_line = eq1 + eq2 # Camber Line Equation

# Plotting
plt.plot(x, camb_line)
plt.axis('equal')
plt.grid(True)
plt.xlim(0,1)
plt.title("Camber Line Profile")
plt.xlabel("x-axis")
plt.ylabel("z-axis")
plt.show()