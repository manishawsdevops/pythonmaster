# # Attributes and Methods.

# # We will be having - class object attributes and Attributes.
# class object attributes are declared in the inside class and those are accesible
# across the class object. For example in the below memborship is a class object attribute.
# Below example illustrates about it and usage of it.

# #if you observe below we are referring the values using the self keyword. Which is very important
# while declaring the classes in python. This self variable is useful for accessing the values from
# various functions with in the class.

# ''' Info between these lines are called Docstrings. ''''

# After creating a class we might be having dunder methods/magic methods that are created automatically
# when the class is created. You can find those by executing help(class_name)
# Foir example: help(PlayerCharacter)

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
