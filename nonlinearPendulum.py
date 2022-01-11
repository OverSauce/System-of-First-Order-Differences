import numpy as np
import matplotlib.pyplot as plt

""" Equations """
""" (1/dt)*(u[n+1] - u[n]) = v[n] """
""" (1/dt)*(v[n+1] - v[n]) = - mu*v[n] - (g/L)*sin(u[n]) """

N = 1000
t0 = 0 # Start of the observation
t1 = 20 # End of the observation
t = np.linspace(t0, t1, N) # Time as linear space
dt = (t1-t0) / N # Timestep, also sampling period

mu = .5 # Air resistance 
g = 9.81 # Gravitational acceleration
L = 1 # Length of the string

u = np.zeros(N) # Angle, over time
v = np.zeros(N) # Derivative of angle, over time

u[0] = 15*np.pi/16 # Initial condition, angle

for n in range(N-1):
    u[n+1] = u[n] + dt*v[n]
    v[n+1] = v[n] + dt*(- mu*v[n] - (g/L)*np.sin(u[n]))

plt.figure()
plt.plot(u, v)
plt.show()
