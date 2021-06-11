# Reduce is bit advanced.
# This will take the accumilator as the input.

# This will automatically prints the output in int. There is no need to convert to list before
# printing.

# reduce(<func_name,<iterable/sequence>,<accumulator_value=0(default)>)


from functools import reduce


list1 = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, list1, 0))


# If you observe the above every time the accumulator will be added with the previous return value.
# this will be quite tough initially but understand carefully. By seeing the output.
