#First with Exception

astr = "Hello"
try:
    istr = int(astr)
except:
    istr = -1

print("First", istr)


#Second without Exception

astr = "1234"
try:
    istr = int(astr)
except:
    istr = -1
print("Second", istr)

#Sample Try Catch

rawstr = input("Enter a number:")

try:
    ival = int(rawstr)
except:
    ival = -1

if ival>0:
    print('No Exception, number is', ival)
else:
    print ( 'Not a number. Input value is', rawstr)