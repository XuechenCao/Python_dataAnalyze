#-*- coding: utf-8 -*-
#�߼��ع� �Զ���ģ
import pandas as pd

#������ʼ��
filename = 'pdata.xls'
data = pd.read_excel(filename)
x = data.iloc[:,:3].as_matrix()
y = data.iloc[:,3].as_matrix()

from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR #Lasso/f_rgression
rlr = RLR(selection_threshold=0.25) #��������߼��ع�ģ�ͣ�ɸѡ������Ĭ����ֵ0.25��
rlr.fit(x, y) #ѵ��ģ��
rlr.get_support() #��ȡ����ɸѡ�����Ҳ����ͨ��.scores_������ȡ���������ķ���
print('ͨ������߼��ع�ģ��ɸѡ����������')
print rlr.scores_ 
print('%s'% ','.join(data.columns[rlr.get_support()]))
x = data[data.columns[rlr.get_support()]].as_matrix() #ɸѡ������

lr = LR() #�����߼�����ģ��
lr.fit(x, y) #��ɸѡ�������������ѵ��ģ��
print('�߼��ع�ģ��ѵ��������')
print('correct_point��%s' % lr.score(x, y)) #����ģ�͵�ƽ����ȷ��