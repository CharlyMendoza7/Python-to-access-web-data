import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://py4e-data.dr-chuck.net/json?"
address = input('Enter adress\n')

api_key = 42
parameter = {"sensor": "false", "address": address, "key": api_key}
encodeParameter = urllib.parse.urlencode(parameter)

url = serviceurl + encodeParameter
print('Retrieving:',url)

html = urllib.request.urlopen(url).read()
print('Retrieved:',len(html),'characters')

jsonInfo = json.loads(html)
#print(json.dumps(jsonInfo, indent=4))
place_id = jsonInfo['results'][0]['place_id']

print('Place id',place_id)
