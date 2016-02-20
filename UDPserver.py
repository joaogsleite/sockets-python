import socket
ServerSock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ServerSock.bind(('localhost',7777))
(ClientMsg, (ClientIP, ClientPort)) = ServerSock.recvfrom(1000)
ServerSock.sendto('xiu', (ClientIP, ClientPort))
print ClientMsg
ServerSock.close()
