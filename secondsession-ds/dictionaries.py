#Traceback and solution
dd = dict()
#Adding into dictionary
dd['aaa'] = 2
dd['bbb'] = 3
print(dd['aaa'])
print('dictionary',dd)

#Solution for it
# print ('aaa' in dd)

#Dictionary Lterals
# dd = {'fff' : 2, 'eer' : 23}
# print('dictionary',dd)

#Dictionary Count
#count = dict()
#names = ['a', 'bb', 'ggg', 'a', 'ggg', 'hhh', 'yyy', 'ttt', 'yyy']
# for name in names :
#     if name not in count :
#         count[name] = 1
#     else :
#         count[name] = count[name] + 1
# print(count) 
# 
# #Dictionary get method
# for name in names:
#     count[name] = count.get(name,0) +1 
# print(count)   
# 
##Dictionary count words from input
# line = input('Enter the sentence to count words:')
# counts = dict()
# words = line.split()
# print('Words---', words)
# print('---Counting---')
# for word in words:
#     counts[word] = counts.get(word,0) +1 
# print('Count is',counts)

##Dictionary - Get value by iterating through key
people = {'aa':12, 'ddd': 34, 'rto': 67}
# for key in people :
#     print(key, people[key])

# Retrieve lists of keys and Values using dictionary methods 
# without using for loop 
#print ('retrieve people', list(people))  #Retrievs the keys in a list
#print ('retrieve people using key', list(people.keys()))  #Using Dictionary keys() method
#print ('retrieve people count', list(people.values())) # Using Dictionary Values method
#print ('retrieve people all items', list(people.items())) # Using Dictiocnary Items method - Returns List of Tuples

#Iterate through the dictionary using two iterative variable and using items() method
# for key,value in people.items() :
#     print(key, value)

stuff = dict()
print(stuff.get('candy',-1))
