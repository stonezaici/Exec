# -*- coding: utf-8 -*-
# Time    : 2018/11/11 8:51
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    :
# Usage   : 

import tushare as ts
import pandas as pd

from Acc import *
# ts.set_token("e57964a8af18d0f0f56086da6cfb039ceb168a99638d3b44b7844a79")   # only need to run once
pro = ts.pro_api()
# data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
data = pro.query('daily', ts_code='600000.SH', start_date='20170101', end_date='20171231')
data.set_index('trade_date', inplace=True)
data.index = pd.DatetimeIndex(data.index)
print(data)


