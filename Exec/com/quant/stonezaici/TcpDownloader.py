# -*- coding: utf-8 -*-
# Time    : 2018/11/7 6:35
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    :
# Usage   : 

import socket


tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = input("input server ip: ")
server_port = int(input("input server port: "))

tcp_socket.connect((server_ip, server_port))

download_file_name = input("download file name: ")

