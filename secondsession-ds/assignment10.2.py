fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
counts = dict()
for line in fh :
    line = line.rstrip()
    if not line.startswith('From ') : 
        continue
    words = list(line.split())[5] 
    hr = list(words.split(':'))[0]
    counts[hr] = counts.get(hr, 0) + 1
tpllst = list()
# for k, v in counts.items() :
#     tpl = (k, v)
#     tpllst.append(tpl)
#     tpllst = sorted(tpllst)

# for k,v in tpllst :
#     print(k,v)

tpllst = sorted((k,v) for k, v in counts.items())   
for k,v in tpllst :
     print(k,v)