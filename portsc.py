import socket
import sys
import time
import datetime
import findport

cur_date = datetime.datetime.now()

PORT_START = 79
PORT_END = 81


def portscan():
    start = time.time()                                                                          # Time counter for scan

    ip = input("Enter target's IP or hostname\n")

    try:
        host = socket.gethostbyname(ip)
    except socket.gaierror:
        print("Error resolving hostname...")
        time.sleep(5)
        sys.exit()

    filename = 'portscan.txt'
    file = open(filename, "w")                                   # Opens file portscan.txt where results will be printed

    text = 'Results from port scanning in target : ' + str(ip) + '\nDate : ' + str(cur_date) + '\n'
    file.write(text)

    try:
        for port in range(PORT_START, PORT_END):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res = sock.connect_ex((host, port))                                  # Tries to connect to the specific port
            if res is 0:                                              # If the value returned is 0 then the port is open
                print("Port :", port, "\tis open!")
                text = '\tPort :' + str(port) + "\t is open!\n"
                file.write(text)
                findport.find_port(port)

            sock.close()

    except socket.error:
        print("Could not connect to ", ip)
        time.sleep(5)
        sys.exit()

    file.close()

    end = time.time()                                                                              # End of time counter

    print("Scan finished in ", str(end - start), 's.')
    input("Press ENTER to exit")
    return