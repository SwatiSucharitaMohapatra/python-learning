# larg = -1
# print('Before', larg)
# for num in [9, 41, 12, 3, 74, 15]:
#     if num > larg:
#         larg = num
#     print('large', larg, 'current num', num)
# print('After', larg)

# Counting
# count = 0
# print('Before', count)
# for num in [9, 41, 12, 3, 74, 15]:
#     count = count +1
#     print('current count', count, 'for num', num)
# print('total loop count', count)

#Totaling Loop
# total = 0
# print('Before', total)
# for num in [9, 41, 12, 3, 74, 15]:
#     total = total + num
#     print('current total', total, 'for num', num)
# print('total sum of loop', total)

# Average
# count = 0
# total = 0
# print('Before count', count, 'total', total)
# for num in [9, 41, 12, 3, 74, 15]:
#     count = count +1
#     total = total + num
#     print('current count', count, 'total', total, 'num', num)
# print('After count=', count, ': total=', total, ': Average=', total/count)

# Filter out largest Number
# print('Before ')
# for num in [9, 41, 12, 3, 74, 15]:
#     if num > 20:
#         print('num > 20 in list is', num)
# print('After')

# Search using Booean Value
# found = False
# for num in [9, 41, 12, 3, 74, 15]:
#     if num == 3:
#         found = True
#     print(found, num)
# print('After', found)

# # Get Smallest Value
# smallest = None ## No value in the variable
# print('Before', smallest)
# for num in [9, 41, 12, 3, 74, 15]:
#     if smallest is None : # is is similar to == but stronger than ==
#         smallest = num
#     elif num < smallest :
#         smallest = num
#     print('smallest now', smallest, 'current num', num)
# print('After', smallest)

# Assignmenr
largest = None
smallest = None
print('Before smallest', smallest, 'largest', largest)
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    #print(num)
    try:
        inum = int(num)
       # print('current smallest:', smallest, 'largest:', largest, 'number:', num)
        if smallest is None or largest is None:
            largest = inum
            smallest = inum
        if inum < smallest:
            #print('num', inum, 'smallest', smallest, 'check', inum < smallest)
            smallest = inum
        elif inum > largest:
            largest = inum
        #print('new smallest:', smallest, 'largest:', largest, 'number:', inum)
    except:
        print('Invalid input')
print('Maximum is', largest)
print('Minimum is', smallest)