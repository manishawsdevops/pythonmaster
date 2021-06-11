#Enumerate.
#Enumerate gives the index and the value of the iterable/data structure.

for item in enumerate('Hello'):
    print(type(item))

for i,j in enumerate('Hello'):
    print(f'{i} : {j}')

#print the index of the number 50 in the given range.

for i,j in enumerate(list(range(100))):
    if j == 50:
        print(j)
        print(i)