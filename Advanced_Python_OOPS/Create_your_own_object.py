# OOPs

# __init is the default method that every class consist of. When ever we create an object for the
# class the __init__ method will be trigger and we need to provide the parameters to it.
# 'slef' is the keyword/variable which is used to refer the current object.

# __init__ is called as the CONSTRUCTOR of the class.


class PlayerCharacter:
    def __init__(self, name, age):  # These are called as Methods
        self.name = name  # These are called as Attributes
        self.age = age

    def run(self):
        print('run')
        return 'Done'


player1 = PlayerCharacter('Manish', 27)
player2 = PlayerCharacter('Gandhi', 26)

# Very important below.
# We can add attributes to the class by adding like this statement after '.' attribute name and value.
player1.attack = 'No Powers'


print(player1)
print(player2)
print(player1.name, '  ', player1.age)
print(player1.run())
print(player2.run())
print(player2.name, '  ', player2.age)
print(player1.attack)
