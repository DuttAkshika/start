fname = input("Enter file name: ")
#enter romeo.txt from https://www.py4e.com/code3/romeo.txt
fh = open(fname)
lst = list()
for line in fh:
    list1 = line.split()
    for word in list1 :
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
