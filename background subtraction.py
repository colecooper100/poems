# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:02:14 2019

@author: labuser
"""

import pims
import pimsviewer
#from pimsviewer import Viewer
import numpy as np
import PIL

video = pims.open(r'C:\Users\labuser\Documents\SEQconvert/12-56-49.000.seq')

v = np.array(video[:100], dtype='f') #[1000, 1080, 1920]

v -= v.mean(0) #[1080, 1920]




for i, frame in enumerate(v[:100]):
    img = PIL.Image.fromarray(np.clip(frame, 0, 255).astype('u1')).save('frame%08d.png' % i)






































