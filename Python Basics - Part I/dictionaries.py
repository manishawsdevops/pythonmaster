# Dictionaries - its a data type in python but also a data structure. Its a way for us to organise the data.
# So, that we can organise the data within it.
# Dict will be having a key and a value. It is an unordered Key value pairs.
# This means that unlike lists Dict variables values are not stored side by side in the memory. Its a catch here.
# Dict variables can only be accesed by the Key.

dictionary = {
    'a': [1, 2, 3],
    'b': 'Hello',
    'x': True
}

my_list = [
    {
        'a': [1, 2, 3],
        'b': 'Hello',
        'x': True
    },
    {
        'a': [4, 5, 6],
        'b': 'Hello',
        'x': True
    }
]

print(dictionary['a'][1])
print(my_list[0]['a'][1])


# Dictories Keys always has to be immutable like int,str,Boolean. A key in the dict has to be unique.

dictionary_1 = {
    'canbestring': 'canbestring',
    1990: 1098,
    True: 'Itsaboolean'
}
print(dictionary_1[1990])


# Dictionary methods. .get()

user = {
    'name': 'Manish Gandhi Dodda',
    'age': 27
}

print(user.get('dob', 1990))

user2 = dict(name='Gandhi', job='devops')
print(user2)

# In dictionaries we can use the keyword 'in' to find an object.

movie = {
    'name': 'baahubali',
    'hero': 'prabhas'
}
# Here the keyword 'in' checks for the Key like hero in above dict movie.
print('hero' in movie)
print('heroine' in movie)

print('baahubali' in movie.values())  # checks if the value is present.
print('baahubali' in movie.keys())  # checks if the key is present.

# This gives the output of the dict items in the form of a list.
print(movie.items())
print(type(movie.items()))  # This is of the type dict_items.


# Dictionary methods  .clear(),.copy(),.popitem().update()
show = {
    'name': 'jabardast',
    'anchor': 'manu'
}

show_1 = show.copy()
print(show)
show.clear()
print(show)
print(show_1)

print(show_1.popitem())
print(show_1)

show_1.update({'anchor': 'anasuya', 'judge': 'roja'})
print(show_1)
