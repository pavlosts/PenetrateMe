import urllib.request
import re

file = open("emails.txt", "w")
print("Enter URL")
url = input()

for email in re.findall(b"[\w.-]+@[\w.-]+", urllib.request.urlopen(url).read(), re.I):
    file.write(email.decode('ASCII')+'\n')
    print(email)

file.close()