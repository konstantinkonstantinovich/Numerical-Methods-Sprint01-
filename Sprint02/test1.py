from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

# Concentration over time
N = lambda t: N0 * np.exp(-k * t)
# dN/dt
def dx_dt(x):
    return -k * x

k = .5
h = 0.001
N0 = 100.

t = np.arange(0, 10, h)
y = np.zeros(len(t))

y[0] = N0
for i in range(1, len(t)):
    # Euler method
    y[i] = y[i-1] + dx_dt(y[i-1]) * h

max_error = abs(y-N(t)).max()
print ('Max difference between the exact solution and Euler approximation with step size h=0.001:')

print ('{0:.15}'.format(max_error))