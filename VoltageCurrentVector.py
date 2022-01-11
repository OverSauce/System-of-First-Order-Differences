import numpy as np
import matplotlib.pyplot as plt
import time as tt

""" Series LC circuit with 1V DC source starting at t=0s """
""" v[n+1] = v[n] + (dt/C)*i[n] """
""" i[n] = i[n-1] + (dt/L)*(V[n] - v[n]) """

""" Series RLC circuit with 1V DC source starting at t=0s """
""" v[n+1] = v[n] + (dt/C)*i[n] """
""" i[n] = i[n-1] + (dt/L)*(V[n] - v[n] - R*i[n-1]) """

def gaussian(t, sig, mu):
    return np.exp(-((t - mu)/(2*sig))**2) # (1/np.sqrt(2*np.pi*sig**2))

T = 1e-1
N = 1000
t = np.linspace(0, T, N)

L = 100e-3
C = 100e-6
R = 10

dt = T/N
dtL = dt/L
dtC = dt/C

v = np.zeros(N)
i = np.zeros(N)
V = 1 + np.zeros(N)

def difEqSysInSingleLoop(i, v, V):
    for n in range(N-1):
        i[n] = i[n-1] + dtL*(V[n] - v[n] - R*i[n-1]) # - R*i[n-1]
        v[n+1] = v[n] + dtC*i[n]
    return i, v

def plotter(t, v, strs="Unit", titl="Title"):
    plt.clf()
    plt.plot(t, v)
    plt.xlabel("sec")
    plt.ylabel(strs)
    plt.title(titl)
    plt.show()

# t0 = tt.time()

i, v = difEqSysInSingleLoop(i, v, V)

# t1 = tt.time()

# print("Runtime: " + str(1000*(t1-t0)) + " ms for " + str(N) + " elements")

# plotter(t, V)
# plotter(t, v, strs="Volt", titl="Voltage over Cap")
# plotter(t, i*R, strs="Volt", titl="Voltage over Resistor")
# plotter(t, i, strs="Ampere", titl="Current")

plt.figure()
plt.plot(v, i)
plt.xlabel("Voltage")
plt.ylabel("Current")
plt.show()