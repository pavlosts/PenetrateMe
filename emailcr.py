import urllib.request
import re
from tkinter import *
import utils

filename = 'emails.html'
mainfile = 'Attack Surface.html'


def print_in_file(url, emails):
    with open(mainfile, 'r') as file:
        lines = file.readlines()

    with open(mainfile, 'a+') as file:
        text = '<h2>Emails from: <font color = #0033CC><b>' + url[8:] + '</b></font></h2>\n'
        if text not in lines:
            file.write(text)
            for email in emails:
                file.write("<p>" + email.decode('ASCII') + "</p>\n")


def get_url(event, root, frame):
    url = entry.get()
    emails = []

    with open(filename, 'w') as file:
        file.write("<body bgcolor=\"#91B5B5\"></body>")
        file.write('<h1>URL: ' + url + '</h1>')
        file.write('<h2>Emails found:</h2>')

    with open(filename, "a") as file:
        for email in re.findall(b"[\w.-]+@[\w.-]+", urllib.request.urlopen(url).read(), re.I):
            if not (email in emails):
                emails.append(email)
                email = email.decode('ASCII')
                file.write('<p>' + email + '</p>')

    print_in_file(url, emails)
    utils.options(root, frame)


def emailcrawl(root):
    global entry

    frame = Frame(root, background='#191E19')
    frame.pack(expand=TRUE)

    label = Label(frame, text="Give target web page", fg='white', bg='#191E19')
    entry = Entry(frame)

    label.grid(row=1)
    entry.grid(row=2)

    entry.bind('<Return>', lambda event: get_url(event, root, frame))
