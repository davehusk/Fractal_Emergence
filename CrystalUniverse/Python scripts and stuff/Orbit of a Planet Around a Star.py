# To connect nonlinear dynamics to a cosmic scale, let's consider a simplified model of a two-body problem in an orbital system.
# In this model, we examine the motion of a smaller body (like a planet) around a much larger body (like a star), influenced by gravitational forces.

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def two_body_orbit(t, state, G, M):
    x, y, vx, vy = state  # Position and velocity components of the smaller body

    # Distance from the larger body
    r = np.sqrt(x**2 + y**2)

    # Gravitational force magnitude
    F = G * M / r**2

    # Acceleration components
    ax = -F * x / r
    ay = -F * y / r

    return [vx, vy, ax, ay]

# Gravitational constant and mass of the larger body (e.g., a star)
G = 6.67430e-11  # m^3 kg^-1 s^-2
M = 1.989e30     # kg (mass of the Sun)

# Initial conditions: position and velocity of the smaller body (e.g., a planet)
initial_state = [1.5e11, 0, 0, 30000]  # Approximate values for Earth

# Time array
t_span = [0, 3.154e7]  # One year in seconds
t_eval = np.linspace(*t_span, 1000)

# Solve the differential equations
solution = solve_ivp(two_body_orbit, t_span, initial_state, args=(G, M),
                     t_eval=t_eval, method='RK45')

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(solution.y[0], solution.y[1])
plt.title("Orbit of a Planet Around a Star")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.grid()
plt.show()
