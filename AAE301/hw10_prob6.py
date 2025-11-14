# AAE 301: Signals Homework 10
# Problem 6
# Author: Bruce LaBounty

import sympy
import control
import scipy.signal as signal
from sympy.plotting import plot

# Initialization
A_matrix = sympy.Matrix([
        [-3, -6, -10, 10],
        [1, -1, 0, 0],
        [0, 1, -2, 3],
        [0, 0, 1, -2]
])

B_matrix = sympy.Matrix([[1],[0],[0],[0]])
C_matrix = sympy.Matrix([[1, -4, -2, 10]])

# Problem i)
s, t = sympy.symbols('s, t')

N = (s*sympy.eye(4) - A_matrix).inv()

G = (C_matrix*N*B_matrix).expand()
G.simplify()

print(G)

# McMillan Degree Calculation (Also includes problem ii)
num = [1, 1, -13, 3] # s^3 + s^2 - 13s + 3
den = [1, 8, 26, 50, 19] # s^4 + 8s^3 +26s^2 + 50s + 19
sys = control.tf(num, den)

sys_min = control.minreal(sys)
print(sys_min)

# Problem iii)
r, p, k = signal.residue(num, den)

G_s = 0 # Initializaing G(s)
for i in range(len(r)):
    G_s = G_s + r[i] / (s - p[i])

G_s = G_s * 30 / s # Doing Y(s) = G(s)U(s)
y_t = sympy.inverse_laplace_transform(G_s, s, t)

# Plotting
plt = plot(
    y_t,
    (t, 0, 10),
    title="System Response y(t)",
    xlabel="t",
    ylabel="y(t)",
    show=True
)