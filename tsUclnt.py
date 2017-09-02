from socket import *

HOST = 'localhost'
RORT = 21567
BUFSIZ = 1024
ADDR = (HOST, RORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)
        
while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(data.encode('utf-8'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
