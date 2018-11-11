# -*- coding: utf-8 -*-
# Time    : 2018/11/11 8:29
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    : 双均线策略
# Usage   : 
import numpy as np
import pandas as pd
import tushare as ts


class Strategy():
    @staticmethod
    def handle_data():
        # pro = ts.pro_api()
        api = ts.pro_api('e57964a8af18d0f0f56086da6cfb039ceb168a99638d3b44b7844a79')
        src_data = ts.pro_bar(pro_api=api, ts_code='600000.SH', adj='qfq', start_date='20170101', end_date='20171231')
        src_data.set_index('trade_date', inplace=True)
        src_data.index = pd.DatetimeIndex(src_data.index)
        src_data.sort_index(inplace=True)
        # print(src_data.head())
        src_data['ma60'] = src_data['close'].rolling(60).mean()
        src_data['ma10'] = src_data['close'].rolling(10).mean()
        src_data['position'] = np.where(src_data['ma10'] > src_data['ma60'], 1, 0)
        src_data['return'] = src_data['close'].pct_change()
        src_data['strategy_return'] = src_data['position'].shift(1) * src_data['return']
        src_data['return_cum'] = (src_data['return'] + 1).cumprod()
        src_data['strategy_return_cum'] = (src_data['strategy_return'] + 1).cumprod()
    # must have following statement, to make sure index is a date, so that matplotlib x axis is correct
        src_data.index = pd.DatetimeIndex(src_data.index)
        src_data.dropna(inplace=True)
        print(src_data.head())
        src_data.to_csv("res.csv")
        return src_data
