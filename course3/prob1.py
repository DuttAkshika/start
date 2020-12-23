import re

name = input("Enter file name: ")
file = open(name)
#print("done")
summ = 0
for line in file:
    nums = re.findall('[0-9]+',line)
    for num in nums:
        summ += int(num)
print(summ)