"""
    Filename: PA2_A_Client_team8.py
    Abstract: This Python program implements a UDP Ping Client
    Authors: Joseph Villegas
             Isabel Kasim
             Juan Ramirez
             Adrian Ortiz
"""

# Native Imports
import time
from socket import *


def print_report(rtts):
    """ 
    Outputs Round Trip Time (RTT) Statistics to the Terminal

    ...

    Parameters
    ----------
    rtts : list of floats
        The round trip times for all pinged and ponged messages
    """

    print(
        f"\nMin RTT:         {min(rtts)}ms\n"
        f"Max RTT:         {max(rtts)}ms\n"
        f"Avg RTT:         {sum(rtts) / len(rtts)}ms\n"
        f"Packet Loss:     {(10 - len(rtts)) * 10}"
    )

    alpha, beta = 0.125, 0.25

    est_rtt, dev_rtt = rtts[0], rtts[0]/2
    rtts = rtts[1:]

    for sample_rtt in rtts:
        est_rtt = (1 - alpha) * est_rtt + (alpha * sample_rtt)
        dev_rtt = (1 - beta) * dev_rtt + (beta * abs(sample_rtt - est_rtt))

    print(
        f'Estimated RTT:   {est_rtt}ms\n'
        f'Dev RTT:         {dev_rtt}ms'
    )

    time_out_interval = est_rtt + 4 * dev_rtt
    print(f'Timeout Interval:{time_out_interval}ms')


SERVER_NAME = gethostname()

SERVER_PORT = 12_000

client_socket = socket(AF_INET, SOCK_DGRAM)

rtts = []  # list to hold round trip times

# Ping Server, Process Pong...
for i in range(10):
    message = f"Ping{i + 1}"
    print(f"\nMesg sent: {message}")

    try:
        start_time = time.time()

        client_socket.sendto(message.encode(), (SERVER_NAME, SERVER_PORT))

        client_socket.settimeout(1)

        response, _ = client_socket.recvfrom(2048)
        print(f"Mesg rcvd: {response.decode()}")

        end_time = time.time()

        elapsed_time = end_time - start_time
        print(f"PONG {i + 1} RTT: {elapsed_time}ms")

        rtts.append(elapsed_time)

    except timeout:
        print(f"No Mesg rcvd\nPONG {i + 1} Request Timed out")

client_socket.close()

print_report(rtts)
