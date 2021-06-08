#Tuple
#These are like lists but immutable.
# we are going to use brackets in tupe "()"

#Creation of Tuple

my_tuple = (1,2,3,4,5,5)
print(my_tuple[3])

#Dict can have the key objects as Tuple becuase We can only have the immutable objects as keys.

user = {
    (1,2): 'manish',
    'job': 'student'
}

print(user[(1,2)])


#Tuple has only 2 methods - Count, index.

print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))
