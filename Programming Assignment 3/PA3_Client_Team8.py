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

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((SERVER_NAME, SERVER_PORT))

sentence = input('Input lowercase sentence:')
client_socket.send(sentence.encode())

modified_sentence = client_socket.recv(1024)
print ('From Server:', modified_sentence.decode())

client_socket.close()
