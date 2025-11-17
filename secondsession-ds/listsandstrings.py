#Split in a String
# str = "Hello Python World"
# values = str.split()
# print("--splitted values ",values)
# for value in values :
#     print("--splitted values looped",value)

#Assignment 8.4
# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     for wrd in line.split() :
#         if wrd in lst :
#             continue
#         lst.append(wrd)
# print("list of words",sorted(lst), 'count---', len(lst))

#Assignment 8.5
# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"
# fh = open(fname)
# count = 0
# for line in fh :
#     line = line.rstrip()
#     if not line.startswith('From ') : 
#         continue
#     words = (line.split())[1]
#     print(words)
#     count = count + 1
# print("There were", count, "lines in the file with From as the first word")