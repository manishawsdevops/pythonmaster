#Built in Functions and Methods
#https://docs.python.org/3/library/functions.html

greet = 'Hellooworld'
print(len(greet))
print(greet[:len(greet)])

#Functions and Methods
# Functions accepts arguments in curly brackets like print()
# Methods are like which start with "." in the front line .format()

quote = 'to be or not to be'

print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be','me'))
print(quote) #If we observe the ouput of this line it is same as the string as above before formatting, 
#This is because of string immutability.

