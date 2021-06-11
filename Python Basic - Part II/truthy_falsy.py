#Truthy and falsy

is_old = bool('hello')

is_licensed = bool(5)

print(bool('hello'))
print(bool(5))

#In python all the empty values are considered in boolean as False.
#Rest all values are True.

password = 'gandhi'
username = 'manish'

if password and username:
    print('User exists')