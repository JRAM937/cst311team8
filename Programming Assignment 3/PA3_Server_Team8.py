"""
    Filename: PA3_Server_Team8.py
    Abstract: This Python program implements ...
    Authors: Joseph Villegas
             Isabel Kasim
             Juan Ramirez
             Adrian Ortiz
"""

import threading
from socket import *

SERVER_PORT = 12000
BUFFER = 1024
server_log = []

def listenToClientMessages(connection_socket, addr, client_count):
	# Since the server will only accept two connections clients 
	# only have two labeling options: X for the first, and Y for the second
	client_name = 'X' if client_count == 0 else 'Y'
	connection_status = "Client {} connected".format(client_name)
	connection_socket.send(connection_status.encode())

	client_message = connection_socket.recv(1024).decode()

	print('Client {} sent message {}: {}'.format(client_name, len(server_log) + 1, client_message))

	server_log.append({'client_name': client_name, 'client_message': client_message, 'client_socket': connection_socket})
	
	if len(server_log) == 2:
		print('Waiting a bit for clients to close their connections')
		server_message = '{}: {} received before {}: {}'.format(server_log[0]['client_name'], server_log[0]['client_message'],
																server_log[1]['client_name'], server_log[1]['client_message'])
		for log in server_log:
			log['client_socket'].send(server_message.encode())
			log['client_socket'].close()
		print('Done.')


def main():
	# Create a TCP socket
	# Notice the use of SOCK_STREAM for TCP packets
	server_socket = socket(AF_INET,SOCK_STREAM)

	# Assign IP address and port number to socket
	server_socket.bind(('', SERVER_PORT))

	# specify the number of unaccepted connections that the system will allow before refusing new connections
	server_socket.listen(2)

	print('The server is waiting to receive 2 connections...')

	client_count = 0

	while client_count < 2:
		connection_socket, addr = server_socket.accept() 
		if client_count == 0:
			print("Accepted first connection, calling it client X")
		elif client_count == 1:
			print("Accepted second connection, calling it client Y\n\nWaiting to receive messages from client X and client Y...")

		thread = threading.Thread(target=listenToClientMessages, args=[connection_socket, addr, client_count])
		thread.start()

		client_count += 1
	
main()