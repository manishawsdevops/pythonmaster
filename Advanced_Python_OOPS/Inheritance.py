# Inheritance is the most important concept in OOP and Python.
# Generally Inheritacne is ability to derive from the parent class.
# These are also called as child classes, derived class, sub classes.
# Below example illustrates about the Inheritance.
# Wizard and Archer are inherited from User class.
# Wizard and Archer have access to sign_in method.

class User():
    def sign_in_method(self):
        print('You are logged on')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'You are attacking with power {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'You are attacking with {self.arrows} arrows.')


wizard1 = Wizard('Manish', 100)
archer1 = Archer('Gandhi', 1000)

wizard1.sign_in_method()
wizard1.attack()
archer1.sign_in_method()
archer1.attack()


# We observe alot of Dunder methods has been automatically added to the class when defined.
# This is because when we define a class it is inherited from the based class called "Object"
# in python. So, all the classes will be having the default dunder methods which got derived.

# we can check if the instance/object is inherited from class or not using isinstance(instance,classname) function
# as shown below.
# Observe carefully the below you can understand the concept.

print(isinstance(wizard1, User))
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, object))
print(isinstance(wizard1, Archer))
