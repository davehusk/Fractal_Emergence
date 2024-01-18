# Another example of a nonlinear dynamical system is the Van der Pol oscillator. 
# The Van der Pol oscillator is a non-conservative oscillator with non-linear damping. It evolves in time according to a second-order differential equation.

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def van_der_pol_oscillator(state, t, mu):
    x, y = state  # state = [x, y] where x is position and y is velocity
    return [y, mu * (1 - x**2) * y - x]

# Van der Pol oscillator parameter
mu = 3.0

# Initial condition
initial_state = [2.0, 0.0]

# Time array
t = np.linspace(0, 30, 5000)

# Solve Van der Pol equation
solution = odeint(van_der_pol_oscillator, initial_state, t, args=(mu,))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(solution[:, 0], solution[:, 1])
plt.title("Phase Space of the Van der Pol Oscillator")
plt.xlabel("Position (x)")
plt.ylabel("Velocity (y)")
plt.grid()
plt.show()
