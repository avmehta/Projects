# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 09:29:45 2015

@author: avimehta
"""

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.mlab as mlab
import matplotlib.patches as mpatches
import pylab
from pylab import *


data = pd.read_csv("Workbook3.csv")
xdata = np.linspace(0,24,25)
dataclicks = pd.read_csv("clicks.csv")
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
tuesday1 = list(data.Tuesday)
monday1 = list(data.Monday)
monday2 = list(data.MondayM)
tuesday2 = list(data.TuesdayT)
wednesday = list(data.Wednesday)
thursday = list(data.Thursday)
saturday = list(data.Saturday)
sunday = list(data.Sunday)
clickday = list(dataclicks.open_time)
clickhour = list(dataclicks.open)
friday = list(data.Friday)

plt.figure(1)
plt.suptitle('Frequency of Clicks', fontsize=20)
plt.xlabel('Day(Month of March, Year 2014)', fontsize=18)
plt.ylabel('Frequency', fontsize=16)
#plt.hist(saturday, xdata, color = 'red')

eventsat, edges, patches = hist(saturday, xdata, color = 'r')
eventsun, edges, patches = hist(sunday, xdata, color = 'b')
eventsmon, edges, patches = hist(monday2, xdata, color = 'g')
eventswed, edges, patches = hist(wednesday, xdata, color = 'k')
eventsthurs, edges, patches = hist(thursday, xdata, color = 'm')
eventstues, edges, patches = hist(tuesday2, xdata, color = 'y')
eventsfri, edges, patches = hist(friday, xdata, color = 'c')

plt.show()
plt.figure(2)
plt.plot(x, eventsat, color = 'r')
plt.plot(x, eventsun, color = 'b')
plt.plot(x, eventsmon, color = 'g')
plt.plot(x, eventswed, color = 'k')
plt.plot(x, eventstues, color = 'y')
plt.plot(x, eventsthurs, color = 'm')
plt.plot(x, eventsfri, color = 'c')
red_patch = mpatches.Patch(color='r', label='Saturday')
blue_patch = mpatches.Patch(color='b', label='Sunday')
green_patch = mpatches.Patch(color='g', label='Monday')
black_patch = mpatches.Patch(color='k', label='Wednesday')
magenta_patch = mpatches.Patch(color='m', label='Thursday')
yellow_patch = mpatches.Patch(color='y', label='Tuesday')
cyan_patch = mpatches.Patch(color = 'c', label = 'Friday')
plt.legend([red_patch, blue_patch, green_patch, black_patch, magenta_patch, yellow_patch, cyan_patch], ['Saturday', 'Sunday', 'Monday', 'Wednesday', 'Thursday', 'Tuesday', 'Friday'], loc = 0)






#plt.hist([saturday,sunday],xdata, color = ['red','blue'])
#red_patch = mpatches.Patch(color='red', label='Saturday')
#blue_patch = mpatches.Patch(color='blue', label='Sunday')
#plt.legend([red_patch, blue_patch], ['Saturday', 'Sunday'], loc = 0) 
pylab.xlim([0,24])
pylab.ylim([0,2000])









