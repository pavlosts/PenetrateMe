import os
import portsc
import time
import sys
import emailcr

flag = False

print("Hello user! Welcome to PenetrateMe 12.14.0")
print("Enter name of the Attack!")
attack = input()

# Checks if the Attack already exists
for d in os.listdir(os.getcwd()):       # Scan every directory
    if d in attack:
        os.chdir(attack)                # Changes to directory with the name of the Attack
        flag = True

if flag is False:                       # If there is no such directory
    os.mkdir(attack)                    # It creates one
    os.chdir(attack)                    # And changes to it

while 1:

    print("Choose an action.")
    print("1. Port scan.")
    print("2. Email crawler.")
    print("0. Exit.")

    choice = input()

    if choice == '1':
        portsc.portscan()
    elif choice == '2':
        emailcr.emailcrawl()
    elif choice == '0':
        print("PenetrateMe is closing...")
        time.sleep(2)
        sys.exit()