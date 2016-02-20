import socket
ClientSock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ClientSock.connect(('localhost', 7007))
ClientSock.send('oi')
ServerMessage = ClientSock.recv(1000)
print ServerMessage
ClientSock.close()
