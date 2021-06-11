#Loops in the python are very powerful.
# for item in <iterable>
# For loop can be iterable on any Iterable item like char,list,tuple,set,dict.



# for item in 'Hello Manish Gandhi':
#     print(item)


#Iterables
user = {
    'name': 'Prabhas',
    'role': 'Hero',
    'age': 100,
    'movie': 'baahubali'
}

for item in user:
    print(item)

for item in user.items():
    print(item)

for item in user.keys():
    print(item)

for item in user.values():
    print(item)

for k,v in user.items():
    print(k,':',v)