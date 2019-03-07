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

r0=[-17000,0,3000]      #initial starting position
rdot0=[4.704931942091908,0,0]          #initial velocity  (m/s)
R= 7144e3                  #semimayor axis (m)
mu = 3.9857128e14           #SI
w =math.sqrt(mu/R**3)

v_dif_alt = 1.5 * w * r0[2]


nframes = 1500
nframes2 = 3000
nframes3 = 3000
nframes4 = 9700

xs = []
ys = []
zs = []
ds = []
xdots = []

for i in range(nframes):
    t = i
    r_vec= cw.CW2(r0, rdot0, w, t)[0]
    rdot_vec = cw.CW2(r0, rdot0, w, t)[1]
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


V = 0.7875

r0 = [x, y, z]
deltav = [V , 0, 0]

for i in range(len(rdot)):
    rdot0[i] = rdot[i]+deltav[i]


for i in range(nframes2):
    t = i 
    r_vec= cw.CW2(r0, rdot0, w, t)[0]
    rdot_vec = cw.CW2(r0, rdot0, w, t)[1]
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
    
r0 = [x, y, z]
deltav = [0.7875, 0, 0]
for i in range(len(rdot)):
    rdot0[i] = rdot[i]+deltav[i]


for i in range(nframes3):
    t = i 
    r_vec= cw.CW2(r0, rdot0, w, t)[0]
    rdot_vec = cw.CW2(r0, rdot0, w, t)[1]
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


Vx = 0.3
xf = -100
t1 = (xf-x)/Vx


r0 = [x, y, z]
deltav = [0.3, 0, 0]
for i in range(len(rdot)):
    rdot0[i] = rdot[i]+deltav[i]


for i in range(nframes4):
    t = i  
    gam = [0, 0, 2*w*Vx] 
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




fig = plt.figure()
plt.plot(xs,zs,'r-')
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.ylabel("$R$-Bar ($m$)")
plt.xlabel("$V$-Bar ($m$)")
#plt.legend()
plt.grid(linestyle='-')
plt.title("Relative movement")