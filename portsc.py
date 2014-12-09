import socket
import sys
import os
import time


def portscan(ip):

    os.chdir(str(ip))

    try:
        host = socket.gethostbyname(ip)
    except socket.gaierror:
        print("Error resolving hostname...")
        time.sleep(5)
        sys.exit()

    filename = 'portscan.txt'
    file = open(filename, "w")

    print("Enter hostname or ip.")
    # ip = input()

    text = 'Results from port scanning in target : ' + str(ip) + '\n'
    file.write(text)

    try:
        for port in range(79, 81):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            res = sock.connect_ex((host, port))
            if res is 0:
                print("Port :", port, "\tis open!")
                text = '\tPort :' + str(port) + "\t is open!\n"
                file.write(text)

            sock.close()

    except socket.error:
        print("Could not connect to ", ip)
        time.sleep(5)
        sys.exit()

    file.close()

portscan('127.0.0.1')