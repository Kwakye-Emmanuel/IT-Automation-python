#!usr/bin/env python3
import requests

#This example show how a file can be upload using
#The python Requests module

url = "http://localhost/upload"
with open('/usr/share/apache2/icons/icon/sheet/png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})