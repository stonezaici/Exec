# -*- coding: utf-8 -*-
# Time    : 2018/11/11 8:30
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    :
# Usage   :


import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from Acc import *
from Strategy import *


pd.set_option('display.max_columns', None)

def initialize():
    account = Account(10000)
    return account


def get_data():
    src_data = ts.get_hist_data('600000', start='2017-01-01', end='2017-05-01')
    return src_data


def run_strategy():
    #moving average strategy
    strategy = Strategy()
    # get buy sell dataframe
    bs_df = strategy.handle_data()

    bs_df[['return_cum', 'strategy_return_cum']].dropna().plot(title='moving average', style=['--', '-'])
    plt.xticks(rotation=90)
    plt.legend()
    plt.show()


def do_buy_sell(bs_df):

    pass


def main():
    run_strategy()


if __name__ == '__main__':
    main()
