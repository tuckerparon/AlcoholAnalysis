#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 15:29:16 2021

@author: tuckerparon
"""

# Import Packages
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

##### LOAD DATA
df = pd.read_csv("data/HappinessAlcoholConsumption.csv") # happiness and alcohol consumption by country

##### PROCESS DATA
df['TotalDrinks_PerCapita'] = ( df['Beer_PerCapita'] + df['Spirit_PerCapita'] + df['Wine_PerCapita']) # total drinks per capita

##### ANALYZE DATA

### Happiness and Consumption by Region
df_reg = df.groupby('Region', as_index=False)[['TotalDrinks_PerCapita', 'HappinessScore']].mean()
df_reg = df_reg.filter(items=['Region', 'TotalDrinks_PerCapita', 'HappinessScore'])

fig, axs = plt.subplots(nrows=1, ncols=2)
plt.subplots_adjust(wspace=0.5, hspace=0.5)
fig.suptitle('FIG 1. Happiness and Consumption by Region')

x = df_reg['Region']
y1 = df_reg['TotalDrinks_PerCapita']
y2 = df_reg['HappinessScore']


bp1 = sns.barplot(x = x, y = y1, color='brown', ax=axs[0], order=df_reg.sort_values('TotalDrinks_PerCapita').Region)
bp2 = sns.barplot(x = x, y = y2, color='yellow', ax=axs[1], order=df_reg.sort_values('TotalDrinks_PerCapita').Region)

bp1.set_ylabel("Drinks per capita", fontsize = 10)
bp2.set_ylabel("Happiness Score", fontsize = 10)
bp1.set_xticklabels(bp1.get_xticklabels(), rotation = 90)
bp2.set_xticklabels(bp2.get_xticklabels(), rotation = 90)

# Does happiness have a connection to alcohol consumption? With certain types?
### Happiness Score by Drinks
fig, axs = plt.subplots(nrows=2, ncols=2)
plt.subplots_adjust(wspace=0.5, hspace=0.5)
fig.suptitle('FIG 2. Drinks per Capita vs Average Happiness Score')

x = df['HappinessScore']
y1 = df['TotalDrinks_PerCapita']
y2 = df['Beer_PerCapita']
y3 = df['Spirit_PerCapita']
y4 = df['Wine_PerCapita']

s1 = sns.regplot(x = x, y = y1, color='green', ax=axs[0][0], scatter_kws={'s':4})
s2 = sns.regplot(x = x, y = y2, color='brown', ax=axs[0][1], scatter_kws={'s':4})
s3 = sns.regplot(x = x, y = y3, color='blue', ax=axs[1][0], scatter_kws={'s':4})
s4 = sns.regplot(x = x, y = y4, color='red', ax=axs[1][1], scatter_kws={'s':4})

s1.set_ylabel("All", fontsize = 10)
s1.set_xlabel("Happiness Score", fontsize = 10)
s2.set_ylabel("Beer", fontsize = 10)
s2.set_xlabel("Happiness Score", fontsize = 10)
s3.set_ylabel("Spirits", fontsize = 10)
s3.set_xlabel("Happiness Score", fontsize = 10)
s4.set_ylabel("Wine", fontsize = 10)
s4.set_xlabel("Happiness Score", fontsize = 10)

s1_cor = x.corr(y1) # r = 0.5475
s2_cor = x.corr(y2) # r = 0.4934
s3_cor = x.corr(y3) # r = 0.2564
s4_cor= x.corr(y4) # r = 0.4506

df_fig2 = df.drop(['Country', 'Region', 'Hemisphere', 'HDI'], 1)
matrix_fig2 = df_fig2.corr()
matrix_fig2.style.background_gradient(cmap='coolwarm').set_precision(3)
matrix_fig2


# Is happiness correlated with HDI & GDP?
### Happiness by HDI & GDP
fig, axs = plt.subplots(nrows=1, ncols=2)
plt.subplots_adjust(wspace=0.5, hspace=0.5)
fig.suptitle('Happiness Score vs Other Variables')

x = df['HappinessScore']
y1 = df['HDI']
y2 = df['GDP_PerCapita']

sp1 = sns.regplot(x = x, y = y1, color='green', ax=axs[0],  scatter_kws={'s':4})
sp2 = sns.regplot(x = x, y = y2, color='red', ax=axs[1],  scatter_kws={'s':4})

sp1.set_ylabel("HDI", fontsize = 10)
sp1.set_xlabel("Happiness", fontsize = 10)
sp2.set_ylabel("GDP_PerCapita", fontsize = 10)
sp2.set_xlabel("Happiness", fontsize = 10)

############################# NOT USED IN REPORT #############################

hs_hdi = x.corr(y1)
hs_gdp = x.corr(y2)

# Does happiness have a connection to alcohol consumption? With certain types?

### Human Development Index by Drinks
x = df['HDI']
fig, axs = plt.subplots(nrows=2, ncols=2)
plt.subplots_adjust(wspace=0.5, hspace=0.5)
fig.suptitle('Drinks per capita vs Human Development Index')

y = df['TotalDrinks_PerCapita'] # ***
t = sns.regplot(x = x, y = y, color='green', ax=axs[0][0],  scatter_kws={'s':4})
hdi_t = x.corr(y) # r = 0.7157
t.set_ylabel("All", fontsize = 10)
t.set_xlabel("HDI", fontsize = 10)

y = df['Beer_PerCapita']
b = sns.regplot(x = x, y = y, color='brown', ax=axs[0][1], scatter_kws={'s':4})
hdi_b = x.corr(y) # r = 0.5884
b.set_ylabel("Beer", fontsize = 10)
b.set_xlabel("HDI", fontsize = 10)

y = df['Spirit_PerCapita']
s = sns.regplot(x = x, y = y, color='blue', ax=axs[1][0], scatter_kws={'s':4})
hdi_s = x.corr(y) # r = 0.3934
s.set_ylabel("Spirits", fontsize = 10)
s.set_xlabel("HDI", fontsize = 10)

y = df['Wine_PerCapita'] # ***
w = sns.regplot(x = x, y = y, color='red', ax=axs[1][1], scatter_kws={'s':4})
hdi_w = x.corr(y) # r = 0.6026
w.set_ylabel("Wine", fontsize = 10)
w.set_xlabel("HDI", fontsize = 10)

hdi_df = df.drop('HDI', 1)
hdi_corr = hdi_df.corr()

 
# Do certain hemispheres drink more?

### Hemisphere by Drinks
df['Hemisphere']= df['Hemisphere'].replace(['noth'], ['north'])
df_hemi = df.groupby('Hemisphere', as_index=False)[['TotalDrinks_PerCapita']].mean()
df_hemi.plot(kind = 'bar', x = 'Hemisphere', y = 'TotalDrinks_PerCapita') 

north = df[df['Hemisphere']=='north']
south = df[df['Hemisphere']=='south']
t_val,p_val=ttest_ind(north['TotalDrinks_PerCapita'], south['TotalDrinks_PerCapita']) # t = 1.3217, p = 0.1889 
