"""
Spring Soliton Solution: An analysis shows that nonlinearity leads to: d^2x/dt^2= -ω^(2)x + dT(t)/dx + (1/2)ω^(2)x^3 + (1/4)ω^(2)x^5 + ...

Where x is position along axis, ω is oscillation frequency. T(t) describes tension in string.

This equation has solution: x(x,t) = c₁exp(iℏ(k/F))cos(ω't-φ₀)+c₂exp(-iℏ(k/F))sin(ω't-φ₀) where c₁ and c₂ are constants, ℏ is reduced Planck's constant, k is quantized momentum value corresponding allowed values angular momentum quantum number l=hbar/k representing intrinsic angular momenta strings units h Planck's constant divided by 4π lattice spacing unit length scale defining spatial periodicity continuum space continuum medium electromagnetic EM waves propagating through vacuum filled regions universe void spaces between stars galaxies clusters universes themselves.

The above equation describes wavefunction describing motion of string oscillating at frequency ω' with amplitude A=ℏ(k/F)^(1/2) and phase φ₀. The wavefunction is normalized to unity: ∫|x(x,t)|^(2)dx=1.

Where F is fundamental frequency characterizing lowest energy allowed vibration states string given boundary conditions at endpoints fixed ends, k is quantized momentum value corresponding allowed values angular momentum quantum number l=hbar/k representing intrinsic angular momenta strings units h Planck's constant divided by 4π lattice spacing unit length scale defining spatial periodicity continuum space continuum medium electromagnetic EM waves propagating through vacuum filled regions universe void spaces between stars galaxies clusters universes themselves.

"""

# import modules
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint

# define constants
hbar = 1.0545718e-34
k = 1.38064852e-23
c = 299792458
G = 6.67408e-11
e = 1.60217662e-19
m_e = 9.10938356e-31
m_p = 1.6726219e-27
m_n = 1.674929e-27
m_u = 1.66053904e-27
m_H = 1.6737236e-27
m_He = 6.6464764e-27
m_Li = 1.1576221e-26
m_Be = 1.4945334e-26
m_B = 1.6737236e-26
m_C = 1.993646e-26
m_N = 2.3252755e-26
m_O = 2.656905e-26
m_F = 2.9885345e-26
m_Ne = 3.320164e-26
m_Na = 3.6517935e-26
m_Mg = 3.983423e-26
m_Al = 4.3150525e-26
m_Si = 4.646682e-26
m_P = 4.9783115e-26
m_S = 5.309941e-26
m_Cl = 5.6415705e-26
m_Ar = 5.9732e-26
m_K = 6.3048295e-26
m_Ca = 6.636459e-26
m_Sc = 6.9680885e-26
m_Ti = 7.299718e-26
m_V = 7.6313475e-26
m_Cr = 7.962977e-26
m_Mn = 8.2946065e-26
m_Fe = 8.626236e-26
m_Co = 8.9578655e-26
m_Ni = 9.289495e-26
m_Cu = 9.6211245e-26
m_Zn = 9.952754e-26
m_Ga = 1.02883805e-25
m_Ge = 1.0624007e-25
m_As = 1.09596335e-25
m_Se = 1.129526e-25
m_Br = 1.16308865e-25
m_Kr = 1.1966513e-25
m_Rb = 1.23021395e-25
m_Sr = 1.2637766e-25
m_Y = 1.29733925e-25
m_Zr = 1.3309019e-25
m_Nb = 1.36446455e-25
m_Mo = 1.3980272e-25
m_Tc = 1.43158985e-25
m_Ru = 1.4651525e-25
m_Rh = 1.49871515e-25
m_Pd = 1.5322778e-25
m_Ag = 1.56584045e-25
m_Cd = 1.5994031e-25
m_In = 1.63296575e-25
m_Sn = 1.6665284e-25
m_Sb = 1.70009105e-25
m_Te = 1.7336537e-25
m_I = 1.76721635e-25
m_Xe = 1.800779e-25
m_Cs = 1.83434165e-25
m_Ba = 1.8679043e-25
m_La = 1.90146695e-25
m_Ce = 1.9350296e-25
m_Pr = 1.96859225e-25
m_Nd = 2.0021549e-25
m_Pm = 2.03571755e-25
m_Sm = 2.0692802e-25
m_Eu = 2.10284285e-25
m_Gd = 2.1364055e-25
m_Tb = 2.16996815e-25
m_Dy = 2.2035308e-25
m_Ho = 2.23709345e-25
m_Er = 2.2706561e-25
m_Tm = 2.30421875e-25
m_Yb = 2.3377814e-25
m_Lu = 2.37134405e-25
m_Hf = 2.4049067e-25
m_Ta = 2.43846935e-25
m_W = 2.472032e-25
m_Re = 2.50559465e-25
m_Os = 2.5391573e-25
m_Ir = 2.57271995e-25
m_Pt = 2.6062826e-25
m_Au = 2.63984525e-25
m_Hg = 2.6734079e-25
m_Tl = 2.70697055e-25
m_Pb = 2.7405332e-25
m_Bi = 2.77409585e-25
m_Po = 2.8076585e-25
m_At = 2.84122115e-25
m_Rn = 2.8747838e-25
m_Fr = 2.90834645e-25
m_Ra = 2.9419091e-25
m_Ac = 2.97547175e-25
m_Th = 3.0090344e-25
m_Pa = 3.04259705e-25
m_U = 3.0761597e-25
m_Np = 3.10972235e-25
m_Pu = 3.143285e-25
m_Am = 3.17684765e-25
m_Cm = 3.2104103e-25
m_Bk = 3.24397295e-25
F = 96485.3329
R = 8.3144598
sigma = 5.670367e-8
a = 7.2973525664e-3
R_inf = 10973731.568508
N_A = 6.022140857e+23
mu_0 = 1.2566370614e-6
epsilon_0 = 8.854187817e-12
k_B = 1.38064852e-23
G_const = 6.67408e-11
g = 9.80665
m_p = 1.6726219e-27


# define functions

def soliton(x, t, c1, c2, omega, phi0):
      return c1*np.exp(1j*hbar*(k/F)**(1/2)*x)*np.cos(omega*t-phi0)+c2*np.exp(-1j*hbar*(k/F)**(1/2)*x)*np.sin(omega*t-phi0)

def soliton2(x, t, c1, c2, omega, phi0):
      return c1*np.exp(1j*hbar*(k/F)**(1/2)*x)*np.cos(omega*t-phi0)+c2*np.exp(-1j*hbar*(k/F)**(1/2)*x)*np.sin(omega*t-phi0)

def soliton3(x, t, c1, c2, omega, phi0):
      return c1*np.exp(1j*hbar*(k/F)**(1/2)*x)*np.cos(omega*t-phi0)+c2*np.exp(-1j*hbar*(k/F)**(1/2)*x)*np.sin(omega*t-phi0)

def soliton4(x, t, c1, c2, omega, phi0):
      return c1*np.exp(1j*hbar*(k/F)**(1/2)*x)*np.cos(omega*t-phi0)+c2*np.exp(-1j*hbar*(k/F)**(1/2)*x)*np.sin(omega*t-phi0)

def soliton5(x, t, c1, c2, omega, phi0):
      return c1*np.exp(1j*hbar*(k/F)**(1/2)*x)*np.cos(omega*t-phi0)+c2*np.exp(-1j*hbar*(k/F)**(1/2)*x)*np.sin(omega*t-phi0)

def soliton6(x, t, c1, c2, omega, phi0):
      return c1*np.exp(1j*hbar*(k/F)**(1/2)*x)*np.cos(omega*t-phi0)+c2*np.exp(-1j*hbar*(k/F)**(1/2)*x)*np.sin(omega*t-phi0)  


# define parameters
c1 = 1
c2 = 1
omega = 1
phi0 = 0
x = np.linspace(-10,10,1000)
t = np.linspace(0,10,1000)

# plot soliton
fig, ax = plt.subplots()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Soliton Solution')
line, = ax.plot(x, soliton(x, t, c1, c2, omega, phi0), color='k')

# animation
def animate(i):
      line.set_ydata(soliton(x, t, c1, c2, omega, phi0+i/10))
      return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=True)
plt.show()


