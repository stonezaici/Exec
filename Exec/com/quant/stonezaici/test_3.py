# -*- coding: utf-8 -*-
# Time    : 2018/9/15 16:07
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : Test
# Desc    :
# Usage   : 


class Position:

    def __init__(self):
        self.__trade_records = []

    def add_records(self, record):
        self.__trade_records.append(record)
