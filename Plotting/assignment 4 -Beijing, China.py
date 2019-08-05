# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:28:42 2019

@author: azhang
"""

# Beijing, China
# Economic condition and life quality

# How have the quality of people's life and economic condition changed in Beijing over the last 15 years? 
# Does economic condition have a great impact on the quality of life?

# Source :http://data.stats.gov.cn/english/easyquery.htm?cn=E0103
# Source2 : http://www.stats.gov.cn/english/

import pandas as pd
import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt
import seaborn as sns

# pd.read_excel?
#('Beijing_Gross Regional Product.xls') 

gdp = pd.read_excel('Beijing_Gross Regional Product.xls',skiprows = 3)
gdp.set_
print(gdp.columns.tolist())
