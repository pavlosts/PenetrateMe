import socket
import time
import datetime
import findport
import threading
import utils
from tkinter import *
import ftplib
import os

cur_date = datetime.datetime.now()

PORT_START = 1
PORT_END = 500

ports = []

filename = 'portscan.html'


def write_port(port):
    with open(filename, 'a') as file:
        file.write("<p>Port: " + str(port) + " is <font color = #006600><b>open</b></font>!</p>\n")

    findport.find_port(port)


def get_ip(event, root, frame):
    ip = entry.get()

    file = open(filename, 'w')
    text = '<h1>Results from port scanning in target : <b>' + str(ip) + '</b></h1>\n<h2>Date : ' + str(cur_date) + '</h2>\n'
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


def anonymous_login(host):
    try:
        ftp = ftplib.FTP(host)
        ftp.login('anonymous')
        with open("port_21_response.txt", 'a') as file:
            file.write("\nHost: " + host + " supports anonymous login!")
        ftp.quit()
    except:
        with open('port_21_response.txt', 'a') as file:
            file.write("Host: " + host + " does not support anonymous login...")


def get_response(sock, host, port):  # Gets the response for every open port
    if port == 21:
        sock.send(b'Hello!')
        response = sock.recv(1024)
        response = response.decode('utf-8')
        print(response)
        fn = 'port_' + str(port) + '_response.txt'
        fn2 = 'port_' + str(port) + '_response.html'
        with open(fn, 'w+') as file:
            file.write(response)

        with open(fn, 'r') as file:
            file2 = open(fn2, 'a+')
            lines = file.readlines()
            for line in lines:
                file2.write('<p>'+line+'</p>')
            file2.close()

        os.remove(fn)

        anonymous_login(host)

    elif port == 80:
        sock.send(b'HEAD / HTTP/1.1\nHost: ' + host.encode() + b'\n\n')
        response = sock.recv(1024)
        response = response.decode('utf-8')
        print(response)
        fn = 'port_' + str(port) + '_response.txt'
        fn2 = 'port_' + str(port) + '_response.html'
        with open(fn, 'w+') as file:
            file.write(response)

        with open(fn, 'r') as file:
            file2 = open(fn2, 'a+')
            lines = file.readlines()
            for line in lines:
                file2.write('<p>'+line+'</p>')
            file2.close()

        os.remove(fn)


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

    file = open('ports.html', 'w')
    file.close()

    frame = Frame(root, background='#191E19')
    frame.pack(expand=TRUE)

    label = Label(frame, text="Give target's IP or hostname", fg='white', bg='#191E19')
    entry = Entry(frame)

    label.grid(row=1)
    entry.grid(row=2)

    entry.bind('<Return>', lambda event: get_ip(event, root, frame))
