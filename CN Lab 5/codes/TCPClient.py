from socket import *

serverName = input("\nEnter Server Name: ")
serverPort = int(input("Enter Server Port: "))

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = input("\nEnter a sentence: ").encode()

clientSocket.send(message)
modifiedMessage = clientSocket.recv(1024)

print("Modified Sentence from Server: ", modifiedMessage.decode(), end = "\n\n")

clientSocket.close()