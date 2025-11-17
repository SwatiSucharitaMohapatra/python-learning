import re
#fh = open('regex_sum_42.txt')
# numlists = list()
# for line in fh :
#     line = line.rstrip()
#     nums = re.findall('[0-9]+', line)
#     if len(nums) == 0 : continue
#     for num in nums :
#         numlists.append(int(num))
# print(sum(numlists))

fh = open('regex_sum_data.txt')
numlist = list()
for line in fh :
    line = line.rstrip()
    nums = re.findall('[0-9]+', line)
    if len(nums) == 0 : continue
    for num in nums :
        numlist.append(int(num))
print(len(numlist))        
print(sum(numlist))

print( sum( [ (int(num)) for num in re.findall('[0-9]+',open('regex_sum_data.txt').read()) ] ) )