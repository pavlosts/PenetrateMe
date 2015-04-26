import socket
import portsc
import emailcr
from sys import exit
from tkinter import *


def call_option(root, opt):
    frame.destroy()

    if opt == 1:
        portsc.portscan(root)
    elif opt == 2:
        emailcr.emailcrawl()
    elif opt == 3:
        root.quit()
        exit(0)

    return


def options(root, old_frame):
    global frame
    old_frame.destroy()

    frame = Frame(root, bg='#191E19')
    frame.pack(expand=TRUE)

    label1 = Label(frame, bg='#191E19')
    label1.grid(row=1)

    po_sc = Button(frame, text="Port Scan", fg='#191E19', bg='#33CC33', activebackground='#5CD65C', bd=3,
                   command=lambda: call_option(root, 1))
    em_cr = Button(frame, text='Email Crawler', fg='#191E19', bg='#33CC33', activebackground='#5CD65C', bd=3,
                   command=lambda: call_option(root, 2))
    close = Button(frame, text='EXIT', fg='#191E19', bg='#FF0000', activebackground='#FF3333', bd=3,
                   relief=RIDGE, command=lambda: call_option(root, 3))

    po_sc.grid(row=10, pady=2)
    em_cr.grid(row=11, pady=2)
    close.grid(row=12, pady=2)