# Set and Dictionary Comprehensions.

# Set comprehension
my_list1 = {char for char in 'hello'}
my_list2 = {num for num in range(0, 100)}
my_list3 = {num**2 for num in range(0, 100)}
my_list4 = {num**2 for num in range(0, 100) if num % 2 == 0}

print(my_list1)
print('-------------')
print(my_list2)
print('-------------')
print(my_list3)
print('-------------')
print(my_list4)

#########
# Dict Comprehension

sample_dict = {
    'a': 1,
    'b': 2
}

my_new_dict = {k: v**3 for k, v in sample_dict.items()}
print(my_new_dict)

my_new_dict2 = {k: k**3 for k in [1, 2, 3] if k % 2 == 0}
print(my_new_dict2)
