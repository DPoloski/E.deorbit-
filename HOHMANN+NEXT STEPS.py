# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:32:48 2019

@author: POLO
"""


from astropy import units as u
import numpy as np
import math
import matplotlib.pyplot as plt

r0=[-13000,0,3000]      #initial starting position
rdot0=[4.704931942091908,0,0]          #initial velocity  (m/s)
R= 7144e3                  #semimayor axis (m)
mu = 3.9857128e14           #SI
w =math.sqrt(mu/R**3)

v_dif_alt = 1.5 * w * r0[2]



nframes = 1500
nframes2 = 100
nframes3 = 60

def CW(r0, rdot0, w, t):
    x0 = r0[0]
    y0 = r0[1]
    z0 = r0[2]
    xdot0 = rdot0[0]
    ydot0 = rdot0[1]
    zdot0 = rdot0[2]
    
    xt = ((4*xdot0)/w-6*z0)*math.sin(w*t)-((2*zdot0)/w)*math.cos(w*t)+(6*w*z0-3*xdot0)*t+(x0+(2*zdot0)/w)
    yt = y0*math.cos(w*t)+(ydot0/w)*math.sin(w*t)
    zt = ((2*xdot0)/w-3*z0)*math.cos(w*t)+((zdot0)/w)*math.sin(w*t)+(4*z0-(2*xdot0)/w)
    
    xdott = ((4*xdot0)/w-6*z0)*w*math.cos(w*t)+(2*zdot0)*math.sin(w*t)+(6*w*z0-3*xdot0)
    ydott = -y0*w*math.sin(w*t)+ydot0*math.cos(w*t)
    zdott = -((2*xdot0)/w-3*z0)*w*math.sin(w*t)+zdot0*math.cos(w*t)
    
    return([xt,yt,zt],[xdott,ydott,zdott])
    
xs = []
ys = []
zs = []
ds = []

def CW2(r0, rdot0, w, t):
    x0 = r0[0]
    y0 = r0[1]
    z0 = r0[2]
    xdot0 = rdot0[0]
    ydot0 = rdot0[1]
    zdot0 = rdot0[2]
    gamx = 0
    gamy = 0
    gamz = 0   #2*w*xdot0
    
    xt = ((4*xdot0)/w-6*z0)*math.sin(w*t)-((2*zdot0)/w)*math.cos(w*t)+(6*w*z0-3*xdot0)*t+(x0+(2*zdot0)/w)+((4/w**2)*(1-math.cos(w*t))-3*0.5*t**2)*gamx+((2/w**2)*(w*t-math.sin(w*t)))*gamz
    yt = y0*math.cos(w*t)+(ydot0/w)*math.sin(w*t)+((1/w**2)*(1-math.cos(w*t)))*gamy
    zt = ((2*xdot0)/w-3*z0)*math.cos(w*t)+((zdot0)/w)*math.sin(w*t)+(4*z0-(2*xdot0)/w)+((2/w**2)*(math.sin(w*t)-w*t))*gamx+((1/w**2)*(1-math.cos(w*t)))*gamz
    
    xdott = ((4*xdot0)/w-6*z0)*w*math.cos(w*t)+(2*zdot0)*math.sin(w*t)+(6*w*z0-3*xdot0)+((4/w)*(math.sin(w*t))-3*t)*gamx+((2/w)*(1-math.cos(w*t)))*gamz
    ydott = -y0*w*math.sin(w*t)+ydot0*math.cos(w*t)+((1/w)*(math.sin(w*t)))*gamy
    zdott = -((2*xdot0)/w-3*z0)*w*math.sin(w*t)+zdot0*math.cos(w*t)+((2/w)*(math.cos(w*t))-1)*gamx+((1/w)*(math.sin(w*t)))*gamz
    
    return([xt,yt,zt],[xdott,ydott,zdott])


for i in range(nframes):
    t = i
    r_vec= CW2(r0, rdot0, w, t)[0]
    rdot_vec = CW2(r0, rdot0, w, t)[1]
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
    
    v = math.sqrt(xdot**2+ydot**2+zdot**2)

#TRIGONOMETRÍA PARA RELACIONAR EJES DEL TARGET CON LOS DEL CHASER 
x1 = abs(x)
alph = (180/math.pi)* math.asin(x1/d)
r_t1 = x1/ math.tan((math.pi/180)*alph)
phase_angle = (180/math.pi) * math.atan(x1/(R - r_t1))
beta = 90 - alph
epsilon = 180 - beta - alph - phase_angle
#rho es el angulo entre los ejes x de Target-chaser
rho = 90 - epsilon
r_c = x1/ math.sin((math.pi/180) * phase_angle)

V = 0.78

r0 = [x, y, z]
deltav = [V * math.cos(rho*(math.pi/180)), 0, - V * math.sin(rho*(math.pi/180))]

for i in range(len(rdot)):
    rdot0[i] = rdot[i]+deltav[i]


for i in range(nframes2):
    t = i + nframes2 + nframes
    r_vec= CW2(r0, rdot0, w, t)[0]
    rdot_vec = CW2(r0, rdot0, w, t)[1]
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
    
    v = math.sqrt(xdot**2+ydot**2+zdot**2)
    

"""  
    
    
r0 = [x, y, z]
deltav = [0.01, 0, 0]
for i in range(len(rdot)):
    rdot0[i] = rdot[i]+deltav[i]


for i in range(nframes3):
    t = i + nframes2 + nframes
    r_vec= CW2(r0, rdot0, w, t)[0]
    rdot_vec = CW2(r0, rdot0, w, t)[1]
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
    
    v = math.sqrt(xdot**2+ydot**2+zdot**2)


"""

fig = plt.figure()
plt.plot(xs,zs,'r-')
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.ylabel("$R$-Bar ($m$)")
plt.xlabel("$V$-Bar ($m$)")
#plt.legend()
plt.grid(linestyle='-')
plt.title("Relative movement")