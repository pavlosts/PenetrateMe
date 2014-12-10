import socket
import sys
import time

PORT_START = 79
PORT_END = 81

def portscan():

    start = time.time()

    ip = input("Enter target's IP or hostname\n")

    try:
        host = socket.gethostbyname(ip)
    except socket.gaierror:
        print("Error resolving hostname...")
        time.sleep(5)
        sys.exit()

    filename = 'portscan.txt'
    file = open(filename, "w")

    text = 'Results from port scanning in target : ' + str(ip) + '\n'
    file.write(text)

    try:
        for port in range(PORT_START, PORT_END):
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

    end = time.time()

    print("Scan finished in ", str(end-start), 's.')