# Generator
# This is advanced topic, these are in python allows us to generate values over a time.
# range() is a generator.

# Generators can be used to generate a sequence.

# These are prettu hard initially to understand but they are memory optimised. Observe carefully the
# below example. If a function has "yield" in for loop it is called as generator.

# Basic syntax of generator is
# def <fun_name>():
#   for i in range(num):
#       yield <manipulation on i>

# This is critical here, YIELD will pause the function and checks for the next() function in the
# program and executes it.

# Here in the below example the for loop will iterate over the generator_func().
def generator_func(num):
    for i in range(num):
        yield i


for i in generator_func(10):
    print(i)

g = generator_func(10)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# next(g) will print the next value in the iterable.
# Also, there is a catch in this we cannot iterate the next more than the number of times in the
# iterable.

# huge_list = list(generator_func(100000))
