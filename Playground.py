a = [(0, 2), (4, 3), (9, 9), (10, -1)]

b = list(map(lambda param: param[1], a))

b.sort()
# print(b)

c = []

for i in b:
    c = c + (list(filter(lambda param: i in param, a)))

print(c)
