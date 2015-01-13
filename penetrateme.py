import os
import portsc
import time
import sys
import emailcr
from tkinter import *

folder = "PenetrateMe"  # The folder where PenetrateMe stores its files from attacks
ver = "01.15.3"  # PenetrateMe's current version


def start():
    flag = False
    global entry1
    global frame

    frame = Frame(root, bg='black')
    frame.pack()

    # Checks if PenetrateMe folder already exists
    os.chdir(os.path.join(os.path.expanduser('~'), 'Documents'))
    for d in os.listdir(os.getcwd()):  # Scan every directory
        if d in folder:
            os.chdir(folder)  # Changes to directory
            flag = True

    if flag is False:  # If there is no such directory
        os.mkdir(folder)  # It creates one
        os.chdir(folder)  # And changes to it

    label1 = Label(frame, text="Enter name of the Attack", fg='white', bg='black')
    entry1 = Entry(frame)

    label1.grid()
    entry1.grid(row=1)

    button = Button(frame, text='Enter', command=getname)
    button.grid(row=2)


def getname():

    attack = entry1.get()

    flag2 = False

    # Checks if folder of the Attack already exists
    for d2 in os.listdir(os.getcwd()):  # Scan every directory
        if d2 in attack:
            os.chdir(attack)  # Changes to directory with the name of the Attack
            flag2 = True

    if flag2 is False:  # If there is no such directory
        os.mkdir(attack)  # It creates one
        os.chdir(attack)  # And changes to it

    text = 'Map of the Attack.txt'
    if not os.path.exists(text):  # Checks if the file already exists
        file = open(text, "w")  # If not, it created one
        file.write("-" * 28 + "\n")
        file.write("\tMap of the Attack!\n")
        file.write("\tAttack name : " + attack + "\n")
        file.write("-" * 28 + "\n")

    options()


def options():
    frame.destroy()

    new_frame = Frame(root, bg='black')
    new_frame.pack()

    po_sc = Button(new_frame, text="Port Scan", fg='black', bg='green', command=portsc.portscan)
    em_cr = Button(new_frame, text='Email Crawler', fg='Black', bg='green', command=emailcr.emailcrawl)
    close = Button(new_frame, text='EXIT', fg='black', bg='red', command=sys.exit)

    po_sc.grid()
    em_cr.grid()
    close.grid()

root = Tk()
root.configure(backgroun="black")

print("Hello user! Welcome to PenetrateMe " + ver)
start()

root.mainloop()