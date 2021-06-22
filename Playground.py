# import re

# matrix = [['T', 's', 'i'], ['h', '%', 'x'], ['i', ' ', '#'], [
#     's', 'M', ' '], ['$', 'a', ' '], ['#', 't', '%'], ['i', 'r', '!']]
# # new = list(map(lambda x: x[0], k))

# # str1 = ''.join(new)

# # print(str1)
# # li = []

# m = 7
# n = 3

# li = ['']*(m*n)

# for i, j in enumerate(matrix):
#     # print(j)
#     for a, b in enumerate(j):
#         # print(b)
#         # # # print(idx, item)
#         dest = a*7 + i
#         # # print(dest)
#         # print(b, end='')
#         li[dest] = b
#         # print(b)
#         # print(li[dest])
#         # # # print(a, b)
#         # # print(b, end='')
#         # # print(dest, end='')
#     # print('\n')

# print(li)

# mystring = ''.join(map(str, li))

# print(mystring)

# pattern = re.compile(r"[a-zA-Z]\W+[a-zA-Z]")

# print(re.sub(r"([a-zA-Z])(\W+)([a-zA-Z])", r"\1 \3", mystring))

# # li(pattern.findall(mystring))

from os import write


dict1 = {'email': 'alknlasknclsa@lsnvl',
         'subject': 'slnvkldsnvsd',
         'message': 'aspwmvpnwm'}

list1 = ['sldnvkln', 'ksnvlksndmv', 'lknviwnev']

# with open('database_out.txt', 'w') as file:
#     file.write(str(dict1))
