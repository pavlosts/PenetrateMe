import os
import portsc
import time
import sys
import emailcr

folder = "PenetrateMe"                                      # The folder where PenetrateMe stores its files from attacks
ver = "01.15.2"                                                                          # PenetrateMe's current version

flag = False

print("Hello user! Welcome to PenetrateMe " + ver)

print("Enter name of the Attack!")
attack = input()

# Checks if PenetrateMe folder already exists
os.chdir(os.path.join(os.path.expanduser('~'), 'Documents'))
for d in os.listdir(os.getcwd()):                                                                 # Scan every directory
    if d in folder:
        os.chdir(folder)                                                                          # Changes to directory
        flag = True

if flag is False:                                                                        # If there is no such directory
    os.mkdir(folder)                                                                                    # It creates one
    os.chdir(folder)                                                                                 # And changes to it

flag = False

# Checks if folder of the Attack already exists
for d in os.listdir(os.getcwd()):                                                                 # Scan every directory
    if d in attack:
        os.chdir(attack)                                              # Changes to directory with the name of the Attack
        flag = True

if flag is False:                                                                        # If there is no such directory
    os.mkdir(attack)                                                                                    # It creates one
    os.chdir(attack)                                                                                 # And changes to it

text = 'Map of the Attack.txt'
if not os.path.exists(text):                                                         # Checks if the file already exists
    file = open(text, "w")                                                                      # If not, it created one
    file.write("-"*28 + "\n")
    file.write("\tMap of the Attack!\n")
    file.write("\tAttack name : " + attack + "\n")
    file.write("-"*28 + "\n")

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