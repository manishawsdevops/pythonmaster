# @@Classmethod and @@staticmethod

# Class method is something which we can call without creating an object.
# static method is something which we can call without creating object but no need to cls variable
# as shown belpow
# These are also called as Decorators.

class Testingmethods:
    membership = True

    def __inti__(self, name, age):
        self.name = name
        self.age = age

    def func1(self):
        pass

    @classmethod  # Class Method  - These are also called as Decorators.
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod  # static Method
    def adding_things2(num1, num2):
        return num1 + num2


print(Testingmethods.adding_things(1, 2))
print(Testingmethods.adding_things2(2, 3))
