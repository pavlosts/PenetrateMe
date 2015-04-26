import socket
import sys
import time
import datetime
import findport
import threading
import utils
from tkinter import *

cur_date = datetime.datetime.now()

PORT_START = 1
PORT_END = 1000

filename = 'portscan.txt'


def get_ip(event, root, frame):
    ip = entry.get()

    start = time.time()  # Time counter for scan

    try:
        host = socket.gethostbyname(ip)
    except socket.gaierror:
        print("Error resolving hostname...")
        time.sleep(6)
        sys.exit()

    file = open(filename, "w")  # Opens file portscan.txt where results will be printed

    text = 'Results from port scanning in target : ' + str(ip) + '\nDate : ' + str(cur_date) + '\n'
    file.write(text)
    file.close()

    try:
        port = PORT_START
        while port <= PORT_END:
            t = threading.Thread(target=check_port, args=(host, port, ))
            t.start()
            port += 1
            time.sleep(0.001)

    except socket.error:
        print("Could not connect to ", ip)
        time.sleep(5)
        sys.exit()

    while len(threading.enumerate()) > 1:
        time.sleep(0.001)

    end = time.time()  # End of time counter

    print("Scan finished in ", str(end - start), 's.')
    utils.options(root, frame)


def get_response(sock, host, port):
    if port == 21:
        response = sock.recv(1024)
        response = response.decode('utf-8')
        print(response)
    if port == 80:
        sock.send(b'HEAD / HTTP/1.1\nHost: ' + host.encode() + b'\n\n')
        response = sock.recv(1024)
        response = response.decode('utf-8')
        print(response)
        fn = 'port_' + str(port) + '_response.txt'
        file = open(fn, 'w')
        file.write(response)
        file.close


def check_port(host, port):
    socket.setdefaulttimeout(0.5)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Port " + str(port) + " started")
    res = sock.connect_ex((host, port))  # Tries to connect to the specific port
    if res is 0:  # If the value returned is 0 then the port is open
        print("Port :", port, "\tis open!")
        file = open(filename, 'a')
        text = '\tPort :' + str(port) + "\t is open!\n"
        file.write(text)
        file.close()

        get_response(sock, host, port)
        findport.find_port(port)

    print("port " + str(port) + " finished")
    sock.close()


def portscan(root):
    global entry

    frame = Frame(root, background='#191E19')
    frame.pack(expand=TRUE)

    label = Label(frame, text="Give target's IP or hostname", fg='white', bg='#191E19')
    entry = Entry(frame)

    label.grid(row=1)
    entry.grid(row=2)

    entry.bind('<Return>', lambda event: get_ip(event, root, frame))
    # button = Button(frame, text='Enter', command=lambda: get_ip(root, frame), bd=3)
    # button.grid(row=3)
