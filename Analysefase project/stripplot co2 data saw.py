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

sns.stripplot(jitter=True, size = 5, data=data.iloc[:,15:20])
plt.title('CO2 Values', fontsize = 14, fontweight = 'bold')
plt.style.use('ggplot')
plt.xlabel('Lokaal')
plt.grid(True)
plt.ylabel('CO2 (ppm)')

plt.figure(figsize=(20,10))
plt.show()
