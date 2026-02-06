# AAE364 Homework #3 Problem #3 in Python
# Author: Bruce LaBounty
# Date: 2/5/26

import numpy as np
import matplotlib.pyplot as plt
import control as ct

# initialization

t = np.linspace(0, 15)
s = ct.tf('s') # Defining s within s-domain

# G(s)
G = 10 / (s**3 + 4.5*s**2 + 22*s + 10)

# G_1(s)
G1 = 1 / (s + 1)

# G_2(s)
G2 = 10 / (s**2 + 12*s + 10)

#INFO FOR LAST QUESTION
info = ct.step_info(G, T=t)
print(info)

# Making Step Responses
t_G, y_G = ct.step_response(G,t)
t_G1, y_G1 = ct.step_response(G1,t)
t_G2, y_G2 = ct.step_response(G2,t)

# Plotting
plt.plot(t_G, y_G, label='G(s)')
plt.plot(t_G1, y_G1, label='G1(s)')
plt.plot(t_G2, y_G2, label='G2(s)')

plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Unit-Step Responses of G(s), G1(s), and G2(s)')

plt.grid(True)
plt.legend()
plt.show()