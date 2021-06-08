#strings

print(type("Manish Gandhi!!"))

username = 'baahubali'
password = 'rajamouli'

#Long strings can be used for multi line strings.

long_string = '''   
WOW
O O
---
'''

print(long_string)

first_name = 'Manish'
last_name = 'Dodda'

print(first_name + ' ' + last_name)

#Strig concatenation.
# Strings can concatenation only works with strings.

print('Hello' + ' World')

#Type conversion

print(type(str(100)))
print(type(int(str(100))))
a = '500'
print(type(a))
a = int(a)
print(type(a))


#Escape Sequence - "\" - We should use to escape the symbol and treat as string.
Weather = "\t Manish\'s \n  \"Gandhi\" "
print(Weather)

#Formatted Strings - sytax -- f'' in print says that its a fomratted string and substitutes the variables in
# curly braces.
name = 'Manish'
age = '26'
print(f'Hi {name}. You are {age} years old.')

#String Indexes. - These are stored in memory as ordered sequence.

selfish = '01234567'
print(selfish[0])
print(selfish)

# [start:stop:stepover]

print(selfish[0:8:2])
print(selfish[1:])
print(selfish[:5])
print(selfish[-1])
print(selfish[::-1]) # This provides a reverse of a string in python. Important trick.***

#Immutability. Strings in python are immutable. We cannot change the value of string once it created.
# The only way to change the string is changing the whole value.






