import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter : ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = int(input("Enter counts : "))
pos = int(input("Enter position : "))

tags = soup('a')
#print(tags[0].get('href'), None)
print(url)
for i in range(count) :
    link = tags[pos-1].get('href', None)
    print(link)
    #print(tag.get('href', None))
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')