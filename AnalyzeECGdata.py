# -*- coding: utf-8 -*-
"""
Created on Fri May  1 01:15:18 2015

@author: avimehta
"""

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import sympy as sym
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def func(x, a, b, c):
    return a * np.exp(-x/b) + c

x = np.linspace(0,15.0,251)
datafile = open("Workbook.csv")
df = pd.read_csv(datafile)
DataC = df.Data
print(DataC)


popt, pcov = curve_fit(func, x, DataC)
print ("a = %s , b = %s, c = %s" % (popt[0], popt[1], popt[2]))



plt.figure()
plt.xlabel('Time (microseconds)')
plt.ylabel('Voltage(V)')
plt.plot(x, DataC, 'ko', label="Original  Data")
plt.plot(x, func(x, *popt), 'r-', label="Fitted Curve")
plt.legend()
plt.show()
