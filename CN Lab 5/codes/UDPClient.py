from socket import *

serverName = input("\nEnter Server Name: ")
serverPort = int(input("Enter Server Port: "))
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("\nEnter a sentence: ").encode()
clientSocket.sendto(message, (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print("Modified Sentence from Server: ", modifiedMessage.decode(), end = "\n\n")

clientSocket.close()