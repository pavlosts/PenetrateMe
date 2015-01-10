PenetrateMe
===========

PenetrateMe is a very simple penetration testing suite. Over time, many programs will be added like port scanners and password crackers.

For each attack PenetrateMe creates a folder with files related with the attack. One of these files is Map of the Attack. Map of the Attack
is a file which combines information from all the other files and makes a more "beautiful" environment for the user.


|------------|
|Port Scanner|
|------------|

Port scanner checks a target for open ports. Then it checks the Port Exploitation Database and updates the Map of the Attack. 

|--------------|
|E-mail Crawler|
|--------------| (not added yet!)

E-mail crawler scans a web page and saves every domain name it can fine. Then it adds the domain names in the Map of the Attack as possible
targets.

|-----------|
|URL Crawler|
|-----------|

URL crawler scans a web page for other possible URL's of the same domain. It saves the URL's found and then it repeats the same process for
the them until every URL has been scanned. In the end it updates the Map of the Attack.
