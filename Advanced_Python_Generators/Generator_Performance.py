# Generator Performance.

# Generators are like range(). They actually donot occupy the space in the memory.

# Let us consider an example as below where we calculated the performace using Decorators.
# Here we are trying to calculated the time taken for execution of two functions long_time and
# long_time_2. In long_time_2 we are providing the list as an input rather than the range.

# Execute the program you will be amazed with the result. Here in the function long_time()
# funtion we are using range() which is nothing but a generator. In the place of the range() you
# can even construct your own generators. Below is the sample code snippet of it.

# def generator_func(num):
#     for i in range(num):
#         yield i

from time import time


def performance(func):
    def wrapper_func(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'Took {t2-t1} secs to execute')
    return wrapper_func


@performance
def long_time():
    for i in range(1000000):
        i*5


@performance
def long_time_2():
    for i in list(range(1000000)):
        i*5


long_time()
long_time_2()
