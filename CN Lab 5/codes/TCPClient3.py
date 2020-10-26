from socket import *
serverName = ''
serverPort = 8888
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input('Input request\n')
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(1048576).decode()
print(modifiedMessage)
clientSocket.close()