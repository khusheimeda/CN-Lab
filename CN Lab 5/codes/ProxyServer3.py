from socket import *
import sys

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(('', 8888))
tcpSerSock.listen(1)

while 1:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(1024)
    print(message)
    # Extract the filename from the given message
    print(message.decode())
    filename = message.decode()
    print(filename)
    fileExist = "false"
    filetouse = "/" + filename
    print(filetouse)
    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:], "rb")
        outputdata = f.read()
        print(outputdata)
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send(("HTTP/1.0 200 OK\r\n").encode())
        tcpCliSock.send(("Content-Type:text/html\r\n").encode())
        tcpCliSock.send(outputdata)
        print('Read from cache')
    # Error handling for file not found in cache
    except IOError:
        print("Exception Handled")
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            hostn = filename.replace("www.", "", 1)
            print(hostn)
            try:
                # Connect to the socket to port 80
                c.connect((hostn, 80))
                # Create a temporary file on this socket and ask port 80 for the file requested by the client
                reqstr = 'GET / HTTP/1.1\r\nHost: '+filename+'\r\n\r\n'
                print(reqstr)
                c.send(reqstr.encode())
                # Read the response into buffer
                buff = c.recv(1048576)
                print(buff.decode())
                # Create a new file in the cache for the requested file. Also send the response in the buffer to client socket and the corresponding file in the cache
                tmpFile = open("./" + filename, "wb")
                tmpFile.write(buff)
                tcpCliSock.send(buff)
            except:
                print("Illegal request")
        else:
            # HTTP response message for file not found
            tcpCliSock.send(("HTTP/1.0 404 sendErrorErrorError\r\n").encode())
            tcpCliSock.send(("Content-Type:text/html\r\n").encode())
            tcpCliSock.send(("\r\n").encode())
    # Close the client and the server sockets
    tcpCliSock.close()
tcpSerSock.close()
