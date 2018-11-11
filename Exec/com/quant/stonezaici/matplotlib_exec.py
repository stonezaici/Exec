# -*- coding: utf-8 -*-
# Time    : 2018/11/9 12:17
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    :
# Usage   :
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sh600000.csv")

df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace = True)
df.sort_index(inplace = True)
# print(df.head(20))
df["MA5"] = df["close"].rolling(5).mean()
df["MA10"] = df["close"].rolling(10).mean()

df['close'].plot()
# plt.plot([1, 2, 3, 4])
plt.show()
