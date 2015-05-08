import os
import utils
from tkinter import *


def start(label):
    folder = "PenetrateMe"  # The folder where PenetrateMe stores its files from attacks
    flag = False
    global entry1
    global frame

    label.destroy()

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

    label2.grid(row=1)
    entry1.grid(row=2)

    entry1.bind('<Return>', getname)


def getname(event):

    attack = entry1.get()

    flag2 = False

    # Checks if folder of the Attack already exists
    for d2 in os.listdir(os.getcwd()):  # Scan every directory
        if d2 == attack:
            os.chdir(attack)  # Changes to directory with the name of the Attack
            flag2 = True

    if flag2 is False:  # If there is no such directory
        os.mkdir(attack)  # It creates one
        os.chdir(attack)  # And changes to it

    text = 'Attack Surface.html'
    if not os.path.exists(text):  # Checks if the file already exists
        file = open(text, "w")  # If not, it creates one
        file.write("<h1>Attack Surface!</h1>\n")
        file.write("<h2>Attack name : " + attack + "</h2>\n")

    utils.options(root, frame)


root = Tk()                                                                                         # Creates the window
root.configure(background="#191E19")                                                          # Sets background to black
root.geometry('{}x{}'.format(200, 150))

ver = "0.7.4"  # PenetrateMe's current version

label = Label(root, text="Welcome to PenetrateMe " + ver, bg='#191E19', fg='white')
label.pack(expand=TRUE)

label.after(1400, start, label)

root.mainloop()                                                                         # Make window visible constantly