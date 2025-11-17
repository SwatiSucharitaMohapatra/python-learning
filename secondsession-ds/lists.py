#Range function

print(list(range(6)))

frinds = ['a', 'b', 'c', 'd']
print(list(range(len(frinds))))

#Iterate for loop 
for fr in frinds :
    print(fr)

#Iterate for loop using range/ counted loop
for i in range(len(frinds)) :
    print("---- i",frinds[i])