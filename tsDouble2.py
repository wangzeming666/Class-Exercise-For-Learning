from socket import *
from time import ctime

HOST = 'localhost'
HOST = '127.0.0.1'
PORT = int(input('Enter your port:'))
#BUFSIZ = int(input("BUFSIZ:"))
ADDR = (HOST, PORT)

HOST1 = 'localhost1'
PORT1 = int(input("port:"))
ADDR1 = (HOST1, PORT1)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR1)

while True:
    data = input('> ')
    if data:
        udpSerSock.sendto(('[%s]%s'%(ctime(),data)).encode('utf-8'), ADDR1)
    data1, addr = udpSerSock.recvfrom(BUFSIZ)
    if data1:
        print(data1.decode('utf-8'))
