# AAE 334 Homework 3 (Using Python)
# Author: Bruce LaBounty

import numpy as np
import matplotlib.pyplot as plt

<<<<<<< HEAD
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
=======
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
>>>>>>> 39f1f2d9dd4527564a63b79dbe41814a8954b58f
plt.xlabel("x-axis")
plt.ylabel("z-axis")
plt.show()