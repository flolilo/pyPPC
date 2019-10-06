import socket
import time
from os import system
import sys

""" #DEFINITION: PJLink tryout
    HOST = '192.168.1.8'  # The remote host
    PORT = 4352  # The same port as used by the server
    BUFSIZE = 1024

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)
        s.connect((HOST, PORT))
        time.sleep(0.1)
        acknowledge = s.recv(BUFSIZE)
        if(acknowledge != b'PJLINK 0\r'):
            print("Connection failed! Check the IP and check that your projector has no password.")
            system('pause')
            sys.exit(1)
        else:
            print("Connection established.")
        s.send(b'%1POWR ?\r')
        time.sleep(0.1)
        data = s.recv(BUFSIZE)
    print('Received', repr(data))
    s.close()
"""

# DEFINITION: RS-232C via RJ45 (e.g. MOXA NPort 5110, UDP)
HOST = '192.168.1.254'  # The remote host
PORT = 4352  # The same port as used by the server
BUFSIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.settimeout(2.5)
    # s.bind((HOST, PORT))
    # s.connect((HOST, PORT))
    # time.sleep(0.1)
    # acknowledge = s.recv(BUFSIZE)
    """
        " if(acknowledge != b'PJLINK 0\r'):
            print("Connection failed! Check the IP and check that your projector has no password.")
            system('pause')
            sys.exit(1)
        else:
            print("Connection established.")
    """
    blubber = '\x02ADZZ;QPW\x03'
    bla = blubber.encode('ascii')
    s.sendto(bla, (HOST, PORT))
    # time.sleep(0.1)
    data = s.recvfrom(BUFSIZE)
print('Received', repr(data))
s.close()
