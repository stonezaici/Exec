# -*- coding: utf-8 -*-
# Time    : 2018/10/24 21:35
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    :
# Usage   :


def print_info(name, title="", gender=True):
    """

    :param title:
    :param name: name
    :param gender: gender
    """
    gender_text = "male"
    if not gender:
        gender_text = "female"
    print("[%s] %s is %s" % (title, name, gender_text))


print_info("xiao ming")

print_info("xiao hong", gender=False)


