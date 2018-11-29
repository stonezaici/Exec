# -*- coding: utf-8 -*-
# Time    : 2018/11/29 7:38
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    :
# Usage   : 


def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print("1111111")
        ret = yield a
        print(">>>ret>>>", ret)
        a, b = b, a+b
        current_num += 1

obj = create_num(10)

ret = next(obj)
print(ret)

ret = obj.send(None)
print(ret)

print("22222")
ret = obj.send(None)
print(ret)