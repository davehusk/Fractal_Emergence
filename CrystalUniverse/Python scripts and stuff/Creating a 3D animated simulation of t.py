# Creating a 3D animated simulation of two coupled non-linear oscillators. This example will expand the previous 2D case into three dimensions.

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parameters for the oscillators
m = 1.0  # Mass of the oscillators
k = 1.0  # Spring constant
alpha = 0.1  # Non-linearity coefficient

# Equations of motion for the coupled oscillators in 3D
def equations_of_motion_3d(y, t, m, k, alpha):
    x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2 = y

    # Forces on the first oscillator
    force1_x = -k * x1 - alpha * x1**3 + alpha * (x2 - x1)**3
    force1_y = -k * y1 - alpha * y1**3 + alpha * (y2 - y1)**3
    force1_z = -k * z1 - alpha * z1**3 + alpha * (z2 - z1)**3

    # Forces on the second oscillator
    force2_x = -k * x2 - alpha * x2**3 - alpha * (x2 - x1)**3
    force2_y = -k * y2 - alpha * y2**3 - alpha * (y2 - y1)**3
    force2_z = -k * z2 - alpha * z2**3 - alpha * (z2 - z1)**3

    return [vx1, vy1, vz1, force1_x / m, force1_y / m, force1_z / m,
            vx2, vy2, vz2, force2_x / m, force2_y / m, force2_z / m]

# Initial conditions: initial positions and velocities in 3D
y0_3d = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# Time array for the simulation
t_3d = np.linspace(0, 20, 500)

# Solving the equations of motion
solution_3d = odeint(equations_of_motion_3d, y0_3d, t_3d, args=(m, k, alpha))

# Creating the 3D animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Animation function
def animate(i):
    ax.clear()
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.scatter(solution_3d[i, 0], solution_3d[i, 1], solution_3d[i, 2], color='b', label='Oscillator 1')
    ax.scatter(solution_3d[i, 6], solution_3d[i, 7], solution_3d[i, 8], color='r', label='Oscillator 2')
    ax.legend()

# Creating the animation
ani = FuncAnimation(fig, animate, frames=len(t_3d), interval=40)

plt.show()
