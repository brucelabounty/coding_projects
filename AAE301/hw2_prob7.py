# AAE 301 (Signals I)
# Problem 7: Inner Product Orthogonality
# Author: Bruce LaBounty

import sympy as sp
import numpy as np

t = sp.symbols('t')

f = sp.cos(t) * sp.sin(t)

integral_1 = 1 / (2*np.pi) * sp.integrate(f, (t, 0, 2 * np.pi))
integral_2 = 1 / (1) * sp.integrate(f, (t, 0, 1))

print('0 to 2pi:', integral_1)
print('0 to 1:', integral_2)