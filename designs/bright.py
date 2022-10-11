# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:36:44 2022

@author: MEGHA
"""


import random
import colorsys

def bright_color_gen():
    h,s,l = random.random(), 0.5 + random.random()/2.0, 0.4 + random.random()/5.0
    rgb = [int(256*i) for i in colorsys.hls_to_rgb(h,l,s)]
    
    return rgb
    