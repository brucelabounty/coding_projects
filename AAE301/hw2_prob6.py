# AAE 301 (Signals I)
# Problem 6: Checking Inner Product
# Author: Bruce LaBounty

import sympy as sp
import numpy as np

t, alpha = sp.symbols('t alpha')

f = 1 + alpha * t

integral = 1 / (2*np.pi) * sp.integrate(f, (t, 0, 2 * np.pi))

solution = sp.solve(sp.Eq(integral, 0), alpha)

print('alpha =', solution)