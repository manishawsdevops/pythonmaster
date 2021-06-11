# Map function in Python map()
# By map we can call the function with a iterable.

# map(<function_name>,<iterable>)

my_list = [1, 2, 3]


def multiply_by_2(item):
    return item*2


print(list(map(multiply_by_2, my_list)))
