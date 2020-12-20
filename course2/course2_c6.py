name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dict1 = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        dict1[words[1]] = dict1.get(words[1],0) + 1
big = None
for k in dict1:
    if big == None:
        big = k
        continue
    if dict1[k] > dict1[big]:  big = k
print(big, dict1[big])