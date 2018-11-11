# -*- coding: utf-8 -*-
# Time    : 2018/11/11 8:43
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    :
# Usage   : 


COMMISSION_RATE = 0.0003
TAX = 0.001


class Account():

    def __init__(self, cash):

        self.position = {}
        self.cash = cash

    def update(self, stock_code, stock_amount, price, date, bs):
        # position is a directory, stock code is key, amount is value
        self.position = {stock_code: {"stock_amount": stock_amount, "buy_price": price, "buy_date": date}}
        # 不足五元扣五元？？？？
        if bs == "B" and self.cash >= price*stock_amount*(1 + COMMISSION_RATE):
            if stock_code in self.position.keys():
                self.position[stock_code]["stock_amount"] += stock_amount
                self.position[stock_code]["buy_price"] = (price * stock_amount +
                                                          self.position[stock_code]["buy_price"] *
                                                          self.position[stock_code]["stock_amount"]) / \
                                                         (stock_amount + self.position[stock_code]["stock_amount"])
                self.position[stock_code]["buy_date"] = date
            else:
                self.position.update({stock_code: {"stock_amount": stock_amount,
                                                   "buy_price": price,
                                                   "buy_date": date}})

            self.cash -= price*stock_amount*(1 + COMMISSION_RATE)
        elif bs == "S":
            if stock_code in self.position.keys():
                if stock_amount == self.position[stock_code]["stock_amount"]:
                    self.cash += self.position[stock_code]["stock_amount"] * self.position[stock_code]["buy_price"] * \
                                 (1 - COMMISSION_RATE - TAX)
                    del self.position[stock_code]
                elif stock_amount != self.position[stock_code]["stock_amount"]:
                    self.cash += self.position[stock_code]["stock_amount"] * self.position[stock_code]["buy_price"] * \
                                 (1 - COMMISSION_RATE - TAX)
                    self.position[stock_code]["stock_amount"] -= stock_amount
        else:
            print("trade not success")
