# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:19:23 2019

@author: POLO
"""

import cweq as cw
from astropy import units as u
import numpy as np
import math
import matplotlib.pyplot as plt

R = 7144000  # semimayor target axis (m)
Rc = 7141000  # semimayor chaser init axis (m)
mu = 3.9857128e14  # SI
w = math.sqrt(mu / R ** 3)
r0 = [-17000, 0, 3000]  # initial starting position

v_dif_alt = 1.5 * w * r0[2]

rdot0 = [v_dif_alt, 0, 0]  # initial velocity  (m/s)

# Añadimos esto para hacer una prueba

T = 2 * math.pi * math.sqrt(R ** 3 / mu)
V_abs = math.sqrt(mu / (R - 3000))

a = int(T / 2)

nframes = 1500  # Free drift until -3000m
nframes2 = a  # Hohmann first impulse time: Half period
nframes3 = a  # Hohmann second impulse time: Half period in Keeping point
nframes4 = a  # Radial impulse from -2900 to -500 m
nframes5 = 1300  #
nframes6 = 2 * a
nframes7 = 0


xs = []
ys = []
zs = []
ds = []
xdots = []

for i in range(nframes):
    t = i
    r_vec = cw.CW2(r0, rdot0, w, t)[0]
    rdot_vec = cw.CW2(r0, rdot0, w, t)[1]
    x = r_vec[0]
    y = r_vec[1]
    z = r_vec[2]
    xdot = rdot_vec[0]
    ydot = rdot_vec[1]
    zdot = rdot_vec[2]
    rdot = [xdot, ydot, zdot]
    d = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    ds.append(d)
    xs.append(x)
    ys.append(y)
    zs.append(z)
    xdots.append(xdot)
    v = math.sqrt(xdot ** 2 + ydot ** 2 + zdot ** 2)

V = 0.784443554086188

r0 = [x, y, z]
deltav = [V, 0, 0]

for i in range(len(rdot)):
    rdot0[i] = rdot[i] + deltav[i]


for i in range(nframes2):
    t = i
    r_vec = cw.CW2(r0, rdot0, w, t)[0]
    rdot_vec = cw.CW2(r0, rdot0, w, t)[1]
    x = r_vec[0]
    y = r_vec[1]
    z = r_vec[2]
    xdot = rdot_vec[0]
    ydot = rdot_vec[1]
    zdot = rdot_vec[2]
    rdot = [xdot, ydot, zdot]
    d = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    ds.append(d)
    xs.append(x)
    ys.append(y)
    zs.append(z)
    xdots.append(xdot)

    v = math.sqrt(xdot ** 2 + ydot ** 2 + zdot ** 2)

r0 = [x, y, z]
deltav = [0.7843611877178878, 0, 0]
for i in range(len(rdot)):
    rdot0[i] = rdot[i] + deltav[i]


for i in range(nframes3):
    t = i
    r_vec = cw.CW2(r0, rdot0, w, t)[0]
    rdot_vec = cw.CW2(r0, rdot0, w, t)[1]
    x = r_vec[0]
    y = r_vec[1]
    z = r_vec[2]
    xdot = rdot_vec[0]
    ydot = rdot_vec[1]
    zdot = rdot_vec[2]
    rdot = [xdot, ydot, zdot]
    d = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    ds.append(d)
    xs.append(x)
    ys.append(y)
    zs.append(z)
    xdots.append(xdot)

    v = math.sqrt(xdot ** 2 + ydot ** 2 + zdot ** 2)

Vx = 0.3
xf = -500
xi = r_vec[0]
var_x = xf - xi
var_v_z = w * var_x * 0.25


r0 = [x, y, z]
deltav = [0, 0, var_v_z]
for i in range(len(rdot)):
    rdot0[i] = rdot[i] + deltav[i]


for i in range(nframes4):
    t = i
    r_vec = cw.CW2(r0, rdot0, w, t)[0]
    rdot_vec = cw.CW2(r0, rdot0, w, t)[1]
    x = r_vec[0]
    y = r_vec[1]
    z = r_vec[2]
    xdot = rdot_vec[0]
    ydot = rdot_vec[1]
    zdot = rdot_vec[2]
    rdot = [xdot, ydot, zdot]
    d = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    ds.append(d)
    xs.append(x)
    ys.append(y)
    zs.append(z)
    xdots.append(xdot)

    v = math.sqrt(xdot ** 2 + ydot ** 2 + zdot ** 2)


r0 = [x, y, z]
deltav = [0, 0, var_v_z]
for i in range(len(rdot)):
    rdot0[i] = rdot[i] + deltav[i]


for i in range(nframes4):
    t = i
    r_vec = cw.CW2(r0, rdot0, w, t)[0]
    rdot_vec = cw.CW2(r0, rdot0, w, t)[1]
    x = r_vec[0]
    y = r_vec[1]
    z = r_vec[2]
    xdot = rdot_vec[0]
    ydot = rdot_vec[1]
    zdot = rdot_vec[2]
    rdot = [xdot, ydot, zdot]
    d = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    ds.append(d)
    xs.append(x)
    ys.append(y)
    zs.append(z)
    xdots.append(xdot)

    v = math.sqrt(xdot ** 2 + ydot ** 2 + zdot ** 2)


Vx = 0.3
xf = -100
t1 = (xf - x) / Vx


r0 = [x, y, z]
deltav = [0.3, 0, 0]
for i in range(len(rdot)):
    rdot0[i] = rdot[i] + deltav[i]


for i in range(nframes5):
    t = i
    gam = [0, 0, 2 * w * Vx]
    # ESTO ES PARA EL FORCED MOTION EN X CUANDO ESTAMOS EN Z0
    r_vec = cw.CW(r0, rdot0, w, t, gam)[0]
    rdot_vec = cw.CW(r0, rdot0, w, t, gam)[1]
    x = r_vec[0]
    y = r_vec[1]
    z = r_vec[2]
    xdot = rdot_vec[0]
    ydot = rdot_vec[1]
    zdot = rdot_vec[2]
    rdot = [xdot, ydot, zdot]

    d = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    ds.append(d)
    xs.append(x)
    ys.append(y)
    zs.append(z)
    xdots.append(xdot)

    v = math.sqrt(xdot ** 2 + ydot ** 2 + zdot ** 2)


r0 = [x, y, z]
deltav = [-0.3, 0, 0]
for i in range(len(rdot)):
    rdot0[i] = rdot[i] + deltav[i]


for i in range(nframes5):
    t = i
    gam = [0, 0, 0]
    # ESTO ES PARA EL FORCED MOTION EN X CUANDO ESTAMOS EN Z0
    r_vec = cw.CW(r0, rdot0, w, t, gam)[0]
    rdot_vec = cw.CW(r0, rdot0, w, t, gam)[1]
    x = r_vec[0]
    y = r_vec[1]
    z = r_vec[2]
    xdot = rdot_vec[0]
    ydot = rdot_vec[1]
    zdot = rdot_vec[2]
    rdot = [xdot, ydot, zdot]

    d = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    ds.append(d)
    xs.append(x)
    ys.append(y)
    zs.append(z)
    xdots.append(xdot)

    v = math.sqrt(xdot ** 2 + ydot ** 2 + zdot ** 2)

xf = 100
xi = r_vec[0]
var_x = xf - xi
var_v_z = w * var_x * 0.25


r0 = [x, y, z]
deltav = [0, 0, var_v_z]
for i in range(len(rdot)):
    rdot0[i] = rdot[i] + deltav[i]


for i in range(nframes6):
    t = i
    r_vec = cw.CW2(r0, rdot0, w, t)[0]
    rdot_vec = cw.CW2(r0, rdot0, w, t)[1]
    x = r_vec[0]
    y = r_vec[1]
    z = r_vec[2]
    xdot = rdot_vec[0]
    ydot = rdot_vec[1]
    zdot = rdot_vec[2]
    rdot = [xdot, ydot, zdot]
    d = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    ds.append(d)
    xs.append(x)
    ys.append(y)
    zs.append(z)
    xdots.append(xdot)

    v = math.sqrt(xdot ** 2 + ydot ** 2 + zdot ** 2)


"""


r0 = [x, y, z]
deltav = [0, 0, Vz]
for i in range(len(rdot)):
    rdot0[i] = rdot[i]+deltav[i]


for i in range(nframes7):
    t = i 
    gam = [-2*w*Vz, 0, -3*(w**2)*(Vz*t+r0[2])] 
    #ESTO ES PARA EL FORCED MOTION EN X CUANDO ESTAMOS EN Z0
    r_vec= cw.CW(r0, rdot0, w, t, gam)[0]
    rdot_vec = cw.CW(r0, rdot0, w, t, gam)[1]
    x = r_vec[0]
    y = r_vec[1]
    z = r_vec[2]
    xdot = rdot_vec[0]
    ydot = rdot_vec[1]
    zdot = rdot_vec[2]
    rdot = [xdot, ydot, zdot]
    d = math.sqrt(x**2+y**2+z**2)
    ds.append(d)
    xs.append(x)
    ys.append(y)
    zs.append(z)
    xdots.append(xdot)

    
    v = math.sqrt(xdot**2+ydot**2+zdot**2)

"""


fig = plt.figure()
plt.plot(xs, zs, "r-")
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.ylabel("$R$-Bar ($m$)")
plt.xlabel("$V$-Bar ($m$)")
# plt.legend()
plt.grid(linestyle="-")
plt.title("Relative movement")
