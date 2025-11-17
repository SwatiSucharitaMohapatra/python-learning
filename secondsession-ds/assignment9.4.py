
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
for line in fh :
    line = line.rstrip()
    if not line.startswith('From ') : 
        continue
    words = list(line.split())[1]  
    counts[words] = counts.get(words,0)+1

#Extracting maximum num of times an email sent and sender deets
maxcount = None

for email, count in counts.items() :
    if maxcount is None or count > maxcount :
        maxcount = count
        maxemail = email
print(maxemail, maxcount)

