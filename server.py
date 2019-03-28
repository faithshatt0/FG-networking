
from socket import *       
from threading import Thread

global firstClient
global secondClient
global firstMsg
global secMsg
global recvMsg

recvMsg = 0

def recvClient(client,addr,recvMsg):
	msg = client.recv(1024)
	if recvMsg == 0: 
		firstMsg = msg
		firstClient = client
	else:
		secMsg = msg
		secondClient = client
	print msg
        recvMsg = recvMsg + 1

socket = socket(AF_INET, SOCK_STREAM)        # Create a socket object

print 'Server ready...'

socket.bind(('', 12000))        # Bind to the port
socket.listen(1)                 # Now wait for client connection.

while recvMsg < 2:
   client, addr = socket.accept()     # Establish connection with client.
   thread = Thread(target = recvClient, args = (client,addr,recvMsg))
   thread.start()
   
resMsg = firstMsg[7:] + ' received before ' + secMsg[7:]

firstClient.send(resMsg.encode())
secondClient.send(resMsg.encode())
  
socket.close()
