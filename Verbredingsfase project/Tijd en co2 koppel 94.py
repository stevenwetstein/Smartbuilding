# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:03:32 2017

@author: steven
"""

#import modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#open csv
file = 'Ha_ho_de OS3 GRFMET 94 co2 aanzuig.csv'
data = pd.read_csv(file, sep = ';')

print(data.info)


#zet systeemtijd
data['Systeemtijd'] = pd.to_datetime(data['Systeemtijd'],format = '%H:%M:%S').dt.hour
print(data['Systeemtijd'])

#categoriseer systeemtijd
data1 = data.groupby([data['Systeemtijd']]).mean()
print(data1)

#categoriseer datum
data['Dag'] = sorted(data['Dag'])
data2 = data.groupby([data['Dag']]).mean()
print(data2)

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


#loop voor controle
som = 0
b=0
for a in range(len(data)):
    if data.iloc[a,0] ==4:
        som = som + data.iloc[a,1]
        b +=1
som = som /b
print(som)

#plot grafiek
plt.bar(data1.index, data1['Waarde'])
plt.ylim(450,600)
plt.xlabel('Time')
plt.ylabel('Avg co2')
plt.show()


#plot grafiek
plt.bar(maandag.index, maandag['Waarde'])
plt.title('Maandag')
plt.ylim(475,600)
plt.xlabel('Time')
plt.ylabel('Avg co2')
plt.show()

plt.bar(dinsdag.index, dinsdag['Waarde'])
plt.title('Dinsdag')
plt.ylim(475,600)
plt.xlabel('Time')
plt.ylabel('Avg co2')
plt.show()

plt.bar(woensdag.index, woensdag['Waarde'])
plt.title('Woensdag')
plt.ylim(475,600)
plt.xlabel('Time')
plt.ylabel('Avg co2')
plt.show()

plt.bar(donderdag.index, donderdag['Waarde'])
plt.title('Donderdag')
plt.ylim(475,600)
plt.xlabel('Time')
plt.ylabel('Avg co2')
plt.show()

plt.bar(vrijdag.index, vrijdag['Waarde'])
plt.title('Vrijdag')
plt.ylim(475,600)
plt.xlabel('Time')
plt.ylabel('Avg co2')
plt.show()

plt.bar(zaterdag.index, zaterdag['Waarde'])
plt.title('Zaterdag')
plt.ylim(475,600)
plt.xlabel('Time')
plt.ylabel('Avg co2')
plt.show()

plt.bar(zondag.index, zondag['Waarde'])
plt.title('Zondag')
plt.ylim(475,600)
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
plt.grid(True)
plt.ylabel('Avg CO2 (ppm)')
plt.legend(bbox_to_anchor=(1.01, 1))
plt.figure(figsize=(20,10))
plt.show()


data['Datum'] = pd.to_datetime(data['Datum'],format = '%d-%m-%Y')
heatmapdata1 = data.iloc[:,0:3]
heatmapdata = heatmapdata1.pivot_table(heatmapdata1, columns = ['Datum'], index = ['Systeemtijd'], aggfunc = np.mean)
print(heatmapdata.sort_index())
heatmapplot = sns.heatmap(heatmapdata, cmap = 'PuBuGn')
plt.figure(1)
plt.savefig('heatmap.png')
plt.show()
#carpetplot
data['Datum'] = pd.to_datetime(data['Datum'],format = '%d-%m-%y')
pd.to_numeric(heatmapdata1['Datum'])
heatmapdata1 = data.iloc[:,0:3]
heatmapdata1 = heatmapdata1['Datum']
heatmapdata = heatmapdata1.pivot_table(heatmapdata1, index = ['Datum'], columns = ['Systeemtijd'], aggfunc = np.mean)

print(float(data1["Datum"][0]))
print(len(data['Datum'][0]))
print(data['Datum'][0])
for i in data['Datum']:
    if len(i) < 8:
        print(i)