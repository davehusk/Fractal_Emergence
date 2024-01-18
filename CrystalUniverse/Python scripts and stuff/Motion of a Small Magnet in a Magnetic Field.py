# Another physical example demonstrating chaos and nonlinear dynamics is the motion of a magnet in a magnetic field. 
# Here, we'll consider a simple model where a small magnet moves in the magnetic field created by a fixed large magnet.

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def magnet_motion(t, state, mu, m, B0, R):
    x, v = state  # Position and velocity of the small magnet

    # Magnetic force on the small magnet due to the large fixed magnet
    # Assuming a simple model where the force is inversely proportional to the cube of the distance
    force = mu * m * B0 / (x**2 + R**2)**(3/2)

    # Newton's second law
    acceleration = force / m

    return [v, acceleration]

# Parameters
mu = 1.0  # Magnetic permeability
m = 0.1  # Mass of the small magnet
B0 = 1.0  # Magnetic field strength
R = 0.5  # Distance scale factor

# Initial conditions
initial_state = [1.0, 0.0]  # Initial position and velocity

# Time array
t_span = [0, 10]  # Time span for the simulation
t_eval = np.linspace(*t_span, 1000)  # Time points at which to solve

# Solve the differential equations
solution = solve_ivp(magnet_motion, t_span, initial_state, args=(mu, m, B0, R),
                     t_eval=t_eval, method='RK45')

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(solution.t, solution.y[0])
plt.title("Motion of a Small Magnet in a Magnetic Field")
plt.xlabel("Time")
plt.ylabel("Position")
plt.grid()
plt.show()
