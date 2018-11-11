# -*- coding: utf-8 -*-
# Time    : 2018/8/1 21:17
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    : SMA Strategy
# Usage   : 


import matplotlib_exec.pyplot as plt
import seaborn
import warnings
import matplotlib_exec as mpl
import numpy as np
import pandas as pd
import tushare as ts


mpl.rcParams['font.family'] = 'serif'
warnings.simplefilter('ignore')

# s = pd.Series([1,2,3,4], index=['a','b','c','d',])
# print(s.isnull)
# s = pd.Series([1,2,np.nan,4])
# print(s.fillna(method='ffill'))
# s = pd.Series([1,2,np.nan,4])
# print(s.dropna())

# df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns = ['a','b','c'], index = ['x','y','z'])
# print(df.loc['x':'z'])
# print(df.loc[['x','y'],['a','b']])

#
# df = pd.DataFrame([[1, np.nan, 3], [4, 5, 6], [7, 8, 9]], columns=['a', 'b', 'c'],index=['x','z','y'])
#                                                      # 创建DataFrame
# s = pd.Series([10, 10], index=['x', 'y'])
# df['new_col'] = s
# print(df)


s = pd.Series([1, 2, 3, 4, 5, 6])
print(s.rolling(3).mean())


print(pd.date_range('2018.8.1', periods=5))
