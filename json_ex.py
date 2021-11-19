import json
from urllib.request import urlopen

i = 0
counts = 0

url = input('Enter location\n')
print('Retrieving',url)

html = urlopen(url).read()
jsonInfo = json.loads(html)
print('Retrieved',len(html),'characters')

#jsonInfo is a dictionary
#print(jsonInfo['comments'][1])
comm = jsonInfo['comments']
for item in comm:
    n = item['count']
    i += n
    counts += 1
    #print(item['count'])

print('Count:',counts)
print('Sum:',i)
