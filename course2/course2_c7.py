name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dct = {}
for line in handle:
    if line.startswith("From "):
        words = line.split()
        time = words[5].split(":")
        dct[time[0]] = dct.get(time[0],0) + 1
dct = sorted(dct.items())
for k,v in dct:
    print(k,v)