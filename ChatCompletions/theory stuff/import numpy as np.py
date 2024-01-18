import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters (These would need to be adjusted based on your specific problem)
L = 50  # Length of spatial domain
T = 10  # Total time
dx = 0.1  # Spatial step size
dt = 0.01  # Time step size

x = np.arange(0, L, dx)
t = np.arange(0, T, dt)
X, T = np.meshgrid(x, t)

# Initial condition (A simple example soliton)
U = 2/(np.cosh(0.5*(X-10-3*T))**2)  # Adjust as needed for your soliton profile

# Creating the figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting the surface
ax.plot_surface(X, T, U, cmap='viridis')

ax.set_xlabel('Space')
ax.set_ylabel('Time')
ax.set_zlabel('Amplitude')

plt.show()
