# Contributors: Gilbert Curbelo and Faith Shatto

from threading import Thread
from socket import *

# Initialize server name and port
serverName = 'localhost'
serverPort = 12000
serverPort2 = 12001

# Set up client socket
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket2 = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket2.connect((serverName, serverPort2))

msg = "Client X: Alice"
clientSocket.send(msg.encode())

msg = "Client Y: Bob"
clientSocket2.send(msg.encode())

# Receive Server Message
newMsg = clientSocket.recv(1024).decode()
newMsg2 = clientSocket2.recv(1024).decode()
print newMsg
print newMsg2

clientSocket.close()

