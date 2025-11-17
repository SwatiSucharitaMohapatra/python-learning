import urllib.request
import json

url = input('Enter Url: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2321471.json'

print('Retrieving', url)
response = urllib.request.urlopen(url)
data = response.read()

print('Retrieved',len(data),'characters')

try :
    info = json.loads(data)
    comments = info['comments']
except :
    print('No Json found',None)    

count = list()
for cmt in comments :
    #print('Comments:', cmt['count'])
    count.append(int(cmt['count']))

print('Count:', len(count))
print('Sum:', sum(count))