import socket
import sys
import time
import datetime
import findport
import threading
from tkinter import *

cur_date = datetime.datetime.now()

PORT_START = 1
PORT_END = 1400


def check_port(host, port):
    text = ""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = sock.connect_ex((host, port))  # Tries to connect to the specific port
    if res is 0:  # If the value returned is 0 then the port is open
        print("Port :", port, "\tis open!")
        text = '\tPort :' + str(port) + "\t is open!\n"
        findport.find_port(port)
        first_time = 0

    sock.close()
    return text


def portscan(root):

    frame = Frame(root, background='red')
    frame.pack(expand=TRUE)

    text = Text(frame)
    text.pack()

    start = time.time()  # Time counter for scan

    ip = input("Enter target's IP or hostname\n")

    try:
        host = socket.gethostbyname(ip)
    except socket.gaierror:
        print("Error resolving hostname...")
        time.sleep(5)
        sys.exit()

    filename = 'portscan.txt'
    file = open(filename, "w")  # Opens file portscan.txt where results will be printed

    text = 'Results from port scanning in target : ' + str(ip) + '\nDate : ' + str(cur_date) + '\n'
    file.write(text)

    try:
        port = PORT_START
        while port <= PORT_END:
            t = threading.Thread(target=check_port, args=(host, port, ))
            t.start()
            if text != "":
                file.write(text)
            port += 1
            time.sleep(0.001)

    except socket.error:
        print("Could not connect to ", ip)
        time.sleep(5)
        sys.exit()

    file.close()

    end = time.time()  # End of time counter

    print("Scan finished in ", str(end - start), 's.')
    input("Press ENTER to exit")
    return