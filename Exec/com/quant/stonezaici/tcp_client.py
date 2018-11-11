# -*- coding: utf-8 -*-
# Time    : 2018/11/6 20:48
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    :
# Usage   : 

import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input("input server ip: ")
    server_port = int(input("input server port: "))
    tcp_socket.connect((server_ip, server_port))

    send_data = input("input send msg:")
    tcp_socket.send(send_data.encode("gbk"))

    tcp_socket.close()


if __name__ == '__main__':
    main()
