import numpy as np
import matplotlib.pyplot as plt

def plotter3D(u, v, t, xstr="x", ystr="y"):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    plt.plot(u, v, t)
    plt.xlim(-max(u), max(u))
    plt.ylim(-max(v), max(v))
    plt.xlabel(xstr)
    plt.ylabel(ystr)
    plt.show()

""" Non-linear Pendulum Equations """
""" (1/dt)*(u[n+1] - u[n]) = v[n] """
""" (1/dt)*(v[n+1] - v[n]) = - mu*v[n] - (g/L)*sin(u[n]) """

def nonLinearPendulum(mu=.1, g=9.81, L=1, tims=[]):       # mu = air resistance; g gravitational acceleration; L = length of the string
    dt = tims[0] + (tims[1] - tims[0]) / tims[2]
    u = np.zeros(tims[2])                           # Angle, over time
    v = np.zeros(tims[2])                           # Derivative of angle, over time
    t = np.linspace(tims[0], tims[1], tims[2])      # Time as linear space
    u[0] = 15*np.pi/16                              # Initial condition, angle
    for n in range(int(tims[2]-1)):
        u[n+1] = u[n] + dt*v[n]
        v[n+1] = v[n] + dt*(- mu*v[n] - (g/L)*np.sin(u[n]))
    return u, v, t

""" Series LC circuit with 1V DC source starting at t=0s """
""" v[n+1] = v[n] + (dt/C)*i[n] """
""" i[n] = i[n-1] + (dt/L)*(V[n] - v[n]) """

""" Series RLC circuit with 1V DC source starting at t=0s """
""" v[n+1] = v[n] + (dt/C)*i[n] """
""" i[n] = i[n-1] + (dt/L)*(V[n] - v[n] - R*i[n-1]) """

def currentVoltageSystem(R=10, L=100e-3, C=100e-6, tims=[]):
    dt = tims[0] + (tims[1] - tims[0]) / tims[2]
    i = np.zeros(tims[2])                                   # Angle, over time
    v = np.zeros(tims[2])                                   # Derivative of angle, over time
    V = 10 + np.zeros(tims[2])
    t = np.linspace(tims[0], tims[1], tims[2])              # Time as linear space
    for n in range(int(tims[2]-1)):
        i[n] = i[n-1] + (dt/L)*(V[n] - v[n] - R*i[n-1])     # - R*i[n-1]
        v[n+1] = v[n] + (dt/C)*i[n]
    return i, v, t

# def gaussian(t, sig, mu):
#     return np.exp(-((t - mu)/(2*sig))**2) # (1/np.sqrt(2*np.pi*sig**2))

def derivative(u):
    N = len(u)
    temp = u
    for n in range(N-1):
        u[n] = temp[n+1] - temp[n]
    u[N-1] = u[N-2]
    return u
