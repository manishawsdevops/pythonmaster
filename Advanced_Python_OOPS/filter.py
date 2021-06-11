# Filter function accepts the function name and iterable.
# here the filter will return the value olnly if the return of the function is TRUE.
# Always the output of function will be a list. So, we need to convert it to a list.


mylist = [1, 2, 3]


def odd_only(item):
    return item % 2 != 0


print(list(filter(odd_only, mylist)))
