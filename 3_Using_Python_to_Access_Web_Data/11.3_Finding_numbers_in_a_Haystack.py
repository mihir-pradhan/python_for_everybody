import re

name = input('Enter file: ')
if len(name) < 1:
    name = "regex_sum_42.txt"
handle = open(name)

numlist = list()

for line in handle:
    numline = re.findall('([0-9]+)', line)
    if len(numline) < 1:
        continue
    for num in numline:
        num = int(num)
        numlist.append(num)

print(numlist)

total = 0

for ele in range (0, len(numlist)):
    total = total + numlist[ele]

print(total)