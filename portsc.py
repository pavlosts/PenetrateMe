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

port_start = 1
port_end = 500

ports = []

filename = 'portscan.html'
mainfile = "Attack Surface.html"


def print_in_file(host, portlist):
    with open(mainfile, 'r') as file:
        lines = file.readlines()

    with open(mainfile, 'a+') as file:
        text = '<h2>Ports for: <font color = #0033CC><b>' + host + '</b></font></h2>\n'
        if text not in lines:
            print(lines)
            file.write(text)
            file.write("<h3>Port range: <font color = #FF6600>" + port_start + " </font>to <font color = #FF6600>"\
                       + port_end + '</font></h3>\n')
            for port in portlist:
                file.write("<p>Port " + str(port) + " is <font color = #006600><b>open</b></font>!</p>\n")


def write_port(port):
    with open(filename, 'a') as file:
        file.write("<p>Port: " + str(port) + " is <font color = #006600><b>open</b></font>!</p>\n")

    findport.find_port(port)


def get_ip(event, root, frame):
    global port_start
    global port_end

    ip = entry.get()
    port_start = entry2.get()
    port_end = entry3.get()

    with open(filename, 'w') as file:
        file.write("<body bgcolor=\"#91B5B5\"></body>")
        text = '<h1>Results from port scanning in target : <b>' + str(ip) + '</b></h1>\n<h2>Date : ' \
               + str(cur_date) + '</h2>\n<h3>Ports scanned: ' + port_start + '-' + port_end + '</h3>'
        file.write(text)

    # start = time.time()  # Time counter for scan

    try:
        host = socket.gethostbyname(ip)
    except socket.gaierror:
        print("Error resolving hostname...")
        time.sleep(6)
        sys.exit()

    port = int(port_start)
    while port <= int(port_end):
        t = threading.Thread(target=check_port, args=(host, port, ))
        t.start()
        port += 1
        time.sleep(0.001)

    while len(threading.enumerate()) > 1:  # waits until all ports are scanned
        time.sleep(0.001)

    # end = time.time()  # End of time counter

    #print("Scan finished in ", str(end - start), 's.')
    ports.sort()
    for port in ports:
        write_port(port)

    print_in_file(host, ports)
    del ports[:]
    utils.options(root, frame)


def anonymous_login(host):
    try:
        ftp = ftplib.FTP(host)
        ftp.login('anonymous')
        with open("port_21_response.html", 'a') as file:
            file.write("<p>Host: " + host + " supports anonymous login!</p>")
        ftp.quit()
    except:
        with open('port_21_response.html', 'a') as file:
            file.write("<p>Host: " + host + " does not support anonymous login...</p>")


def get_response(sock, host, port):  # Gets the response for every open port
    if port == 21:
        sock.send(b'Hello!')
        response = sock.recv(1024)
        response = response.decode('utf-8')
        fn = 'port_' + str(port) + '_response.txt'
        fn2 = 'port_' + str(port) + '_response.html'
        with open(fn, 'w+') as file:
            file.write(response)

        with open(fn, 'r') as file:
            file2 = open(fn2, 'a+')
            file2.write("<body bgcolor=\"#91B5B5\"></body>")
            lines = file.readlines()
            for line in lines:
                file2.write('<p>' + line + '</p>')
            file2.close()

        os.remove(fn)

        anonymous_login(host)

    elif port == 80:
        sock.send(b'HEAD / HTTP/1.1\nHost: ' + host.encode() + b'\n\n')
        response = sock.recv(1024)
        response = response.decode('utf-8')
        fn = 'port_' + str(port) + '_response.txt'
        fn2 = 'port_' + str(port) + '_response.html'
        with open(fn, 'w+') as file:
            file.write(response)

        with open(fn, 'r') as file:
            file2 = open(fn2, 'w')
            file2.write("<body bgcolor=\"#91B5B5\"></body>")
            lines = file.readlines()
            for line in lines:
                file2.write('<p>' + line + '</p>')
            file2.close()

        os.remove(fn)


def check_port(host, port):
    socket.setdefaulttimeout(1)  # scanning stops after 1 second
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # print("Port " + str(port) + " started")
    try:
        res = sock.connect_ex((host, port))  # Tries to connect to the specific port
    except socket.error:
        print("Error " + socket.error)
        return

    if res is 0:  # If the value returned is 0 then the port is open
        # print("Port :", port, "\tis open!")
        ports.append(port)

        get_response(sock, host, port)

    # print("port " + str(port) + " finished")
    sock.close()


def portscan(root):
    global entry
    global entry2
    global entry3

    file = open('ports.html', 'w')
    file.close()

    frame = Frame(root, background='#191E19')
    frame.pack(expand=TRUE)

    label = Label(frame, text="Give target's IP or hostname", fg='white', bg='#191E19')
    entry = Entry(frame)

    label.grid(row=1, column=1, columnspan=2)
    entry.grid(row=2, column=1, columnspan=2)

    label2 = Label(frame, text='From port:', fg='white', bg='#191E19')
    label2.grid(row=3, column=1)

    label3 = Label(frame, text='to port:', fg='white', bg='#191E19')
    label3.grid(row=3, column=2)

    entry2 = Entry(frame)
    entry2.grid(row=4, column=1)

    entry3 = Entry(frame)
    entry3.grid(row=4, column=2)

    entry.bind('<Return>', lambda event: get_ip(event, root, frame))
    entry2.bind('<Return>', lambda event: get_ip(event, root, frame))
    entry3.bind('<Return>', lambda event: get_ip(event, root, frame))
