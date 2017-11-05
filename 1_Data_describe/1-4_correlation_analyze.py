#-*- coding: utf-8 -*-
from __future__ import print_function
import pandas as pd

catering_sale = 'pdata.xls' #餐饮数据，含有其他属性
data = pd.read_excel(catering_sale, index_col = 'num') #读取数据，指定num列为索引列

a=data.corr() #相关系数矩阵
b=data.corr()['price'] #只显示price相关系数
#c=data[u''].corr(data[u'']) #计算相关系数
print(a)
