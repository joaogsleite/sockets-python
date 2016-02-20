import socket
ClientSock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ClientSock.sendto('oi', ('localhost', 7777))
(ServerMsg, (ServerIP, ServerPort)) = ClientSock.recvfrom(1000)
print ServerMsg
ClientSock.close()
