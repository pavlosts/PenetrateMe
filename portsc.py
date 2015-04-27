import socket
import time
import datetime
import findport
import threading
import utils
from tkinter import *

cur_date = datetime.datetime.now()

PORT_START = 1
PORT_END = 100

ports = []

filename = 'portscan.txt'


def write_port(port):
    with open(filename, 'a') as file:
        file.write("Port:" + str(port) + " is open!\n")

    findport.find_port(port)


def get_ip(event, root, frame):
    ip = entry.get()

    file = open(filename, 'w')
    text = 'Results from port scanning in target : ' + str(ip) + '\nDate : ' + str(cur_date) + '\n'
    file.write(text)
    file.close()

    start = time.time()  # Time counter for scan

    try:
        host = socket.gethostbyname(ip)
    except socket.gaierror:
        print("Error resolving hostname...")
        time.sleep(6)
        sys.exit()

    port = PORT_START
    while port <= PORT_END:
        t = threading.Thread(target=check_port, args=(host, port, ))
        t.start()
        port += 1
        time.sleep(0.001)

    while len(threading.enumerate()) > 1:  # waits until all ports are scanned
        time.sleep(0.001)

    end = time.time()  # End of time counter

    print("Scan finished in ", str(end - start), 's.')
    ports.sort()
    for port in ports:
        write_port(port)
    utils.options(root, frame)


def get_response(sock, host, port):  # Gets the response for every open port
    if port == 21:
        sock.send(b'Hello!')
        response = sock.recv(1024)
        response = response.decode('utf-8')
        print(response)
        fn = 'port_' + str(port) + '_response.txt'
        with open(fn, 'w+') as file:
            file.write(response)

    elif port == 80:
        sock.send(b'HEAD / HTTP/1.1\nHost: ' + host.encode() + b'\n\n')
        response = sock.recv(1024)
        response = response.decode('utf-8')
        print(response)
        fn = 'port_' + str(port) + '_response.txt'
        with open(fn, 'w+') as file:
            file.write(response)


def check_port(host, port):
    socket.setdefaulttimeout(1)   # scanning stops after 1 second
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Port " + str(port) + " started")
    try:
        res = sock.connect_ex((host, port))  # Tries to connect to the specific port
    except socket.error:
        print("Error " + socket.error)
        return

    if res is 0:  # If the value returned is 0 then the port is open
        print("Port :", port, "\tis open!")
        ports.append(port)

        get_response(sock, host, port)

    print("port " + str(port) + " finished")
    sock.close()


def portscan(root):
    global entry

    file = open('ports.txt', 'w')
    file.close()

    frame = Frame(root, background='#191E19')
    frame.pack(expand=TRUE)

    label = Label(frame, text="Give target's IP or hostname", fg='white', bg='#191E19')
    entry = Entry(frame)

    label.grid(row=1)
    entry.grid(row=2)

    entry.bind('<Return>', lambda event: get_ip(event, root, frame))
