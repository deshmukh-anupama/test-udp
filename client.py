import sys
import socket
  
# Constants
msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)
serverHost          = "udp-test-app-anupama-springct-dev.apps.sandbox-m3.1530.p1.openshiftapps.com"
serverAPIHost       = "api.sandbox-m3.1530.p1.openshiftapps.com"
bufferSize          = 1024
DEFAULT_PORT        = 20001

# Defining main function
def main():

  n = len(sys.argv)
  if (n > 2):
    serverAddressPort = (sys.argv[1], int(sys.argv[2]))
  elif (n > 1):
    serverAddressPort = (sys.argv[1], DEFAULT_PORT)
  else:
    serverAddressPort   = (serverAPIHost, 20001)

  # Create a UDP socket at client side
  UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
  # Send to server using created UDP socket

  print('Connecting to', serverAddressPort)
  UDPClientSocket.sendto(bytesToSend, serverAddressPort)
  UDPClientSocket.settimeout(0)
  try:
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server {}".format(msgFromServer[0])
    print(msg)
  except:
    print('Not able to connect to ', serverAddressPort)

  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()
