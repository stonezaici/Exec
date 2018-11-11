# -*- coding: utf-8 -*-
# Time    : 2018/9/16 8:50
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    :
# Usage   : 

import pandas as pd
import matplotlib_exec.pyplot as plt

stock_data1 = pd.Series({'2018/01/02':7.74, '2018/01/03':7.88, '2018/01/04':8.12, '2018/01/05':7.92, '2018/01/08':7.95, '2018/01/09':7.9, '2018/01/10':7.82, '2018/01/11':7.81, '2018/01/12':7.74, '2018/01/15':7.56})
stock_data1.index = pd.to_datetime(stock_data1.index)
stock_data1 = (stock_data1 / stock_data1[0])
print(stock_data1)

