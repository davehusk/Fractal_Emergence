# Creating a 2D and 3D simulation of solitons can be quite complex. However, we can provide a basic representation.
# For the 2D case, we'll simulate a wave packet propagating through a 2D grid, resembling a soliton-like behavior.
# For the 3D case, we'll conceptualize a 3D wave propagating in a lattice structure.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters for the 2D simulation
grid_size = 50  # Size of the 2D grid
initial_amplitude = 2  # Initial amplitude of the wave

# Create a 2D grid
x, y = np.meshgrid(np.linspace(-5, 5, grid_size), np.linspace(-5, 5, grid_size))
z = np.zeros((grid_size, grid_size))

# Initialize a wave packet in the center of the grid
z[grid_size//2 - 5:grid_size//2 + 5, grid_size//2 - 5:grid_size//2 + 5] = initial_amplitude

# Parameters for the 3D simulation
length_of_chain_3d = 30  # Length of the chain in 3D

# Create arrays for 3D simulation
x_3d, y_3d, z_3d = np.indices((length_of_chain_3d, length_of_chain_3d, length_of_chain_3d))

# Initialize a wave in the center of the 3D lattice
z_3d[length_of_chain_3d//2 - 3:length_of_chain_3d//2 + 3, length_of_chain_3d//2 - 3:length_of_chain_3d//2 + 3, length_of_chain_3d//2 - 3:length_of_chain_3d//2 + 3] = initial_amplitude

# Plotting
fig = plt.figure(figsize=(12, 6))

# 2D Plot
ax1 = fig.add_subplot(121)
contour = ax1.contourf(x, y, z, cmap='viridis')
ax1.set_title('2D Soliton-like Wave')
ax1.set_xlabel('X Axis')
ax1.set_ylabel('Y Axis')

# 3D Plot
ax2 = fig.add_subplot(122, projection='3d')
scatter = ax2.scatter(x_3d.ravel(), y_3d.ravel(), z_3d.ravel(), c=z_3d.ravel(), cmap='viridis')
ax2.set_title('3D Soliton-like Wave')
ax2.set_xlabel('X Axis')
ax2.set_ylabel('Y Axis')
ax2.set_zlabel('Z Axis')

plt.show()
