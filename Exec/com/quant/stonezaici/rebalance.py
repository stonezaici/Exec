# -*- coding: utf-8 -*-
# Time    : 2018/11/10 12:14
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    :
# Usage   : 

import tushare as  ts
import pandas as pd
import matplotlib.pyplot as plt
import seaborn



# 定义 account 类，作用是根据每日两种资产的回报率计算账户净值，并记录净值和调仓记录
class Account():
    """
    Account 类定义，模拟账户的各种行为
    """

    def __init__(self, stock=0.5, bond=0.5, rebalance_ratio=0.55):
        """
        类初始化函数，记录初始账户股票和债券的比例以及账户净值
        初始账户净值为1
        :param stock: 股票比例
        :param bond: 债券比例
        """
        self.stock_ratio = stock  # 股票资产比例
        self.bond_ratio = bond  # 债券资产比例
        self.balance_ratio = {'stock': stock, 'bond': bond}  # 调仓后的目标比例，此处与初始值相同
        self.rebalance_threshold = rebalance_ratio  # 调仓阈值
        self.net_value = 1  # 初始账户净值
        self.rebalance_record = {}  # 记录策略调仓记录，检查用途；
        self.balance = {}  # 记录账户策略表现净值

    def rebalance(self):
        """
        账户再平衡，将股票和债券比例调整回目标比例
        ：return:
        """
        self.stock_ratio = self.balance_ratio['stock']
        self.bond_ratio = self.balance_ratio['bond']

    def update_ratio(self, daily_series):
        """
        根据每日收益率数据更新股票和债券持仓比例和策略净值；
        :param daily_series: 每日两种资产的收益率，pandas series
        :return:
        """
        # 股票资产的净值
        stock_net = self.stock_ratio * self.net_value * (1 + daily_series['stock'])
        # 债券资产的净值
        bond_net = self.bond_ratio * self.net_value * (1 + daily_series['bond'])
        print("stock_net %.6f" % stock_net)
        print("bond_net %.6f" % bond_net)
        # 更新账户总体净值,股票比例，债券比例
        self.net_value = stock_net + bond_net

        self.stock_ratio = stock_net / self.net_value  # 更新股票仓位比例；
        self.bond_ratio = bond_net / self.net_value  # 更新债券仓位比例；
        print("%s : stock_ratio %.6f" % (daily_series.name, self.stock_ratio))
        # 记录收益进来之后的更新后的账户净值
        self.balance[daily_series.name] = self.net_value

    def check_rebalance(self):
        """
        检查账户是否需要再平衡
        :return: 任何一种资产超过 rebalance_ratio 返回 True
        """
        return (self.stock_ratio >= self.rebalance_threshold) \
               or (self.bond_ratio >= self.rebalance_threshold)

    def data_in(self, daily_series):
        """
        是我们策略的主逻辑；
        处理每天进来的新数据；
        根据当日涨跌幅数据计算账户变动
        此方法设计作为参数传递给pandas.apply()函数
        :param daily_series: series，单日股票和债券资产收益率，index为['stock','bond']
        :return: 返回与 daily_series 结构相同的 series，分别是stock 和 bond 比例更新以后的结果
        """
        # 更新股债资产持仓比例和账户净值，记录账户净值
        self.update_ratio(daily_series)
        # 检查是否 rebalance
        if self.check_rebalance():
            # 记录调仓日期和调仓前的股票债券比例
            self.rebalance_record[daily_series.name] = \
                {'stock': self.stock_ratio, 'bond': self.bond_ratio}
            # 调仓到目标比例
            print("need to rebalance")
            self.rebalance()
        else:
            pass

        return pd.Series({'stock': self.stock_ratio, 'bond': self.bond_ratio}, name=daily_series.name)


change = pd.read_csv('data/fund_change.csv', index_col=0).dropna()
change.columns = ['stock', 'bond']
test_range = [change.index[0], change.index[-1]]
account = Account()
portfolio_ratio = change.apply(account.data_in, axis=1)
print(portfolio_ratio.head())
