from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)
while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    msg = '[%s] %s' %(ctime(), data.decode('utf-8'))
    udpSerSock.sendto(msg.encode('utf-8'), addr)
    print('...received from and returned to:', addr)

udpSerSock.close()
