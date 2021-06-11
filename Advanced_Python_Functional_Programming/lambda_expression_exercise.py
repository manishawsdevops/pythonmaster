# A lamba expression to square the list.
# Square

my_list = [5, 4, 3]

print(list(map(lambda param: param**2, my_list)))


# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1), (11, 0), (15, -9)]

a.sort(key=lambda x: x[1])

print(a)


# Below is the solution i tried
# a = [(0, 2), (4, 3), (9, 9), (10, -1), (11, 0), (15, -9)]

# b = list(map(lambda param: param[1], a))

# b.sort()
# # print(b)

# c = []

# for i in b:
#     c = c + (list(filter(lambda param: i in param, a)))

# print(c)
