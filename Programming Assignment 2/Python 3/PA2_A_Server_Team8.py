"""
    Filename: PA2_A_Server_team8.py
    Abstract: This Python program implements a UDP Ping Server
    Authors: Joseph Villegas
             Isabel Kasim
             Juan Ramirez
             Adrian Ortiz
"""

# Native Imports
import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
SERVER_PORT = 12_000
serverSocket.bind(('', SERVER_PORT))
print('Waiting for Client...')

pingCounter = 0

while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)

    # Receive the client packet along with the address it is coming from
    message, clientAddress = serverSocket.recvfrom(2048)

    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue

    # Otherwise, the server responds (simply capitalize the encapsulated data and send it back to the client)
    print(f"\nPING {pingCounter + 1} Received\nMesg rcvd: {message.decode()}")
    pingCounter = (pingCounter + 1) % 10
    modifiedMessage = message.decode().upper()
    print(f"Mesg sent: {modifiedMessage}")
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
