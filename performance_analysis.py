#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 20:24:50 2021

@author: tuckerparon
"""

# Import Packages
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

##### LOAD DATA
df = pd.read_csv("data/StudentPerformance.csv")

##### PROCESS DATA
df['total_alc'] = ((df['Walc.x'] + df['Dalc.x'])/2)
df['failures'] = (df['failures.x'] + df['failures.y'])
df['absences'] = (df['absences.x'] + df['absences.y'])
df['health'] = (df['health.x'] + df['health.y'])
df['math_grade'] = (df['G3.x'])
df['port_grade'] = (df['G3.y'])
df['health'] = df['health.x']
df.rename(columns={'studytime.x': 'study_time', 'famrel.x':'fam_rel', 'activities.x':'activities', 'romantic.x':'romantic'}, inplace=True)

##### ANALYZE DATA

# What makes students more/less likely to drink?
### Gender, age, residency, parental status vs alcohol
fig, axs = plt.subplots(nrows=2, ncols=2)
plt.subplots_adjust(wspace=0.5, hspace=0.5)
fig.suptitle('FIG 3. Consumption by Background Characteristics')

y = df['total_alc']
x1 = df['sex']
x2 = df['age']
x3 = df['address']
x4 = df['Pstatus']

bp1 = sns.boxplot(x = x1, y = y, color='red', ax=axs[0][0])
bp2 = sns.boxplot(x = x2, y = y, color='lightgreen', ax=axs[0][1])
bp3 = sns.boxplot(x = x3, y = y, color='turquoise', ax=axs[1][0])
bp4 = sns.boxplot(x = x4, y = y, color='yellow', ax=axs[1][1])

bp1.set_ylabel("Alcohol Consumption (1-5)")
bp1.set_xlabel("Sex", fontsize = 10)
bp2.set_ylabel("Alc. Cons. (1-5)")
bp2.set_xlabel("Age", fontsize = 10)
bp3.set_ylabel("Alc. Cons. (1-5)")
bp3.set_xlabel("Residency", fontsize = 10)
bp4.set_ylabel("Alc. Cons. (1-5)")
bp4.set_xlabel("Parental Status", fontsize = 10)

# Does alcohol have a connection to a student's performance and general wellbeing?
### Alcohol vs failures, study time, absences, grades (math), grades (portuguese)
fig, axs = plt.subplots(nrows=2, ncols=2)
plt.subplots_adjust(wspace=0.5, hspace=0.5)
fig.suptitle('FIG 4a. Alcohol vs Performance')

x = df['total_alc']
y1 = df['failures']
y2 = df['study_time']
y3 = df['math_grade']
y4 = df['port_grade']

bp1 = sns.boxplot(x = x, y = y1, color='red', ax=axs[0][0])
bp2 = sns.boxplot(x = x, y = y2, color='lightgreen', ax=axs[0][1])
bp3 = sns.boxplot(x = x, y = y3, color='turquoise', ax=axs[1][0])
bp4 = sns.boxplot(x = x, y = y4, color='yellow', ax=axs[1][1])

bp1.set_xlabel("Alcohol Consumption (1-5)")
bp1.set_ylabel("Failures", fontsize = 10)
bp2.set_xlabel("Alcohol Consumption (1-5)")
bp2.set_ylabel("Study Time (hrs/week)", fontsize = 10)
bp3.set_xlabel("Alcohol Consumption (1-5)")
bp3.set_ylabel("Math Grade (0-20)", fontsize = 10)
bp4.set_xlabel("Alcohol Consumption (1-5)")
bp4.set_ylabel("Portuguese Grade (0-20)", fontsize = 10)

df_fig4a = df[['total_alc', 'failures', 'study_time', 'math_grade', 'port_grade']]
matrix_fig4a = df_fig4a.corr()
matrix_fig4a.style.background_gradient(cmap='coolwarm').set_precision(3)
matrix_fig4a

### Alcohol vs health, family relationship, extracuriculars and romantic relationship
fig, axs = plt.subplots(nrows=2, ncols=2)
plt.subplots_adjust(wspace=0.5, hspace=0.5)
fig.suptitle('FIG 4b. Alcohol vs Wellbeing')

x = df['total_alc']
y1 = df['health']
y2 = df['activities']
y3 = df['fam_rel']
y4 = df['romantic']

bp1 = sns.boxplot(x = x, y = y1, color='red', ax=axs[0][0])
bp2 = sns.boxplot(x = x, y = y2, color='lightgreen', ax=axs[0][1])
bp3 = sns.boxplot(x = x, y = y3, color='turquoise', ax=axs[1][0])
bp4 = sns.boxplot(x = x, y = y4, color='yellow', ax=axs[1][1])

bp1.set_xlabel("Alcohol Consumption (1-5)")
bp1.set_ylabel("Health (1-5)", fontsize = 10)
bp2.set_xlabel("Alcohol Consumption (1-5)")
bp2.set_ylabel("Extracuricular Activities", fontsize = 10)
bp3.set_xlabel("Alcohol Consumption (1-5)")
bp3.set_ylabel("Family Rel. Quality (1-5)", fontsize = 10)
bp4.set_xlabel("Alcohol Consumption (1-5)")
bp4.set_ylabel("Romantic Relationship", fontsize = 10)

df_a_yes = df[df['activities']=='yes']
df_a_no = df[df['activities']=='no']
df_fr_yes = df[df['fam_rel']=='yes']
df_fr_no = df[df['fam_rel']=='no']

ttest_ind(df_a_yes['total_alc'], df_a_no['total_alc'])
ttest_ind(df_fr_no['total_alc'], df_fr_yes['total_alc'])

df_fig4b = df[['total_alc', 'health', 'fam_rel']]
matrix_fig4b = df_fig4b.corr()
matrix_fig4b.style.background_gradient(cmap='coolwarm').set_precision(3)
matrix_fig4b



