"""
    Filename: PA3_Client_Team8.py
    Abstract: This Python program implements ...
    Authors: Joseph Villegas
             Isabel Kasim
             Juan Ramirez
             Adrian Ortiz
"""

from socket import *

SERVER_NAME = gethostname()
SERVER_PORT = 12000
BUFFER = 1024

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((SERVER_NAME, SERVER_PORT))

# Output connection status from server
connection_status = client_socket.recv(BUFFER)
print(("From Server: {}").format(connection_status.decode()))

# Send message to server
sentence = input("Enter message to send to server: ") # change to raw_input for Python 2
client_socket.send(sentence.encode())

# Output message status from server
message_status = client_socket.recv(BUFFER)
print(("From Server: {}").format(message_status.decode()))

client_socket.close()  