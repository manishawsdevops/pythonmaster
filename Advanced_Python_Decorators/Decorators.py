# Decorators
# Decorators have '@" sign in the class defination.
# Notation will be like @<decorator_name>

# Decorators are useful when you are calling the functions. This can be called before any
# function as shown below.
# Decarotors should have a wrapper function and should return a fuction_name(be careful while returning).

# These decorators can take the args as given below.

# Underneath the hood the decorators executes as below.

# a = my_decorator(func)()  --- Understand with the my_decorator return value.

from time import time


def my_decorator(func):
    def wrapper_func(*args, **kwargs):
        print('******$$$$*****')
        func(*args, **kwargs)
        print('******$$$$*****')
    return wrapper_func


@my_decorator
def hello(greeting, emoji=':-)'):
    print(greeting, emoji)


# @my_decorator
# def bye():
#     print('See you later')


hello('Hello Manish Gandhi Dodda')
# bye()

# These decorators are quite tough to understand. But, it is a powerful feature of python.

# Why do we need Decorators?
# Decorators can be used to test the performace as below

# let us take a random calcultaion of 10000000 numbers.
# This is the best way if you want to test the perforamce of the application.


def performance(func):
    def wrapper_func(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'Took {t2-t1} secs to execute')
    return wrapper_func


@performance
def long_time():
    for i in range(1000000000):
        i*5


long_time()
