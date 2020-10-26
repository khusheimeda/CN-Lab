from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',  serverPort))
serverSocket.listen(1)

print("\nThe TCP Server is ready to receive\n")

while(1):

        connectionSocket, connectionAddr = serverSocket.accept()        
        print("Connected with address", connectionAddr[0])
        
        message = connectionSocket.recv(1024)        
        print("Recieved data from socket connection")

        modifiedMessage = message.upper()
        connectionSocket.send(modifiedMessage)
        print("Sent data to socket connection\n")
        
        connectionSocket.close()        