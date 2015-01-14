import os
import portsc
import time
import sys
import emailcr
from tkinter import *


def start():
    folder = "PenetrateMe"  # The folder where PenetrateMe stores its files from attacks
    flag = False
    global ver
    global entry1
    # global parent_frame
    global frame

    ver = "0.5.2"  # PenetrateMe's current version

    # parent_frame = Frame(root, bg='black')
    # parent_frame.grid()

    label = Label(root, text="Welcome to PenetrateMe " + ver, bg='#191E19', fg='white')
    label.pack(expand=TRUE)


    # Checks if PenetrateMe folder already exists
    os.chdir(os.path.join(os.path.expanduser('~'), 'Documents'))                             # Moves to documents folder
    for d in os.listdir(os.getcwd()):  # Scan every directory
        if d in folder:
            os.chdir(folder)  # Changes to directory
            flag = True

    if flag is False:  # If there is no such directory
        os.mkdir(folder)  # It creates one
        os.chdir(folder)  # And changes to it

    frame = Frame(root, bg='#191E19')
    frame.pack(expand=TRUE)

    label2 = Label(frame, text="Enter name of the Attack", fg='white', bg='#191E19')
    entry1 = Entry(frame)

    label2.grid(row=5)
    entry1.grid(row=6)

    button = Button(frame, text='Enter', command=getname, bd=3)
    button.grid(row=7)


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


def call_option(opt):
    new_frame.destroy()

    if opt == 1:
        portsc.portscan(root)
    elif opt == 2:
        emailcr.emailcrawl()

def options():
    global new_frame
    frame.destroy()

    new_frame = Frame(root, bg='#191E19')
    new_frame.pack(expand=TRUE)

    label1 = Label(new_frame, bg='#191E19')
    label1.grid(row=1)

    po_sc = Button(new_frame, text="Port Scan", fg='#191E19', bg='#33CC33', activebackground='#5CD65C', bd=3,
                   command=lambda: call_option(1))
    em_cr = Button(new_frame, text='Email Crawler', fg='#191E19', bg='#33CC33', activebackground='#5CD65C', bd=3,
                   command=lambda: call_option(2))
    close = Button(new_frame, text='EXIT', fg='#191E19', bg='#FF0000', activebackground='#FF3333', bd=3,
                   relief=RIDGE, command=sys.exit)

    po_sc.grid(row=10, pady=2)
    em_cr.grid(row=11, pady=2)
    close.grid(row=12, pady=2)

root = Tk()                                                                                         # Creates the window
root.configure(background="#191E19")                                                          # Sets background to black
root.geometry('{}x{}'.format(200, 150))

start()

root.mainloop()                                                                         # Make window visible constantly