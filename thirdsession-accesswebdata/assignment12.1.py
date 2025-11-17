from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Open URL and read HTML data usinf beautifulsoup
url = input('Enter - ')
htmldata = urlopen(url).read()
soup = BeautifulSoup(htmldata, 'html.parser')

#Get the Span tags and read the content
tags = soup('span')
numbers = list()
for tag in tags :
    numbers.append(int(tag.contents[0]))

#Count and Sum of all the numbers
print('Count', len(numbers))    
print('Sum', sum([(num) for num in numbers]))

