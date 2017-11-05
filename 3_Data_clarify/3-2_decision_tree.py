#-*- coding: utf-8 -*-

import pandas as pd

inputfile = 'sales_data.xls'
data = pd.read_excel(inputfile, index_col = u'num') #导入数据

#数据是类别标签，要将它转换为数据
data[data == u'good'] = 1
data[data == u'yes'] = 1
data[data == u'high'] = 1
data[data != 1] = -1
x = data.iloc[:,:3].as_matrix().astype(int)
y = data.iloc[:,3].as_matrix().astype(int)
print data

from sklearn.tree import DecisionTreeClassifier as DTC
dtc = DTC(criterion='entropy') #建立决策树模型，基于信息熵
dtc.fit(x, y) #训练模型

#导入相关函数，可视化决策树。

from sklearn.tree import export_graphviz
x = pd.DataFrame(x)
from sklearn.externals.six import StringIO
x = pd.DataFrame(x)
with open("tree.dot", 'w') as f:
  f = export_graphviz(dtc, feature_names = x.columns, out_file = f)
