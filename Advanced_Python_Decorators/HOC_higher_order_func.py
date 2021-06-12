# Higher Order Functions
# HOC's are which can take function as a parameter or returns a function.

def greet(func):
    func()


def greet2(func):
    def func():
        return 5
    return func
