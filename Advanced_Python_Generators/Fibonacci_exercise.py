# Fibonacci Exercise.

# We can implement this using Generators or we can use this using the lists.

# Anyways using the list we might go out of resources.

# Implementing using the Generators.

# def fibo(num):
#     for i in range(num):
#         yield i


# g = fibo(10)
# next(g)

# for i in range(10):
#     result = i + next(g)
#     print(result)


# r = [0, 1]

# for i in range(20):
#     if i >= 1:
#         k = r[i] + r[i-1]
#         r.append(k)

# print(r)

# Think carefully, here the yield is pausing the function and giving the value to the source and
# resuming again.

def fibo(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + a


for x in fibo(100):
    print(x)
