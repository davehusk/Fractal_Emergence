import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters for the oscillators
m = 1.0  # Mass of the oscillators
k = 1.0  # Spring constant
alpha = 0.1  # Non-linearity coefficient

# Equations of motion for the coupled oscillators
def equations_of_motion(y, t, m, k, alpha):
    x1, v1, x2, v2 = y

    # Forces on the first oscillator
    force1 = -k * x1 - alpha * x1**3 + alpha * (x2 - x1)**3

    # Forces on the second oscillator
    force2 = -k * x2 - alpha * x2**3 - alpha * (x2 - x1)**3

    return [v1, force1 / m, v2, force2 / m]

# Initial conditions: initial positions and velocities
y0 = [1.0, 0.0, -1.0, 0.0]

# Time array for the simulation
t = np.linspace(0, 20, 500)

# Solving the equations of motion
solution = odeint(equations_of_motion, y0, t, args=(m, k, alpha))

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(t, solution[:, 0], label='Oscillator 1')
plt.plot(t, solution[:, 2], label='Oscillator 2')
plt.title('Coupled Non-Linear Oscillators')
plt.xlabel('Time')
plt.ylabel('Position')
plt.legend()
plt.show()
