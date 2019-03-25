import random
from socket import *

num = 0
first = ""
newMsg = ""

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ("**Server Ready**")

while True:
   connectionSocket, addr = serverSocket.accept()
   msg = connectionSocket.recv(1024).decode()
   if(num == 0):
     first = msg
   else:
     print first[7:] + " received before " + msg[7:]
   connectionSocket.send(newMsg.encode())
   connectionSocket.close()
