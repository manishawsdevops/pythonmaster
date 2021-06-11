# List comprehensions
# We call as list comprehensions/set comprehensions/dict comprehensions
# We are able to use comprehensions with list,dict,set.

my_list1 = [char for char in 'hello']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num**2 for num in range(0, 100)]
my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]

print(my_list1)
print('-------------')
print(my_list2)
print('-------------')
print(my_list3)
print('-------------')
print(my_list4)
