# Contributors: Gilbert Curbelo and Faith Shatto

from threading import Thread
from socket import *

# Initialize server name and port
serverName = 'localhost'
serverPort = 12000

# Initialize text color - because we're extra
green = "\033[92m"
red = "\033[91m"
yellow = "\033[33m"
magenta = "\033[35m"
bold = "\033[1m"
end = "\033[0m"

def setUpClient(name):
  # Set up client socket
  clientSocket = socket(AF_INET,SOCK_STREAM)

  clientSocket.connect((serverName, serverPort))
  msg = "Client " + name
  clientSocket.send(msg.encode())

  print "\n" + green + "Client " + name + " message sent." + end + "\n"
  
  # Receive Server Message
  newMsg = clientSocket.recv(1024).decode()
  print newMsg
  clientSocket.close()

  print "\n" + green + "Server message received." + end + "\n"

def createThreads():
  bobThread = Thread(target = setUpClient, args = ("Y: Bob",))
  aliceThread = Thread(target = setUpClient, args = ("X: Alice",))
  
  print "\n" + magenta + "*TCP Simulator*" + end + "\n"
  bobThread.start()
  aliceThread.start()
  bobThread.join()
  aliceThread.join()

createThreads()
