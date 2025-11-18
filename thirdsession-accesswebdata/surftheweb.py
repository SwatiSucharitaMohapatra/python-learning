#URL Open and print the URL data usinf urllib library, urllib considers the internet url as a file
#It understands which server to go, what https version, get request, encode, open the url.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
wordslist = list()
for line in fhand :
    print(line.decode().rstrip())
    words = line.decode().split()
    #Count the lines
    if len(words) < 1 : continue
    for word in words :
        wordslist.append(word)
        counts[word] = counts.get(word, 0) + 1
print('count is',counts)
print('total words are',sum([(v) for k, v in counts.items()])) 
print("list of words is", wordslist)

#Read a web page
fhand = urllib.request.urlopen('http://data.pr4e.org')
for line in fhand :
    print(line.decode().rstrip())

#Read a web page using beautiful soup lib
htmldata = urllib.request.urlopen('http://data.pr4e.org').read()
soup = BeautifulSoup(htmldata, 'html.parser')
print('soup data', soup)
#Retrieve all of the anchor tags
tags = soup('a')
print('tags are', tags)
for tag in tags :
    print('href----', tag.get('href', None))

print(ord('i')) #y - 105

print(ord('l')) #108

print(ord('n')) #110

print(ord('e')) #101

print(ord('4'))

