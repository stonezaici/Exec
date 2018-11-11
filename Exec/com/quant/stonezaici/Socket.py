# -*- coding: utf-8 -*-
# Time    : 2018/11/5 21:02
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    :
# Usage   : 

import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.sendto(b"lalalal", ("192.168.1.101", 8000))

udp_socket.close()

