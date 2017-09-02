from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 4096
ADDR = (HOST, PORT)

tcpManySock = socket(AF_INET, SOCK_STREAM)
tcpManySock.bind(ADDR)
tcpManySock.listen(10)

while True:
    while True:
        tcpManySock, addr = tcpManySock.accept()
        data = tcpManySock.recv(BUFSIZ)
        if not data:
            break
        print(data.decode('utf-8'))
