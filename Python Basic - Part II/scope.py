#Scope this is the important in functions.
#scope - what variable do i have access to?

#Anything which is defined with in the file has the global scope like below.

#This has a global scope
a = 10

def test():
    k = 5
    print(a)


test()

#Below variable k is not defined as it is not part of the main function.
# print(k)

#Scope Rules
#1 - Start with Loacl
#2 - Parent local?
#3 - Global
#4 - Built in pythin functions.

#global Keyword makes the variable to reference from the global declaration
b = 10

def count():
    global b
    b += 1
    return b

print(count())
print(count())
print(count())


#nonlocal Keyword

x = float(2.8)

str = ' manish '.strip()

my_list = ['a']

my_list.

print(x)

fruits = {"apple", "banana", "cherry"}