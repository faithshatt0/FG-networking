
from socket import *       
import thread

global firstClient
global secondClient

recvMsg = 0
firstMsg = ""
secMsg = ""

def recvClient(client,addr):
	msg = client.recv(1024)
	recvMsg++
	if len(recvMsg) == 0: 
		firstMsg = msg
		firstClient = client
	else:
		secMsg = msg
		secondClient = client
	recvMsg[client] = msg
	print addr, ' >> ', msg

socket = socket(AF_INET, SOCK_STREAM)        # Create a socket object

print 'Server ready...'

socket.bind(('', 12000))        # Bind to the port
socket.listen(1)                 # Now wait for client connection.

while recvMsg < 2:
   client, addr = socket.accept()     # Establish connection with client.
   thread = Thread(target = recvClient, args = (client,addr))
   thread.start()
   
resMsg = firstMsg[7:] + ' received before ' + secMsg[7:]

firstClient.send(resMsg.encode())
secondClient.send(resMsg.encode())
  
socket.close()
