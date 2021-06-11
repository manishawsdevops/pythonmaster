# Zip - It acts like a zipper.
# This will combine with the iterable in the list.
# fist element with the first item of the another iterable.
# Key catch is none of the iterables variables will not be changed.
# zip() will accept multiples iterables.

# Example

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

print(list(zip(list1, list2, list3)))
