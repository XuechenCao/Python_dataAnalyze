#-*- coding: utf-8 -*-
from __future__ import print_function
import pandas as pd

catering_sale = 'pdata.xls' #
data = pd.read_excel(catering_sale, index_col = u'num') #
#data = data[(data[u'gps_w'] > 400)&(data[u'gps_j'] < 5000)] #
statistics = data.describe() #

statistics.loc['range'] = statistics.loc['max']-statistics.loc['min'] #极差
statistics.loc['var'] = statistics.loc['std']/statistics.loc['mean'] #变异系数
statistics.loc['dis'] = statistics.loc['75%']-statistics.loc['25%'] #
print(statistics)