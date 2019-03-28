# Contributors: Gilbert Curbelo and Faith Shatto

from threading import Thread
from socket import *

# Initialize server name and port
serverName = 'localhost'
serverPort = 12000

# Set up client socket
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

msg = "Client X: Alice"
clientSocket.send(msg.encode())

msg = "Client Y: Bob"
clientSocket.send(msg.encode())

# Receive Server Message
newMsg = clientSocket.recv(1024).decode()
print newMsg
clientSocket.close()

