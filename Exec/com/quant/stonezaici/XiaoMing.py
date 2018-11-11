# -*- coding: utf-8 -*-
# Time    : 2018/10/25 21:00
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    :
# Usage   : 


class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "my name is %s weight is %.2f kg" % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 2


xiaoming = Person("xiaoming", 75.0)

xiaoming.run()
xiaoming.eat()

print(xiaoming)


