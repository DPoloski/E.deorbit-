# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:17:44 2019

@author: POLO
"""
from astropy import units as u
import numpy as np
import math
import matplotlib.pyplot as plt

def CW(r0, rdot0, w, t, gam):
    x0 = r0[0]
    y0 = r0[1]
    z0 = r0[2]
    xdot0 = rdot0[0]
    ydot0 = rdot0[1]
    zdot0 = rdot0[2]
        
    gamx = gam[0] 
    gamy = gam[1]  
    gamz = gam[2]  
    
    xt = ((4*xdot0)/w-6*z0)*math.sin(w*t)-((2*zdot0)/w)*math.cos(w*t)+(6*w*z0-3*xdot0)*t+(x0+(2*zdot0)/w)+((4/w**2)*(1-math.cos(w*t))-3*0.5*t**2)*gamx+((2/w**2)*(w*t-math.sin(w*t)))*gamz
    yt = y0*math.cos(w*t)+(ydot0/w)*math.sin(w*t)+((1/w**2)*(1-math.cos(w*t)))*gamy
    zt = ((2*xdot0)/w-3*z0)*math.cos(w*t)+((zdot0)/w)*math.sin(w*t)+(4*z0-(2*xdot0)/w)+((2/w**2)*(math.sin(w*t)-w*t))*gamx+((1/w**2)*(1-math.cos(w*t)))*gamz
    
    xdott = ((4*xdot0)/w-6*z0)*w*math.cos(w*t)+(2*zdot0)*math.sin(w*t)+(6*w*z0-3*xdot0)+((4/w)*(math.sin(w*t))-3*t)*gamx+((2/w)*(1-math.cos(w*t)))*gamz
    ydott = -y0*w*math.sin(w*t)+ydot0*math.cos(w*t)+((1/w)*(math.sin(w*t)))*gamy
    zdott = -((2*xdot0)/w-3*z0)*w*math.sin(w*t)+zdot0*math.cos(w*t)+((2/w)*(math.cos(w*t))-1)*gamx+((1/w)*(math.sin(w*t)))*gamz
    
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