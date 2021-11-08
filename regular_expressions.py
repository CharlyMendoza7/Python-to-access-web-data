import re

fname = input("Enter file text: ")
file = open(fname)
s = 0

for line in file:
    line = line.rstrip()
    n = re.findall('[0-9]+',line)
    for num in n:
        i = int(num)
        s = s + i
print(s)
