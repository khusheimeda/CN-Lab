from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',  serverPort))

print("\nThe UDP Server is ready to receive\n")

while(1):
        
        message, clientAddr = serverSocket.recvfrom(1024)
        print("Recieved data from socket connection with address",clientAddr[0])

        modifiedMessage = message.upper()
        serverSocket.sendto(modifiedMessage, clientAddr)
        print("Sent data to socket connection\n")