
# coding: utf-8

# # Assignment 2
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# An NOAA dataset has been stored in the file `data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv`. The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) [Daily Global Historical Climatology Network](https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
# 
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Ann Arbor, Michigan, United States**, and the stations the data comes from are shown on the map below.

# In[15]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))
    
    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')


# In[4]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import numpy as np
get_ipython().magic('matplotlib notebook')

# clean the dataframe
df = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
df.sort_values(by='Date', inplace = True)
df = df[(pd.DatetimeIndex(df['Date']).month !=2) & (pd.DatetimeIndex(df['Date']).day !=29)]
df['Year'] = pd.DatetimeIndex(df['Date']).year
df['Month_Date'] = df['Date'].apply(lambda x: x[5:])
df['Data_Value'] = df['Data_Value'] / 10

#get the max and min on each day in the range of 2005 - 2014
dmax = df[(df['Element']=='TMAX') & (df['Year'] != 2015)]
dmin = df[(df['Element']=='TMIN') & (df['Year'] != 2015)]
dmax = dmax.groupby('Month_Date').agg({'Data_Value':max})
dmin = dmin.groupby('Month_Date').agg({'Data_Value':min})

#get the max and min in 2015
max_2015 = df[(df['Element']=='TMAX') & (df['Year'] == 2015)]
min_2015 = df[(df['Element']=='TMIN') & (df['Year'] == 2015)]
max_2015_1 = max_2015.groupby('Month_Date').agg({'Data_Value':max})
min_2015_1 = min_2015.groupby('Month_Date').agg({'Data_Value':min})

#make the month&day a column in each dataframe
dmax.reset_index(inplace = True)
dmin.reset_index(inplace = True)
max_2015_1.reset_index(inplace = True)
min_2015_1.reset_index(inplace = True)

#get the broken max an min in 2015
bmax = (max_2015_1[max_2015_1['Data_Value'] > dmax['Data_Value']]).index.tolist()
bmin = (min_2015_1[min_2015_1['Data_Value'] < dmin['Data_Value']]).index.tolist()

#plot the required 
plt.figure(figsize = (15, 10))
plt.plot(dmax['Data_Value'], 'grey', alpha =0.4, label = 'Record High')
plt.plot(dmin['Data_Value'], 'grey', alpha =0.4, label = 'Record Low')
plt.gca().fill_between(range(len(dmin)), dmin['Data_Value'], dmax['Data_Value'], facecolor ='grey', alpha = 0.15)
plt.scatter(bmax, max_2015_1['Data_Value'].iloc[bmax], s = 10,  c = 'blue', alpha = 0.5, label = 'Broken Max in 2015')
plt.scatter(bmin, min_2015_1['Data_Value'].iloc[bmin], s = 10,  c = 'black',  label = 'Broken Min in 2015')

#label the title, axes, and legend
plt.title('Temperature 2005-2014 and extreme 2015 in Ann Arbor, Michigan')
plt.xlabel('Month')
plt.ylabel('Temperature degree C')
plt.legend(loc = 4, frameon = False)

#hide the lines on top and right
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

#relabel the x-axis to make it more clear to audiences
labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul','Aug','Sep','Oct','Nov','Dec']
ticks = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
plt.xticks(ticks, labels)



# In[ ]:




# In[ ]:



