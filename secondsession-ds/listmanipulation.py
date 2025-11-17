#Concatenate
a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 12]
c = a + b
#print(c)

#Slicing
d = [2, 3, 45, 56, 77, 5, 79, 90]
# print(d[1:6])
# print(d[:6])
# print(d[2:])
# print(d[:])

# print(type(d))
# print(dir(list))

#Append
# d.append('345')
# #print(d)
# print(4 in d)
# print(45 in d)
# print('345' in d)

#Functions
# print(max(d))
# print(min(d))
# print(sum(d))
# print(len(d))
# print(sum(d)/len(d))
# d.sort()
# print(d)

# Average without list and list functions
# total = 0
# count = 0
# while True :
#     inp = input('Enter a number:')
#     if inp == 'done' :
#         break
#     count = count + 1
#     total = total + float(inp)
#print('Average:', total/count)

# Average with list and list functions
l = list()
while True :
    inp = input('Enter a number:')
    if inp == 'Done' :
        print("Breaking out of loop")
        break
    l.append(float(inp))
print('Average:', sum(l)/len(l))