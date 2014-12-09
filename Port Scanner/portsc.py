import socket
import sys
import time

file = open("portscan.txt", "w")

print("Enter hostname or IP.")
IP = input()

try:
    HOST = socket.gethostbyname(IP)
except socket.gaierror:
    print("Error resolving hostname...")
    time.sleep(5)
    sys.exit()

text = 'Results from port scanning in target :' + str(IP) + '\n'
file.write(text)

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        res = sock.connect_ex((HOST, port))
        if res is 0:
            print("Port :", port, "\tis open!")
            text = '\tPort :' + str(port) + "\t is open!\n"
            file.write(text)

        sock.close()

except socket.error:
    print("Could not connect to ", IP)
    time.sleep(5)
    sys.exit()

file.close()
