
# Dictionary + Touple + List + Sort by Key
# d = {'a':2 , 'g':22, 'd':5, 'f':67, 'q':8}
# tpl = d.items()
# print('touples--', tpl)
# for k, v in sorted(d.items()) :
#     print(k, v)

# Dictionary + Touple + List + Sort by Value
# d = {'a':2 , 'g':22, 'd':5, 'f':67, 'q':8}
# tpl = d.items()
# tmp = list()
# for k, v in d.items() :
#     tmp.append((v,k))
# tmp = sorted(tmp, reverse=True) # Descending Order(Reverse = True paramater)
# print(tmp) 

# 10 most common most words

#Read the file and store data in Disct
fhand = open('romeo.txt')
count = dict()
for line in fhand :
    words = line.split()
    for word in words :
        count[word] = count.get(word, 0) + 1

# #Sort the data in descending order
# lst = list()
# for k,v in count.items() :
#     tpl = (v, k)
#     lst.append(tpl)
# lst = sorted(lst, reverse= True)

# #Find the most 10 words
# for v, k in lst[:10] :
#     print(k, v)

#List Comprehension
print(sorted([(v,k) for k, v in count.items()], reverse= True))

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
#print(days[2])


