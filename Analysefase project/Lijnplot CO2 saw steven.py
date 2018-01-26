# -*- coding: utf-8 -*

"""
Created on Mon Nov 06 11:12 2017

@author: Steven
"""

# imported required libraries and defining functions for reading data,
# mean normalizing features and estimating gaussian distribution.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pylab import rcParams
import seaborn as sns


rcParams['figure.figsize'] = 5, 4

file = 'SAW data omgekeerd goed.csv'
data = pd.read_csv(file, sep = ';', parse_dates= True, index_col = 0, dayfirst = True)

plt.style.use('ggplot')
plt.plot(data.iloc[0:,2])
plt.title('Value CO2')
plt.xlabel('Month')
plt.ylabel('CO2 Value')
plt.ylim(0, 900)
plt.show()

