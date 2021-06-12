# Erros in Python.
# Error Handling

# Built-in Exceptions in Python.
# https://docs.python.org/3/library/exceptions.html

# Different types of basics errors are:
# Type Error
# Syntax Error
# Name Error
# Index Error
# Key Error - These are majorly in Dictionaries.
# Zero Division Error
# Value Error

# Error handling

# while True:
#     try:
#         age = int(input('Please enter the age: '))
#         100/age
#         print(age)
#     except (ValueError, ZeroDivisionError) as err:
#         print(err)
#     else:
#         print('Thank You!!')
#         break

while True:
    try:
        age = int(input('Please enter the age: '))
        100/age
        print(age)
    except ValueError as err:
        print('Please enter a number')
        continue
    except ZeroDivisionError as err:
        print('Please enter the age which is greater than 0')
        continue
    else:
        print('Thank You!!')
        break
    finally:
        print('Ok, I am done!!')
    print('Can you hear me')


# We can raise our own exceptions by using below syntax

# raise <Exception>('<message>')
# Ex: raise ValueError('Hey cut it down')
