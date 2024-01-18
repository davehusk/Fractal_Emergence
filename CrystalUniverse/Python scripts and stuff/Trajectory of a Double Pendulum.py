# Let's consider the double pendulum as an example, a well-known physical system that exhibits chaotic behavior. 
# The double pendulum consists of two pendulums attached end to end, where the motion of one directly influences the other.

from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt


# Double Pendulum Differential Equations
def double_pendulum(t, state, l1, l2, m1, m2, g):
    theta1, z1, theta2, z2 = state

    # Equations of motion
    c, s = np.cos(theta1 - theta2), np.sin(theta1 - theta2)

    theta1_dot = z1
    z1_dot = (m2*g*np.sin(theta2)*c - m2*s*(l1*z1**2*c + l2*z2**2) -
              (m1+m2)*g*np.sin(theta1)) / l1 / (m1 + m2*s**2)

    theta2_dot = z2
    z2_dot = ((m1+m2)*(l1*z1**2*s - g*np.sin(theta2) + g*np.sin(theta1)*c) +
              m2*l2*z2**2*s*c) / l2 / (m1 + m2*s**2)

    return [theta1_dot, z1_dot, theta2_dot, z2_dot]

# Parameters
l1, l2 = 1.0, 1.0  # Length of the pendulums
m1, m2 = 1.0, 1.0  # Mass of the pendulums
g = 9.81  # Acceleration due to gravity

# Initial conditions
initial_state = [np.pi / 2, 0, np.pi / 2, 0]  # Initial angles and velocities

# Time array
t_span = [0, 30]  # Time span for the simulation
t_eval = np.linspace(*t_span, 1000)  # Time points at which to solve

# Solve the differential equations
solution = solve_ivp(double_pendulum, t_span, initial_state, args=(l1, l2, m1, m2, g),
                     t_eval=t_eval, method='RK45')

# Extracting angles for plotting
theta1, theta2 = solution.y[0], solution.y[2]

# Converting to Cartesian coordinates for visualization
x1 = l1 * np.sin(theta1)
y1 = -l1 * np.cos(theta1)

x2 = x1 + l2 * np.sin(theta2)
y2 = y1 - l2 * np.cos(theta2)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x1, y1, label="Pendulum 1")
plt.plot(x2, y2, label="Pendulum 2")
plt.title("Trajectory of a Double Pendulum")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.legend()
plt.grid()
plt.show()
