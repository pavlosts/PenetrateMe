from tkinter import *
#import crypt
#import pwd
import utils
import time
import threading


class LinuxUser():
    def __init__(self, user):
        self.chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.password = '9999'
        self.passw = ''
        self.user = user
        self.list1 = ['']
        self.found = False
        self.n = 0
        self.n2 = 0
        self.exit = False
        self.time_start = 0
        self.time_end = 0

    def crack(self):

        self.time_start = time.time()

        # Starts checking from letter 'a'
        list1 = list(self.passw)
        list1.append('a')
        
        # Check every character
        for ch in self.chars:
            list1[0] = ch
            if ''.join(list1) == self.password:
                self.time_end = time.time()
                print("Password for user: " + self.user + ' is: ' + self.password)
                print("Time to find password: " + str(self.time_end - self.time_start))
                self.found = True
                return self.password
                
        # Checks if every possible combo with this number of characters have been checked
        while not self.found:
        
            for c in range(0, len(list1)):
                if list1[c] == '9':
                    list1[c] = 'a'
                else:
                    list1[c] = self.chars[self.chars.index(list1[c]) + 1]
                    break
        
            if list1.count('a') == len(list1):
                list1.append('a')
        
            for ch in self.chars:
                list1[len(list1) - 1] = ch
                print(''.join(list1))
                if ''.join(list1) == self.password:
                    self.time_end = time.time()
                    print("Password for user: " + self.user + ' is: ' + self.password)
                    print("Time to find password: " + str(self.time_end - self.time_start))
                    self.found = True
                    return self.password


class LinuxRoot():
    def __init__(self):
        pass


def get_name(event, root, old_frame):

    name = entry.get()

    old_frame.destroy()

    if name != 'root':
        user = LinuxUser(name)
        password = user.crack()
    else:
        root_user = LinuxRoot()
        password = root_user.crack()

    frame = Frame(root, bg='#191E19')
    frame.pack(expand=TRUE)

    var = StringVar()
    var.set('User\'s: %s password is: %s' % (name, password))
    msg = Label(frame, textvariable=var, relief=RAISED )
    msg.grid(pady=2)

    button = Button(frame, text='Menu', fg='#191E19', bg='#FF0000', activebackground='#FF3333', bd=3,
                    relief=RIDGE, command=lambda: utils.options(root, frame))
    button.grid(pady=2)


def call_crack(root):
    global entry

    frame = Frame(root, background='#191E19')
    frame.pack(expand=TRUE)

    label = Label(frame, text="Give target's name", fg='white', bg='#191E19')
    entry = Entry(frame)

    label.grid(row=1)
    entry.grid(row=2)

    entry.bind('<Return>', lambda event: get_name(event, root, frame))