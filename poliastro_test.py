# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:15:48 2019

@author: daniel.polo
"""


from astropy import units as u

from poliastro.bodies import Earth, Mars, Sun
from poliastro.twobody import Orbit



# Data from Curtis, example 4.3
r = [-6045, -3490, 2500] * u.km
v = [-3.457, 6.618, 2.533] * u.km / u.s

ss = Orbit.from_vectors(Earth, r, v)
ss.epoch
s
ss.plot()