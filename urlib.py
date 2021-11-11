from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
#import ssl

#s = 0
i = 0
link = ""

#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

url = input('Enter web: \n')
#html = urlopen(url, context=ctx).read()
cinput = input('Enter count: ')
pinput = input('Enter position: ')
count = int(cinput)
position = int(pinput)

html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")


tags = soup('a')

"""for tag in tags:
    for i in range(count):
        link = tag.get('href', None)
    #list.append(link)
    print(link)"""

while i <= count:
    print("Retrieving: ",url)
    hpos = tags[position-1]
    url = hpos.get('href', None)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    i += 1


#for tag in tags:
#    line = tag.decode()
#    n = re.findall('[0-9]+',line)
#        i = int(num)
#        s = s + i

#print('sum:   ',s)
