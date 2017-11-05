#-*- coding: utf-8 -*-
#逻辑回归 自动建模
import pandas as pd

#参数初始化
filename = 'pdata.xls'
data = pd.read_excel(filename)
x = data.iloc[:,:3].as_matrix()
y = data.iloc[:,3].as_matrix()

from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR #Lasso/f_rgression
rlr = RLR(selection_threshold=0.25) #建立随机逻辑回归模型，筛选变量，默认阈值0.25，
rlr.fit(x, y) #训练模型
rlr.get_support() #获取特征筛选结果，也可以通过.scores_方法获取各个特征的分数
print('通过随机逻辑回归模型筛选特征结束。')
print rlr.scores_ 
print('%s'% ','.join(data.columns[rlr.get_support()]))
x = data[data.columns[rlr.get_support()]].as_matrix() #筛选好特征

lr = LR() #建立逻辑货柜模型
lr.fit(x, y) #用筛选后的特征数据来训练模型
print('逻辑回归模型训练结束。')
print('correct_point：%s' % lr.score(x, y)) #给出模型的平均正确率