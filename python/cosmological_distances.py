
##############################################################################################
# Ayden Cook

import numpy as np
import matplotlib.pyplot as plt

SAVE_FIGURES = False

##############################################################################################
# Constants

H_0 = 1/14  # current value of hubble's constant, in units of 1/Gyr
c = 0.3066013938  # speed of light, in units of Gpc/Gyr

# proportionality constants for the energy density of...
omega_m = 0.32  # matter
omega_lambda = 0.68  # the cosmological constant
omega_r = 0  # radiation

# current age of the universe in Gyr. satisfies a(t_0) = 1
t_0 = (2/(3*np.sqrt(omega_lambda)*H_0)) * np.arcsinh(np.sqrt(omega_lambda/omega_m))

##############################################################################################
# Part 1: Scale Factor versus Time

# values of time to plot
plot_t = np.linspace(0, t_0*1.5, 1000)


# calculates the scale factor at time t
def a(t):
    return (omega_m/omega_lambda)**(1/3) * np.sinh(3*np.sqrt(omega_lambda)*H_0*t/2)**(2/3)


figure = plt.figure("Scale Factor vs Time")
axes = figure.add_subplot()
plt.title("Scale Factor vs Time")
plt.grid(which="major")
axes.set_xlabel("Time (Gyr)")
axes.set_ylabel("Scale Factor")
axes.minorticks_on()
axes.plot(plot_t, a(plot_t))
axes.scatter(t_0, 1, color="black", zorder=3)
axes.text(t_0+0.5, 0.9, "Present")
plt.savefig("scale_vs_time.png", dpi=400) if SAVE_FIGURES else plt.show()

##############################################################################################
# Part 2: Comoving Distance versus Redshift

# values of time for plot
plot_t = np.linspace(0.01, t_0, 1000)


# calculates the redshift at time t
def z(t):
    return 1/a(t) - 1


# calculates the comoving distance given a lookback time t_l
def d_c(t_l, steps=1000):
    start = t_0 - t_l
    end = t_0
    dt = (end - start)/steps
    def f(t): return c/a(t)
    sum = 0
    for i in range(steps):
        sum += f(start + i*dt)*dt
    return sum


figure = plt.figure("Comoving Distance vs Redshift")
axes = figure.add_subplot()
plt.title("Comoving Distance vs Redshift")
plt.grid(which="major")
axes.set_xlabel("Redshift")
axes.set_ylabel("Comoving Distance (Gpc)")
axes.minorticks_on()
axes.plot(z(plot_t), d_c(t_0-plot_t))
plt.savefig("comoving_vs_redshift.png", dpi=400) if SAVE_FIGURES else plt.show()


##############################################################################################
# Part 3: Luminosity Distance versus Redshift

# values of time for plot
plot_t = np.linspace(0.1, t_0, 1000)


# calculates the luminosity distance given a lookback time t_l
def d_l(t_l, steps=1000):
    return d_c(t_l, steps=steps)*(1 + z(t_0-t_l))


figure = plt.figure("Luminosity Distance vs Redshift")
axes = figure.add_subplot()
plt.title("Luminosity Distance vs Redshift")
plt.grid(which="major")
axes.set_xlabel("Redshift")
axes.set_ylabel("Luminosity Distance (Gpc)")
axes.minorticks_on()
axes.plot(z(plot_t), d_l(t_0-plot_t))
plt.savefig("luminosity_vs_redshift.png", dpi=400) if SAVE_FIGURES else plt.show()

##############################################################################################
# Part 4: Angular Diameter Distance versus Redshift

# values of time for plot
plot_t = np.linspace(0.1, t_0, 1000)


# calculates the angular diameter distance given a lookback time t_l
def d_a(t_l, steps=1000):
    return d_c(t_l, steps=steps)/(1 + z(t_0-t_l))


figure = plt.figure("Angular Diameter Distance vs Redshift")
axes = figure.add_subplot()
plt.title("Angular Diameter Distance vs Redshift")
plt.grid(which="major")
axes.set_xlabel("Redshift")
axes.set_ylabel("Angular Diameter Distance (Gpc)")
axes.minorticks_on()
axes.plot(z(plot_t), d_a(t_0-plot_t))
plt.savefig("angular_dist_vs_redshift.png", dpi=400) if SAVE_FIGURES else plt.show()

##############################################################################################
# Part 5: Angular Size versus Redshift

plot_t = np.linspace(0.05, t_0 - 0.05, 1000)  # values of time for plot
size = 50.E-6  # size of object in Gpc (50 kpc)


# calculates the angular size of an object given its size s and lookback time t_l
def s_a(s, t_l, steps=1000):
    return s/d_a(t_l, steps=steps)


figure = plt.figure("Angular Size vs Redshift")
axes = figure.add_subplot()
plt.title("Angular Size vs Redshift")
plt.grid(which="major")
plt.yscale("log")
axes.set_xlabel("Redshift")
axes.set_ylabel("Angular Size")
axes.minorticks_on()
axes.plot(z(plot_t), s_a(size, t_0-plot_t), label="Size: {} kpc".format(size*10**6))
axes.legend()
plt.savefig("angular_size_vs_redshift.png", dpi=400) if SAVE_FIGURES else plt.show()

##############################################################################################
