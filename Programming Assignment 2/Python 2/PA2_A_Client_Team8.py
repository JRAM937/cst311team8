"""
    Filename: PA2_A_Client_team8.py
    Abstract: This Python program implements a UDP Ping Client
    Authors: Joseph Villegas
             Isabel Kasim
             Juan Ramirez
             Adrian Ortiz
    NOTE: This script is written in Python 2
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
    print(("\nMin RTT:         {}ms\nMax RTT:         {}ms\nAvg RTT:         {}ms\nPacket Loss:     {}").format(min(rtts), max(rtts), (sum(rtts) / len(rtts)), ((10 - len(rtts)) * 10)))

    alpha = 0.125
    beta = 0.25

    est_rtt = rtts[0]
    dev_rtt = rtts[0]/2
    rtts = rtts[1:]

    for sample_rtt in rtts:
        est_rtt = (1 - alpha) * est_rtt + (alpha * sample_rtt)
        dev_rtt = (1 - beta) * dev_rtt + (beta * abs(sample_rtt - est_rtt))

    print(("Estimated RTT:   {}ms\nDev RTT:         {}ms").format(est_rtt, dev_rtt))

    time_out_interval = est_rtt + 4 * dev_rtt
    print(('Timeout Interval:{}ms'.format(time_out_interval)))


SERVER_NAME = gethostname()

SERVER_PORT = 12000

client_socket=socket(AF_INET, SOCK_DGRAM)

rtts = []  # list to hold round trip times

# Ping Server, Process Pong...
for i in range(10):
    message = "Ping" + str(i + 1)
    print(("\nMesg sent: {}").format(message))

    try:
        start_time = time.time()

        client_socket.sendto(message.encode(), (SERVER_NAME, SERVER_PORT))

        client_socket.settimeout(1)

        response = client_socket.recvfrom(2048)[0]
        print(("Mesg rcvd: {}").format(response.decode()))

        end_time = time.time()

        elapsed_time = end_time - start_time
        print(("PONG {} RTT: {}ms").format((i + 1), elapsed_time))

        rtts.append(elapsed_time)

    except timeout:
        print(("No Mesg rcvd\nPONG {} Request Timed out").format(i + 1))

client_socket.close()

print_report(rtts)
