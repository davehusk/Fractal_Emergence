# Let's create another example of nonlinear dynamics using a different system - the Duffing oscillator. 
# The Duffing oscillator is a non-linear second-order differential equation used to model certain types of damped and driven oscillations.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from scipy.integrate import odeint

# Duffing oscillator differential equation
def duffing_oscillator(state, t, alpha, beta, delta, gamma, omega):
    x, y = state  # state = [x, y] where x is position and y is velocity
    return [y, -delta*y - alpha*x - beta*x**3 + gamma*np.cos(omega*t)]

# Parameters
alpha = -1
beta = 1
delta = 0.3
gamma = 0.37
omega = 1.2

# Time array
t = np.linspace(0, 40, 10000)

# Initial condition
initial_state = [0, 0]

# Solve Duffing equation
solution = odeint(duffing_oscillator, initial_state, t, args=(alpha, beta, delta, gamma, omega))

# Plotting in 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(solution[:, 0], solution[:, 1], t)
ax.set_title("Phase Space of the Duffing Oscillator")
ax.set_xlabel("Position (x)")
ax.set_ylabel("Velocity (y)")
ax.set_zlabel("Time")
plt.show()
