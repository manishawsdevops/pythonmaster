# Underhood of Generators.

# Firstly, let us understand how the for loop works underneath the hood. This is quite tough.
# but, try to understand.

# Example:

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

# Here we will be passing an iterbale like list or range of values to the function special_for
# after it takes the iterable, We have the iter() function with in the python built-in functions
# which will convert the object or variable into iterable. So, here the given list is converted into
# iterable. Once, it is converted into iterable, we can execute the next() function on it.So, we can
# write a while loop add some logic and next(iterator) will return the next value from the function.
# Once, the list is completed it get the Stop Iteration exception and it gets stopped using a break.
# This is how the underhood the for loops work.

# Example special_for([1,2,3])

# Lets us understand and create a new range for ourselves.
# We can create our own new range function which is nothing but genrator.
# To create a range we need a iterable,first,last. To do this we need to create a function which
# can initialize the values and then convert the object interable and should have a next() function
# in it.

# Lets start creating our own range. It will be typical when we start to learn but, when we try to
# understand again and again we might get some understanding.

# If we observe below we are modifying the dunder methods which are the in-built methods
# created when the object is created out of a class.
# the next function should return the next value so, we should return it.
# current is the class object attribute created to handle the object items.


class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # This below statement will allow the first number as the starting point.
        MyGen.current = self.first

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(4, 100)
for i in gen:
    print(i)
