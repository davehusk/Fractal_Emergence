# To illustrate the concept of solitons in a lattice structure and their analogy to electromagnetic waves and possibly gravitational waves, we can simulate a simple one-dimensional chain of oscillators.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for the simulation
length_of_chain = 100  # Number of oscillators in the chain
spring_constant = 1  # Spring constant (k)
mass = 1  # Mass of each oscillator
initial_displacement = 1  # Initial displacement for the soliton wave

# Create an array to hold the displacement of each oscillator
displacements = np.zeros(length_of_chain)

# Initialize the displacement of a few oscillators in the middle of the chain to create a soliton wave
displacements[length_of_chain//2 - 5:length_of_chain//2 + 5] = initial_displacement

# Function to update the positions of oscillators
def update_displacements(d, k, m):
    # Create a new array to hold the updated positions
    new_d = np.copy(d)
    for i in range(1, len(d) - 1):
        # Update based on the difference with neighboring oscillators
        new_d[i] = d[i] + (k/m) * (d[i-1] - 2*d[i] + d[i+1])
    return new_d

# Number of time steps for the simulation
time_steps = 100

# Create a figure for plotting
plt.figure(figsize=(10, 6))

# Plot the initial state of the chain
plt.plot(displacements, label='Initial State')
plt.title('Soliton in a One-Dimensional Chain of Oscillators')
plt.xlabel('Oscillator Index')
plt.ylabel('Displacement')
plt.ylim(-1.5*initial_displacement, 1.5*initial_displacement)
plt.legend()

# Update the positions over time and plot
for _ in range(time_steps):
    displacements = update_displacements(displacements, spring_constant, mass)
    if _ % 20 == 0:  # Plot every 20 time steps
        plt.plot(displacements, label=f'Time step {_}')

plt.legend()
plt.show()
