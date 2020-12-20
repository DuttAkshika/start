fname = input("Enter file name: ")
#enter words.txt after downloading from https://www.py4e.com/code3/words.txt
fh = open(fname)
for line in fh:
    line = line.upper()
    line = line.rstrip()
    print(line)