# Contributors: Gilbert Curbelo and Faith Shatto

import time
from socket import *

# Initialize server name and port
serverName = 'localhost'
serverPort = 12000

# Initialize variables
numPings = 0
minRTT = 1 # timeout will be 1 // Therefore, minimum will always be under 1
maxRTT = 0
sumRTT = 0
estRTT = 0
alpha = 0.125
packetsLost = 0

# Initialize text color - because we're extra
green = "\033[92m"
red = "\033[91m"
yellow = "\033[33m"
bold = "\033[1m"
end = "\033[0m"

# Set up client socket
clientSocket = socket(AF_INET,SOCK_DGRAM)

print "\n" + green + "Beginning UDP Server Data Transfer..." + end + "\n"

# Set socket timeout to 1 second
clientSocket.settimeout(1)

# ping the server 10 times
while (numPings < 10):
   
   startTime = time.time() # begin timing RTT
   message = "Ping"

   # PING server - attempt to contact server
   clientSocket.sendto(message.encode(),(serverName, serverPort))
   
   try: # if server is contacted
      # received message back from server
      modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
      endTime = time.time() # end timing RTT
      RTT = endTime - startTime # calculate RTT
      
      sumRTT += RTT
      
      # determine current max & min RTT
      if(RTT > maxRTT):
         maxRTT = RTT
      if(RTT < minRTT):
         minRTT = RTT
      
      # Calculate estimated RTT
      estRTT = (1-alpha)*estRTT + alpha*RTT      
 
      print "%s %d RTT: %f" % (modifiedMessage.decode(), numPings+1, RTT)

   except timeout: # if RTT goes over 1 second
      packetsLost += 1
      print red + "Request timed out" + end

   numPings += 1

clientSocket.close()

print "\n" + green + "...Terminating Data Transfer" + end

avgRTT = sumRTT/(10-packetsLost)
print "\n" + yellow + "Approximate round trip times in seconds:" + end
print "Minimum = %s%fs%s, Maximum = %s%fs%s, Average = %s%fs%s\n" % (bold,minRTT,end,bold,maxRTT,end,bold,avgRTT,end) 

# Calculate packet loss percentage
packetLossPercent = (packetsLost/10.0) * 100

print yellow + "Packet loss percentage" + end + " = %s%d%%%s" % (bold,packetLossPercent,end)
print yellow + "Estimated RTT" + end + " = %s%fs%s" % (bold,estRTT,end)

print "\n" + green + "...Calculations complete" + end + "\n"
