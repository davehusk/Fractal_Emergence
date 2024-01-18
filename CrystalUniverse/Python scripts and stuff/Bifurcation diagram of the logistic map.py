# Let's create a simple demonstration of a nonlinear system. One classic example is the logistic map, 
# a nonlinear recurrence relation that demonstrates how complex, chaotic behaviour can arise from very simple non-linear dynamical equations.

import matplotlib.pyplot as plt
import numpy as np

# Logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Setup parameters
r_values = np.linspace(2.5, 4.0, 1000)  # Range of the parameter r
iterations = 1000  # Number of iterations
last = 100  # Number of last points to plot to illustrate convergence

# Iterate and plot
x = 1e-5 * np.ones(len(r_values))  # Initial condition
plt.figure(figsize=(10, 6))

for _ in range(iterations):
    x = logistic_map(r_values, x)
    # We display only the last iterations to show the attractors
    if _ > (iterations - last):
        plt.plot(r_values, x, ',k', alpha=0.25)

plt.title("Bifurcation diagram of the logistic map")
plt.xlabel("r")
plt.ylabel("x")
plt.show()
