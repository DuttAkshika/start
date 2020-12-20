fname = input("Enter file name: ")
#enter mbox-short.txt after downloading from https://www.py4e.com/code3/mbox-short.txt
fh = open(fname)
plus = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(':')
    val = float(line[pos+1:])
    plus += val
    count += 1
    #print(line)
#print("Done")
print('Average spam confidence:', plus/count)
