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
    x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, vx2, vy2, vz2, x3, y3, z3, vx3, vy3, vz3, \
    x4, y4, z4, vx4, vy4, vz4, x5, y5, z5, vx5, vy5, vz5, \
      x6, y6, z6, vx6, vy6, vz6 = y

    # Forces on the first oscillator
    force1_x = -k * x1 - alpha * x1**3 + alpha * (x2 - x1)**3 + alpha * (x4 - x1)**3
    force1_y = -k * y1 - alpha * y1**3 + alpha * (y3 - y1)**3
    force1_z = -k * z1 - alpha * z1**3 + alpha * (z2 - z1)**3 + alpha * (z5 - z1)**3

    # Forces on the second oscillator
    force2_x = -k * x2 - alpha * x2**3 + alpha * (x1 - x2)**3 + alpha * (x3 - x2)**3
    force2_y = -k * y2 - alpha * y2**3 + alpha * (y3 - y2)**3
    force2_z = -k * z2 - alpha * z2**3 + alpha * (z1 - z2)**3 + alpha * (z3 - z2)**3

    # Forces on the third oscillator
    force3_x = -k * x3 - alpha * x3**3 + alpha * (x1 - x3)**3 + alpha * (x2 - x3)**3
    force3_y = -k * y3 - alpha * y3**3 + alpha * (y2 - y3)**3
    force3_z = -k * z3 - alpha * z3**3 + alpha * (z1 - z3)**3 + alpha * (z2 - z3)**3

    # Forces on the fourth oscillator
    force4_x = -k * x4 - alpha * x4**3 + alpha * (x1 - x4)**3 + alpha * (x5 - x4)**3
    force4_y = -k * y4 - alpha * y4**3 + alpha * (y5 - y4)**3
    force4_z = -k * z4 - alpha * z4**3 + alpha * (z5 - z4)**3 + alpha * (z1 - z4)**3

    # Forces on the fifth oscillator
    force5_x = -k * x5 - alpha * x5**3 + alpha * (x1 - x5)**3 + alpha * (x4 - x5)**3
    force5_y = -k * y5 - alpha * y5**3 + alpha * (y4 - y5)**3
    force5_z = -k * z5 - alpha * z5**3 + alpha * (z4 - z5)**3 + alpha * (z1 - z5)**3
    
    # Forces on the sixth oscillator
    force6_x = -k * x6 - alpha * x6**3 + alpha * (x1 - x6)**3 + alpha * (x4 - x6)**3
    force6_y = -k * y6 - alpha * y6**3 + alpha * (y4 - y6)**3
    force6_z = -k * z6 - alpha * z6**3 + alpha * (z4 - z6)**3 + alpha * (z1 - z6)**3


    return [vx1, vy1, vz1, force1_x / m, force1_y / m, force1_z / m,
            vx2, 0, vz2, force2_x / m, 0, force2_z / m,
            vx3, vy3, 0, force3_x / m, force3_y / m, 0,
            vx4, 0, vz4, force4_x / m, 0, force4_z / m,
            vx5, vy5, 0, force5_x / m, force5_y / m, 0,
            vx6, vy6, 0, force6_x / m, force6_y / m, 0]

# Initial conditions: initial positions and velocities in 3D for five oscillators
y0_3d = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         -1.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.5, 0.5, 0.0, 0.0, 0.0, 0.0,
         0.0, 1.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 1.0, 0.0, 0.0, 0.0,
         -0.5, 0.5, 0.0, 0.0, 0.0, 0.0]

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
      
      # Oscillator 1
      ax.scatter(solution_3d[i, 0], solution_3d[i, 1], solution_3d[i, 2], color='b', label='Oscillator 1')
      
      # Oscillator 2
      ax.scatter(solution_3d[i, 6], 0, solution_3d[i, 8], color='r', label='Oscillator 2')
      
      # Oscillator 3
      ax.scatter(solution_3d[i, 12], solution_3d[i, 13], 0, color='g', label='Oscillator 3')
      
      # Oscillator 4
      ax.scatter(solution_3d[i, 18], 0, solution_3d[i, 20], color='c', label='Oscillator 4')
      
      # Oscillator 5
      ax.scatter(solution_3d[i, 24], solution_3d[i, 25], 0, color='m', label='Oscillator 5')
      
      # Oscillator 6
      ax.scatter(solution_3d[i, 27], solution_3d[i, 28], 0, color='y', label='Oscillator 6')
      
      ax.legend()

# Creating the animation
ani = FuncAnimation(fig, animate, frames=len(t_3d), interval=40)

plt.show()