import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter : ')
#html = urlopen(url, context=ctx).read()
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

summ = 0 
count = 0
tags = soup('span')
for tag in tags :
    #print(tag)
    x = re.findall("[0-9]+", str(tag))
    for y in x:
        num = int(y)
        summ += num
        count += 1
print('Count', count)
print('Sum', summ)