fruit = 'banana'
letter = fruit[0]
# print(letter)

letter = fruit[4]
# print(letter)

x=5
# print(fruit[x-2])

###Length
x = len(fruit)
# print(x)

#Loop through the string - While
index = 0
while index < x :
    # print(fruit[index], index)
    index = index +1

#Loop through the string - For
for character in fruit :
    print(character)

#Loop through the string and counting letters - Count letter a in the fruit string
count = 0
for character in fruit :
    if character == 'a' :
        count = count+1
print(count)

#Loop through the string and counting letters - Count letter a in the fruit string
count = 0
for character in fruit :
    if character == 'a' :
        count = count+1
#print(count)  

# # String slicing
# str = 'my python learning'
# print(str[0:2])
# print(str[7:8])
# print(str[10:25]) 
# print(str[3:6])
# print(str[3:1])  # blank output
# print(str[:6])
# print(str[12:])
# print(str[:])

# String concatenation
# str1 = 'python'
# str2 =  'learning'
# print(str1+str2) # without space

# print(str1+' '+str2) # with space

# in logical operator
# str1 = 'banana'
# print('n' in str1)
# print('m' in str1)
# print('nan' in str1)
# if 'n' in str1 :
#     print("Yes it is!!!")

# functions of String operator
# str1 = 'banana'
# print(type(str1))
# print(dir(str))

# find operator
# str1 = 'banana'
# print("----",str1.find('na'))
# print(str1.find('sw'))

# Upper and Lower case operator
# str1 = 'banana'
# print("----",str1.upper())
# print("DDDDDD".lower())

# Search and Replace
# str1 = 'banana'
# print(str1.replace('a', 'b'))

# Parcing and Extracting
data = 'From ssss.dsifsdfs@vf.fff.ff date 12.3.23'
atpos1 = data.find('@')
print("---", atpos1)
atpos2 = data.find(" ", atpos1)
print(".....", atpos2)
finaldata = data[atpos1+1 : atpos2]
print('final string', finaldata)