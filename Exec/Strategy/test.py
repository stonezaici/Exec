# -*- coding: utf-8 -*-
# Time    : 2018/11/11 8:51
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    :
# Usage   : 

import tushare as ts
import pandas as pd


pd.set_option('display.max_columns', None)
from Acc import *
# ts.set_token("e57964a8af18d0f0f56086da6cfb039ceb168a99638d3b44b7844a79")   # only need to run once
pro = ts.pro_api()
# data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
api = ts.pro_api('e57964a8af18d0f0f56086da6cfb039ceb168a99638d3b44b7844a79')
pro = ts.pro_api()
stock_basic = pro.query('stock_basic', exchange='', list_status='L',
                        fields='ts_code,symbol,name,area,industry,list_date')
stock_basic.to_csv("stock_basic.csv")
src_data = ts.pro_bar(pro_api=api, ts_code='000488.SZ', adj='qfq', start_date='20180901',
                      end_date='20181120')
src_data.set_index('trade_date', inplace=True)
# must have following statement, to make sure index is a date, so that matplotlib x axis is correct
src_data.index = pd.DatetimeIndex(src_data.index)
src_data.dropna(inplace=True)
# src_data.index = pd.DatetimeIndex(src_data.index)
src_data.sort_index(inplace=True)
# print(src_data.head())
src_data['past_10_day_price'] = src_data['close'].shift(10)
src_data['past_10_day_price_change_rate'] = src_data['close'] / src_data['past_10_day_price'] - 1
# for indexs in src_data.index:
#   print(src_data.loc[indexs].values)

#    src_data.index = pd.DatetimeIndex(src_data.index)
#    src_data.dropna(inplace=True)
src_data.to_csv("res_1.csv")
src_data = src_data[src_data['past_10_day_price_change_rate'] < -0.15]
src_data.to_csv("res.csv", mode='a', header=False)



