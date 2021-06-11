# Lambda Expressions
# These expressions are the functions which are going to execute only once.
# This means that we are not storing this function in the memory.
# lambda <param_name>: <action_on_paramater_like _addition_soOn>

# Below is the example of the map(),reduce(),filter() using with lambda expressions.

from functools import reduce

my_list = [1, 2, 3]

print(list(map(lambda param: param*2, my_list)))
print(list(filter(lambda param: param % 2 != 0, my_list)))
print(reduce(lambda acc, param: acc+param, my_list, 10))

# Understand the above carefully. This can be tricky.
