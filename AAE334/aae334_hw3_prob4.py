# AAE 334 Homework 3 (Using Python)
# Author: Bruce LaBounty

import numpy as np
import matplotlib.pyplot as plt

x_c = np.linspace(0,1,500)

# NACA 0012 is a symmetric airfoil, so we can use the equation from a:
alpha = 15 * np.pi / 180 # 15 degree AoA (radians)
delt_Cp = 4*alpha * np.sqrt((1/x_c - 1))

# Plotting
plt.plot(x_c, delt_Cp)
plt.grid(True)
plt.xlim(0,1)
plt.title("Pressure Coefficient Jump vs. x/c for NACA 0012 Airfoil")
plt.xlabel("x/c")
plt.ylabel("Delta C_p")
plt.show()