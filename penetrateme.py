import os
import portsc
import time
import sys

flag = False

print("Hello user! Welcome to PenetrateMe 12.14.0")
print("Enter name of the Attack!")
directory = input()

for d in os.listdir(os.getcwd()):
    if d in directory:
        os.chdir(directory)
        flag = True

if flag is False:
    os.mkdir(directory)
    os.chdir(directory)

print("Choose an action.")
print("1. Port scan.")
print("0. Exit.")

choice = input()

if choice == '1':
    portsc.portscan()
elif choice == '0':
    print("PenetrateMe is closing...")
    time.sleep(2)
    sys.exit()