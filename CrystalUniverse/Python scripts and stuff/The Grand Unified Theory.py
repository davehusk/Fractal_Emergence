# The Grand Unified Theory (GUT) is a theoretical framework in physics that aims to unify the three fundamental forces 
# (electromagnetic, weak nuclear, and strong nuclear forces) into a single theoretical framework. 
# While a complete GUT is not yet established in physics, we can illustrate aspects of these forces separately.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1. Electromagnetic Force: Illustrated through the motion of a charged particle in a magnetic field (Lorentz Force).
def electromagnetic_motion(t, state, q, B):
    vx, vy, vz = state  # Velocity components of the charged particle
    # Lorentz force components (assuming a uniform magnetic field in the z-direction)
    Fx = q * (vy * B)
    Fy = -q * (vx * B)
    Fz = 0
    return [Fx, Fy, Fz]

# Charge and magnetic field strength
q = 1.0  # Charge of the particle
B = 1.0  # Magnetic field strength

# Initial conditions: velocity of the charged particle
initial_velocity = [0, 1, 0]  # Initial velocity

# Time array
t_span_em = [0, 10]
t_eval_em = np.linspace(*t_span_em, 1000)

# Solve for electromagnetic motion
solution_em = solve_ivp(electromagnetic_motion, t_span_em, initial_velocity, args=(q, B),
                        t_eval=t_eval_em, method='RK45')

# 2. Weak Nuclear Force: Illustrated through beta decay process (simplified model).
# Beta decay is a process where a neutron decays into a proton, emitting an electron and an antineutrino.
# For simplicity, we represent this as a time-dependent probability function.

def beta_decay_probability(t, tau):
    return 1 - np.exp(-t / tau)

# Mean lifetime of a neutron (in seconds)
tau_neutron = 881.5

# Time array for beta decay
t_beta_decay = np.linspace(0, tau_neutron * 3, 1000)

# Calculate beta decay probability
p_beta_decay = beta_decay_probability(t_beta_decay, tau_neutron)

# 3. Strong Nuclear Force: Illustrated through the binding energy of a nucleus (Semi-Empirical Mass Formula).
def binding_energy(A, Z):
    # Constants in the semi-empirical mass formula
    a_v = 15.75
    a_s = 17.8
    a_c = 0.711
    a_sym = 23.7
    a_p = 11.2

    # Binding energy formula
    B = (a_v * A - a_s * A**(2/3) - a_c * Z * (Z - 1) / A**(1/3) -
         a_sym * (A - 2*Z)**2 / A)
    # Pairing term
    if A % 2 == 0:
        if Z % 2 == 0:
            B += a_p / A**(1/2)
        else:
            B -= a_p / A**(1/2)
    return B

# Example nucleus (Iron-56)
A_iron = 56
Z_iron = 26

# Calculate binding energy
B_iron = binding_energy(A_iron, Z_iron)

# Plotting
plt.figure(figsize=(15, 5))

# Electromagnetic Force Plot
plt.subplot(1, 3, 1)
plt.plot(solution_em.t, solution_em.y[0], label='Fx')
plt.plot(solution_em.t, solution_em.y[1], label='Fy')
plt.title("Electromagnetic Motion")
plt.xlabel("Time")
plt.ylabel("Force")
plt.legend()

# Weak Nuclear Force Plot
plt.subplot(1, 3, 2)
plt.plot(t_beta_decay, p_beta_decay)
plt.title("Beta Decay Probability")
plt.xlabel("Time")
plt.ylabel("Probability")

# Strong Nuclear Force Plot
plt.subplot(1, 3, 3)
plt.bar(["Iron-56"], [B_iron])
plt.title("Binding Energy of Nucleus")
plt.xlabel("Nucleus")
plt.ylabel("Binding Energy (MeV)")

plt.tight_layout()
plt.show()

B_iron
