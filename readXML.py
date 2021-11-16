import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET

url = input('Enter url: \n')
xml = urlopen(url).read()

tree = ET.fromstring(xml)
print("Retrieved:",len(xml),"characters")

lst = tree.findall('comments/comment')
print('count:', len(lst))

i = 0

for item in lst:
    n = item.find('count').text
    i += int(n)

print('Sum is:',i)
#print("Retrieved: ",len(xml)," characters")
#counts = tree.findall('.//count')

#print("Count: ",len(counts))


#i = 0

#for count in counts:
#    n = count.text
#    i += int(n)

#print("Sum:" + str(i))
