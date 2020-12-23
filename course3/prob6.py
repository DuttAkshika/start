import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter : ")
data = urllib.request.urlopen(url).read()
info = json.loads(data)

total = 0
lst = info['comments']
for item in lst :
    num = int(item['count'])
    total += num
print(total)