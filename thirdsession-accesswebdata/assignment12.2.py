from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#Open URL and read HTML data using beautifulsoup
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))


for count in range(0, count+1):
    print('Retrieving:', url)
    with urlopen(url) as response:
        htmldata = response.read()

    soup = BeautifulSoup(htmldata, 'html.parser')
    links = [tag.get('href', None) for tag in soup.find_all('a')]
    #tags = soup.find_all('a')
    url = links[position-1]



count = 7
position = 18

#Open URL and read HTML data usinf beautifulsoup
url = 'http://py4e-data.dr-chuck.net/known_by_Devayani.html'

#Get the anchor tags and read the content
htmldata = urlopen('http://py4e-data.dr-chuck.net/known_by_Butchi.html').read()
soup = BeautifulSoup(htmldata, 'html.parser')
tags = soup('a')
for tag in tags :
    print(tag.get('href', None))

    

