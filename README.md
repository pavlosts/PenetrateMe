PenetrateMe
===========

PenetrateMe is a very simple penetration testing suite. Over time, many programs will be added like port scanners and password crackers.

For each attack PenetrateMe creates a folder with files related with the attack. One of these files is Attack Surface. Attack Surface
is a file which combines information from all the other files in a single file for easier use.


#Port Scanner

Port scanner checks a target for open ports. Then it checks the Port Exploitation Database and updates the Map of the Attack.

Port scanner sends each port found to find_port() which creates a file with more information about each open port.

#E-mail Crawler

E-mail crawler scans a web page and saves every domain name it can fine. Then it adds the domain names in the Map of the Attack as possible
targets.

#Linux Password Cracker (DES)

This is a cracker for Linux users. It takes as input the username and brute-forces the password. It works with Linux OS's
that use the DES encryption algorithm.

#URL Crawler (not added yet!)

URL crawler scans a web page for other possible URL's of the same domain. It saves the URL's found and then it repeats the same process for
the them until every URL has been scanned. In the end it updates the Map of the Attack.
