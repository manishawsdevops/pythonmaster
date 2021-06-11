#Functions
#functions start with the degf functions.
#functions should be written in the start of the program.

#Default parameters allows us to give the defauolt value while defining the function.
#Positional Parameters
#return - This is very important while defining the function. If we dont have return while
#defining the function, it will return None.
#Usuallu best practice is to return the value to make the code simple.

#Parameters and Aurguments for the Functions.
#Parameters - These are used while defining the function.
#Arguments - These are the actual values while calling the function.

#Default Parameters and Keyword Arguments.
#Positional Parameters/Aurguments are the ones which are send in exact same position.

#Keyword Arguments



def say_hello(name='baahubali',emoji=':-)'):
    print(f'Hello!!! {name} {emoji}')

#Positional Arguments
say_hello('Manish',':-)')

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def show_tree():
    for i in picture:
        for j in i:
            if j == 0:
                print(' ',end='')
            elif j == 1:
                print('$',end='')
        print('')

# show_tree()

def sum(num1,num2):
    return(num1+num2)

say_hello(emoji=':-)',name='Manish Gandhi')   
say_hello()

print(sum(1,2))


def fun1(num1,num2):
    def fun2(n1,n2):
        return n1+n2
    return fun2(num1,num2)

sum = fun1(10,20)
print(sum)