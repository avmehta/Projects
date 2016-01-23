# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 17:29:36 2015

@author: avimehta
"""

import random
import numpy as np
total = 0
runs = 1000000
trials = []
for i in range(runs):
    seq = random.sample(range(1,9),8)
    temp = []
    count = 0
    for x in range(8):
        if any(y in temp for y in (seq[x]+1, seq[x]-1)):
            temp.append(seq[x])
        else:
            temp.append(seq[x])
            count = count + 1
    total = count + total
    trials.append(count)
avg = np.mean(trials)
std = np.std(trials, dtype=np.float64)
print("%.10f" % (avg))
print("%.10f" % (std))


        
    
    
    