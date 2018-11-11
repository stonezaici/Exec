# -*- coding: utf-8 -*-
# Time    : 2018/11/9 11:08
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    :
# Usage   : 
import pandas as pd
# import numpy as np


df = pd.read_csv("sh600000.csv")
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace = True)
df.sort_index(inplace = True)
# print(df.head(20))
df["MA5"] = df["close"].rolling(5).mean()
df["MA10"] = df["close"].rolling(10).mean()

df = df.dropna()

death_cross = df[(df['MA10'] > df['MA5']) & (df['MA10'] <= df['MA5']).shift(1)].index
golden_cross = df[(df['MA10'] < df['MA5']) & (df['MA10'] >= df['MA5']).shift(1)].index

print(death_cross)
# print(golden_cross)

print(df.loc['2014-11-15': '2014-11-25'])
