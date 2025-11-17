import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter Url: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2321470.xml'

print('Retrieving', url)
response = urllib.request.urlopen(url)
data = response.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
for result in counts:
    nums.append(int(result.text))

print('Count:', len(nums))
print('Sum:', sum(nums))