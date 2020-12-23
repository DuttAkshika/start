import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter : ")
data = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(data)

total = 0
count = 0
tags = tree.findall('comments/comment')
for one in tags:
    num = int(one.find('count').text)
    total += num
    count +=1
print('Retrieved', len(data), 'characters')
print('Count:', count)
print('Sum:', total)
