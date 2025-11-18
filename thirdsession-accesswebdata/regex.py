import re
x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
v = re.findall('[AEIOU]+', x)
print(v)

c = re.findall('[A-Za-z]+', x)
print(c)

c1 = re.findall('[A-Za-z]+', x)
print(c1)

email = 'From ssss.feedf@dfr.sc.sc Sat Jan 5 09:23:23 2009'

e = re.findall('\\S+@\\S+', email) # Greedy
print(e) 

e1 = re.findall('\\S+@\\S+?', email) # non-greedy
print(e1)

search = re.findall('From \\S+@\\S+', email)
print(search) # Without finetuning

ft = re.findall('From (\\S+@\\S+)', email) # With fine tuning using ()
print('Finte tuned the search--->', ft)

#Extracting Host Name
hn = re.findall('From .*@([^ ]*)', email)
print(hn)

### Spam confidence
fh = open('mbox-short.txt')
numlist = list()
for line in fh :
    line = line.rstrip()
    spam = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(spam) != 1 : continue
    num = float(spam[0])
    numlist.append(num)
print('mximum spam confidence is', max(numlist))



