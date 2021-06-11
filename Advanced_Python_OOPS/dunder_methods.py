# Object Introspection
# The python actually intreperets the object type while it is running.
# So, this type of ability ti interpret the methods the ibject can perform is called as
# Introspection.
# Python provides dir(<obj_name) like functions to introspect.

# For example

a = []

print(dir(a))
# All the methods which are having __<method>__ are called as Dunder methods.


# DUNDER Methods
# These are pre assigned for every class that is being created.
# generally We dont edit these but We do have capability to edit these.
# If we modify the dunder method it is modifed only to that class.


class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __del__(self):
        return "deleted"

    def __call__(self):
        return('yes??')

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
