# __init__ This is the constructor.

# The __init__ provides a lot of control as if we are unable to provide the name or age to the
# constructor it will error out.

# These aconstructors are very helpful to check the initial validations before we go ahead and
# create the actual object in the memory.

class PlayerCharacter:
    '''
    Info:  This creates an object with Player Attributes. 
    '''
    membership = True  # Class Object Attributes. These can be refeered using self.<var_name> or class_name.<var_name>

    def __init__(self, name, age):
        if self.membership:
            self.name = name  # Attributes - These can be referred using self.<var_name>
            self.age = age

    def shout(self):
        '''
        Info: This prints the name to the output.
        '''
        print(f'My name is {self.name}')


player1 = PlayerCharacter('Manish', 26)

print(player1)
print(player1.membership)
print(player1.name)
print(player1.shout())
