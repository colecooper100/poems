# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:13:30 2019

@author: labuser
"""

import trackpy as tp
import pims
import matplotlib.pyplot as plt




images = pims.open(r'C:\Users\labuser\Documents\SEQconvert/*.png')  # many PNGs with sequential names

for i in range(50):
    plt.imshow(images[i])
    plt.pause(0.1)

f = tp.locate(images[0], 11)

for i in range(30):
    g = tp.locate(images[i], 11,minmass = 20)
    tp.annotate(g, images[i])
    plt.pause(0.1)

h = tp.batch(images[:],11)

h.head()
plt.figure()
tp.plot_traj(h)


















































