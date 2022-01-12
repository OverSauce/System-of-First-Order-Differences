import differenceLib as df

i, v, t = df.currentVoltageSystem(tims=[0, 1e-1, 1000])

df.plotter3D(i, v, t, xstr="Current(A)", ystr="Voltage(V)")

u, v, t = df.nonLinearPendulum(tims=[0, 10, 1000])

df.plotter3D(u/df.np.pi, v, t, xstr="Angle (x$\pi$)", ystr="Angular Velocity")
