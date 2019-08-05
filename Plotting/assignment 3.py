# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:18:16 2019

@author: azhang
"""

# Use the following data for this assignment:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlp
from matplotlib.cm import get_cmap
from matplotlib import cm


np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])
df = df.T
df.describe()
mean = (df.mean())
std = ((df.std())/np.sqrt(df.count()))
ci = [i * 1.96 for i in std]

blues = cm.Blues
reds = cm.Reds
norm = mlp.colors.Normalize(vmin=-1.96, vmax=1.96)

def boxplot(y):
    
    colors = pd.DataFrame()
    colors['index'] = [i-y for i in mean]/std
    colors['color'] = colors['index'].apply(lambda x: reds(abs(x/10)) if x>0 else blues(abs(x/10)))
    fig = plt.figure(figsize=(10,8))
    line = plt.axhline(y, color='grey',linewidth=2, label = 'Y')
    boxplot = plt.bar(df.columns, mean, yerr=ci, color = colors['color'], capsize = 10)
    
    plt.xticks(df.columns)
    plt.title('Data in 1992-1995')
    plt.ylabel('Mean')
    plt.xlabel('Year')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    return boxplot,line

def onclick(boxplot, line,event='button_press_event'):
    for i in range(4):
        index = (norm((mean[i]-event.ydata)/df.std()[i]))
        color = reds(abs(index/10)) if index > 0 else blues(abs(index/10))
        boxplot[i].set_color(color) 
    line.set_ydata(event.ydata)

boxplot,line = boxplot(42000)
plt.gcf().canvas.mpl_connect('button_press_event', onclick(boxplot,line))
