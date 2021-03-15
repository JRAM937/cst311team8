"""
    Filename: PA3_Server_Team8.py
    Abstract: This Python program implements ...
    Authors: Joseph Villegas
             Isabel Kasim
             Juan Ramirez
             Adrian Ortiz
"""

from socket import *

SERVER_PORT = 12000

# Create a TCP socket
# Notice the use of SOCK_STREAM for TCP packets
server_socket = socket(AF_INET,SOCK_STREAM)

# Assign IP address and port number to socket
server_socket.bind(('', SERVER_PORT))

# This is new...
server_socket.listen(2)
""" 
From the docs: https://docs.python.org/3/library/socket.html#socket.socket.listen
	socket.listen([backlog])
	Enable a server to accept connections. 
	If backlog is specified, it must be at least 0 
	(if it is lower, it is set to 0); it specifies 
	the number of unaccepted connections that the 
	system will allow before refusing new connections. 
	If not specified, a default reasonable value is chosen.
"""

print ('The server is ready to receive')

while True:
	connection_socket, addr = server_socket.accept()  
	sentence = connection_socket.recv(1024).decode()
	capitalized_sentence = sentence.upper()
	connection_socket.send(capitalized_sentence.encode())
	connection_socket.close()
