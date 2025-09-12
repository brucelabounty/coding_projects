# AAE 333 (Fluids)
# Problem 1: Knudsen Number Semi-log Plot
# Author: Bruce LaBounty

import numpy as np
import matplotlib.pyplot as plt


char_length = 3.5 # Characteristic Length (m)

# Extracting data from file
data = np.loadtxt(r"AAE333\nrlmsise_Dragon.txt")

height = data[:, 0] # Altitude (km)
N2 = data[:, 1] * 10**6 # Number Density for diatomic Nitrogen (m-3)
O2 = data[:, 2] * 10**6 # Number Density for diatomic Oxygen (m-3)

# Calculating Mean Free Path (MFP)
d_N2 = .36e-9 # Diameter of diatomic Nitrogen (m)

mfp = 1 / (np.sqrt(2) * np.pi * (d_N2)**2 * (N2 + O2))

Kn = mfp / char_length # Knusden Number

# Plotting Results
plt.semilogy(height, Kn)
plt.xlabel("Altitude [km]")
plt.ylabel("Knudsen Number")
plt.title("Knudsen Number versus Height [km]")
plt.grid(True)
plt.show()

# Finding the value where flow switches to continuum
idx = np.where(Kn < 0.01)
cont_alt = height[idx]
print(cont_alt[-1])