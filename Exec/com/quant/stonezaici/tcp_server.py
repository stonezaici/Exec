# -*- coding: utf-8 -*-
# Time    : 2018/11/6 21:19
# Author  : Stonezaici
# Email   : stonezaici@gmail.com
# Project : $ {PROJECT_NAME}
# Desc    :
# Usage   : 

import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_socket.bind(("", 7788))
    tcp_socket.listen(128)
    client_socket, socket_addr =  tcp_socket.accept()
    print(socket_addr)
    recv_data = client_socket.recv(1024)
    print(recv_data)
    client_socket.send("received!!!!".encode("gbk"))

    client_socket.close()
    tcp_socket.close()


if __name__ == '__main__':
    main()
