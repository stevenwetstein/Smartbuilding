# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:54:35 2017

@author: steven
"""

#import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.mlab as mlab
import seaborn as sns

#open csv
file = 'Ha_ho_de OS2 GRFMET 87 co2 aanzuig.csv'
data = pd.read_csv(file, sep = ';')

#zet systeemtijd 
data['Systeemtijd'] = pd.to_datetime(data['Systeemtijd'],format = '%H:%M:%S').dt.hour
print(data['Systeemtijd'])

#categoriseer systeemtijd
data1 = data.groupby([data['Systeemtijd']]).mean()
print(data1)

# =============================================================================
# #categoriseer datum
# data['Dag'] = sorted(data['Dag'])
# data2 = data.groupby([data['Dag']]).mean()
# print(data2)
# =============================================================================

#opslaan maandag
maandag = data[data['Dag'] == 'maandag']
maandag = maandag.groupby([data['Systeemtijd']]).mean()
print(maandag)

#opslaan dinsdag
dinsdag = data[data['Dag'] == 'dinsdag']
dinsdag = dinsdag.groupby([data['Systeemtijd']]).mean()
print(dinsdag)

#opslaan woensdag
woensdag = data[data['Dag'] == 'woensdag']
woensdag = woensdag.groupby([data['Systeemtijd']]).mean()
print(woensdag)

#opslaan donderdag
donderdag = data[data['Dag'] == 'donderdag']
donderdag = donderdag.groupby([data['Systeemtijd']]).mean()
print(donderdag)

#opslaan vrijdag
vrijdag = data[data['Dag'] == 'vrijdag']
vrijdag = vrijdag.groupby([data['Systeemtijd']]).mean()
print(vrijdag)

#opslaan zaterdag
zaterdag = data[data['Dag'] == 'zaterdag']
zaterdag = zaterdag.groupby([data['Systeemtijd']]).mean()
print(zaterdag)

#opslaan zondag
zondag = data[data['Dag'] == 'zondag']
zondag = zondag.groupby([data['Systeemtijd']]).mean()
print(zondag)

# =============================================================================
# #Loop voor controle
# gerard = []
# nul=0
# b1=0
# henk = 0 
# b2 = 0
# 
# for i in range(len(data)):
#     if data.iloc[i,0] == 0:
#         nul = nul + data.iloc[i,1]
#         b1 +=1
#     elif data.iloc[i,0] == 23:
#         henk = henk + data.iloc[i,1]
#         b2 +=1
#     elif data.iloc[i-1,0] == 0:
#         nul=nul/b1
#         henk = henk/b2
#         gerard.append([nul, henk])
#         b1=0
#         b2=0
#         print(np.mean(nul))
#         nul=0
#         henk=0
# print(gerard)
# 
# =============================================================================
#loop voor controle
# =============================================================================
# som = 0
# b=0
# for a in range(len(data)):
#     if data.iloc[a,0] ==0:
#         som = som + data.iloc[a,1]
#         b +=1
# som = som /b
# print(som)
# 
# =============================================================================
#plot grafiek
plt.bar(maandag.index, maandag['Waarde'])
plt.title('Maandag')
plt.ylim(475,550)
plt.xlabel('Time')
plt.ylabel('Avg co2')
plt.show()

plt.bar(dinsdag.index, dinsdag['Waarde'])
plt.title('Dinsdag')
plt.ylim(475,550)
plt.xlabel('Time')
plt.ylabel('Avg co2')
plt.show()

plt.bar(woensdag.index, woensdag['Waarde'])
plt.title('Woensdag')
plt.ylim(475,550)
plt.xlabel('Time')
plt.ylabel('Avg co2')
plt.show()

plt.bar(donderdag.index, donderdag['Waarde'])
plt.title('Donderdag')
plt.ylim(475,550)
plt.xlabel('Time')
plt.ylabel('Avg co2')
plt.show()

plt.bar(vrijdag.index, vrijdag['Waarde'])
plt.title('Vrijdag')
plt.ylim(475,550)
plt.xlabel('Time')
plt.ylabel('Avg co2')
plt.show()

plt.bar(zaterdag.index, zaterdag['Waarde'])
plt.title('Zaterdag')
plt.ylim(475,550)
plt.xlabel('Time')
plt.ylabel('Avg co2')
plt.show()

plt.bar(zondag.index, zondag['Waarde'])
plt.title('Zondag')
plt.ylim(475,550)
plt.xlabel('Time')
plt.ylabel('Avg co2')
plt.show()

         
pltma = plt.plot(maandag.index, maandag['Waarde'], label = 'Maandag')
pltdi = plt.plot(dinsdag.index, dinsdag['Waarde'], label = 'Dinsdag')
pltwo = plt.plot(woensdag.index, woensdag['Waarde'], label = 'Woensdag')
pltdo = plt.plot(donderdag.index, donderdag['Waarde'], label = 'Donderdag')
pltvr = plt.plot(vrijdag.index, vrijdag['Waarde'], label = 'Vrijdag')
pltza = plt.plot(zaterdag.index, zaterdag['Waarde'], label = 'Zaterdag')
pltzo = plt.plot(zondag.index, zondag['Waarde'], label = 'Zondag')
pltavg = plt.plot(data1.index, data1['Waarde'], label = 'Gemiddeld', linestyle = '--', color = 'k', linewidth = 2.5)
plt.title('CO2 Values', fontsize = 14, fontweight = 'bold')
plt.style.use('ggplot')
plt.xlabel('Time (hour)')
plt.ylim(490, 565)
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
xi = [i for i in range(0, len(x))]
plt.xticks(xi,x)
plt.grid(True)
plt.ylabel('Avg CO2 (ppm)')
plt.legend(bbox_to_anchor=(1.01, 1))
plt.figure(figsize=(40,20))
plt.show()


#carpetplot
data['Datum'] = pd.to_datetime(data['Datum'],format = '%d-%m-%Y')
heatmapdata1 = data.iloc[:,0:3]
heatmapdata = heatmapdata1.pivot_table(heatmapdata1, columns = ['Datum'], index = ['Systeemtijd'], aggfunc = np.mean)
print(heatmapdata.sort_index())
heatmapplot = sns.heatmap(heatmapdata, cmap = 'PuBuGn', square = True)
plt.figure(1)
plt.yticks(6)
plt.savefig('heatmap.png')
plt.show()


