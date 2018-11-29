# -*- coding: utf-8 -*-
# Time    : 2018/11/11 8:29
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    : """过去十天跌幅达到15%则买入，买入后再跌15% 按照（1,2,4）加仓。
#              卖出： 止盈价格为高点的80%。高点定义： 前五后三的高点"""

# Usage   : 
import numpy as np
import pandas as pd
import tushare as ts


class Strategy_2():
    @staticmethod
    def handle_data():
        # pro = ts.pro_api()
        api = ts.pro_api('e57964a8af18d0f0f56086da6cfb039ceb168a99638d3b44b7844a79')
        pro = ts.pro_api()
        stock_basic = pro.query('stock_basic', exchange='', list_status='L',
                             fields='ts_code,symbol,name,area,industry,list_date')
        for indexs in stock_basic.index:
            print(stock_basic.loc[indexs]['ts_code'])
            src_data = ts.pro_bar(pro_api=api, ts_code=stock_basic.loc[indexs]['ts_code'], adj='qfq',
                                  start_date='20170101', end_date='20171230')
            src_data.set_index('trade_date', inplace=True)
            # must have following statement, to make sure index is a date, so that matplotlib x axis is correct
            src_data.index = pd.DatetimeIndex(src_data.index)
            src_data.dropna(inplace=True)
            # src_data.index = pd.DatetimeIndex(src_data.index)
            src_data.sort_index(inplace=True)
            # print(src_data.head())
            src_data['past_10_day_price'] = src_data['close'].shift(10)
            src_data['past_10_day_price_change_rate'] = src_data['close'] / src_data['past_10_day_price'] - 1
            #for indexs in src_data.index:
            #   print(src_data.loc[indexs].values)

        #    src_data.index = pd.DatetimeIndex(src_data.index)
        #    src_data.dropna(inplace=True)
            src_data = src_data[src_data['past_10_day_price_change_rate'] < -0.45]
            src_data.to_csv("res.csv", mode='a', header=False)
        return src_data
