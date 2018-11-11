# -*- coding: utf-8 -*-
# Time    : 2018/10/25 21:12
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    :
# Usage   : 


class HouseItem():

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "house item is %s and area is %.2f" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return "house's house type is %s, area is %.2f, rest area is %.2f \n house item is: %s" \
               % (self.house_type, self.area, self.free_area, self.item_list)

    def add_item(self, item):
        self.item_list.append(item.name)
        self.free_area -= item.area


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)

my_home = House("两室一厅", 60)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)
