# AAE 334 Homework 3 (Using Python)
# Author: Bruce LaBounty

import numpy as np
import matplotlib.pyplot as plt

x_c = np.linspace(0, 1, 100)

# Each function argument in the piecewise
func1 = lambda x: (1/4) * (x - 2*x**2)
func2 = lambda x: (1/36) * (1 + x - 2*x**2)

# Conditions associated with each function
cond1 = (x_c >= 0) & (x_c <= 0.25)
cond2 = (x_c > 0.25) & (x_c <= 1.0)

# Camber profile calculation!
zc_c = np.piecewise(x_c, [cond1, cond2], [func1, func2])

# Plotting results
plt.plot(x_c, zc_c)
plt.axis('equal')
plt.grid(True)
plt.xlim(0,1)
plt.title("Camber Profile")
plt.xlabel("x-axis")
plt.ylabel("z-axis")
plt.show()