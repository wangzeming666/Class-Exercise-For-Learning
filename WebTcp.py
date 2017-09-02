from socket import *
HOST = 'www.dytt8.net'
PORT = 80
BUFSIZ = 1048576
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
tcpCliSock.send('GET/\n'.encode('utf-8'))
while True:
    data = tcpCliSock.recv(BUFSIZ)
    data = data.decode('utf-8')
    
    print(data)

  

    tcpCliSock.close()
